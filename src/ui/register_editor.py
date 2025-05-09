#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
from typing import Optional, List, Dict, Any, Union, cast

from PySide6.QtWidgets import (
    QWidget,
    QFileDialog,
    QMessageBox,
    QTableView,
    QLineEdit,
    QCheckBox,
    QComboBox,
    QPushButton,
    QLabel,
    QApplication,
    QAbstractItemView,
    QHeaderView,
    QDialog,
)
from PySide6.QtCore import Qt, QSortFilterProxyModel, Signal, Slot, QModelIndex
from PySide6.QtUiTools import QUiLoader

from src.models.register_model import RegisterData, RegisterTableModel
from src.controllers.register_controller import RegisterController


class RegisterEditor(QDialog):
    """寄存器编辑器窗口类"""

    def __init__(self, parent: Optional[QWidget] = None) -> None:
        super().__init__(parent)

        # 设置窗口标题和属性
        self.setWindowTitle("寄存器数据编辑器")
        self.setMinimumSize(800, 600)

        # 加载UI
        loader = QUiLoader()
        ui_path = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            "ui",
            "register_editor.ui",
        )
        self.ui = loader.load(ui_path, self)

        # 初始化模型和控制器
        self.register_model = RegisterTableModel(self)
        self.register_controller = RegisterController(self.register_model, self)

        # 创建代理模型用于筛选
        self.proxy_model = QSortFilterProxyModel(self)
        self.proxy_model.setSourceModel(self.register_model)

        # 获取UI组件引用
        self.table_view = self.findChild(QTableView, "registerTableView")

        # 获取过滤器组件
        self.address_filter = self.findChild(QLineEdit, "addressFilterEdit")
        self.name_filter = self.findChild(QLineEdit, "nameFilterEdit")
        self.desc_filter = self.findChild(QLineEdit, "descFilterEdit")
        self.show_modified_checkbox = self.findChild(QCheckBox, "showModifiedCheckBox")

        # 获取详细信息组件
        self.address_edit = self.findChild(QLineEdit, "addressEdit")
        self.name_edit = self.findChild(QLineEdit, "nameEdit")
        self.value_edit = self.findChild(QLineEdit, "valueEdit")
        self.dec_value_label = self.findChild(QLabel, "decValue")
        self.binary_value_label = self.findChild(QLabel, "binaryValue")
        self.description_edit = self.findChild(QLineEdit, "descriptionEdit")
        self.writable_checkbox = self.findChild(QCheckBox, "writableCheckBox")

        # 获取按钮
        self.new_button = self.findChild(QPushButton, "newButton")
        self.open_button = self.findChild(QPushButton, "openButton")
        self.save_button = self.findChild(QPushButton, "saveButton")
        self.import_button = self.findChild(QPushButton, "importButton")
        self.export_button = self.findChild(QPushButton, "exportButton")
        self.add_button = self.findChild(QPushButton, "addButton")
        self.delete_button = self.findChild(QPushButton, "deleteButton")
        self.reset_button = self.findChild(QPushButton, "resetButton")
        self.apply_button = self.findChild(QPushButton, "applyButton")
        self.cancel_button = self.findChild(QPushButton, "cancelButton")

        # 获取Combo Box
        self.device_combo = self.findChild(QComboBox, "deviceComboBox")
        self.register_group_combo = self.findChild(QComboBox, "registerGroupComboBox")

        # 获取状态标签
        self.status_label = self.findChild(QLabel, "statusLabel")

        # 设置模型
        if self.table_view:
            self.table_view.setModel(self.proxy_model)
            # 设置自动调整列宽
            self.table_view.horizontalHeader().setSectionResizeMode(
                3, QHeaderView.ResizeMode.Stretch
            )
            self.table_view.setSelectionBehavior(
                QAbstractItemView.SelectionBehavior.SelectRows
            )

        # 初始状态
        self.current_selected_index = -1
        self.editing_new_register = False

        # 连接信号和槽
        self.connect_signals()

        # 设置示例数据
        self.loadSampleData()

    def connect_signals(self) -> None:
        """连接信号和槽"""
        # 表格选择变更信号
        if self.table_view:
            self.table_view.selectionModel().selectionChanged.connect(
                self.on_selection_changed
            )

        # 按钮点击信号
        if self.new_button:
            self.new_button.clicked.connect(self.on_new_clicked)
        if self.open_button:
            self.open_button.clicked.connect(self.on_open_clicked)
        if self.save_button:
            self.save_button.clicked.connect(self.on_save_clicked)
        if self.import_button:
            self.import_button.clicked.connect(self.on_import_clicked)
        if self.export_button:
            self.export_button.clicked.connect(self.on_export_clicked)
        if self.add_button:
            self.add_button.clicked.connect(self.on_add_clicked)
        if self.delete_button:
            self.delete_button.clicked.connect(self.on_delete_clicked)
        if self.reset_button:
            self.reset_button.clicked.connect(self.on_reset_clicked)
        if self.apply_button:
            self.apply_button.clicked.connect(self.on_apply_clicked)
        if self.cancel_button:
            self.cancel_button.clicked.connect(self.on_cancel_clicked)

        # 过滤器变更信号
        if self.address_filter:
            self.address_filter.textChanged.connect(self.update_filter)
        if self.name_filter:
            self.name_filter.textChanged.connect(self.update_filter)
        if self.desc_filter:
            self.desc_filter.textChanged.connect(self.update_filter)
        if self.show_modified_checkbox:
            self.show_modified_checkbox.stateChanged.connect(self.update_filter)

        # 值编辑器变更信号
        if self.value_edit:
            self.value_edit.textChanged.connect(self.update_value_displays)

        # 控制器信号
        self.register_controller.registersSaved.connect(self.on_registers_saved)
        self.register_controller.registersLoaded.connect(self.on_registers_loaded)
        self.register_controller.error.connect(self.show_error)

    def update_filter(self) -> None:
        """更新过滤器"""
        address_filter = self.address_filter.text() if self.address_filter else ""
        name_filter = self.name_filter.text() if self.name_filter else ""
        desc_filter = self.desc_filter.text() if self.desc_filter else ""
        show_modified = (
            self.show_modified_checkbox.isChecked()
            if self.show_modified_checkbox
            else False
        )

        # 实现自定义过滤逻辑
        self.proxy_model.setFilterKeyColumn(-1)  # 所有列

        # 自定义过滤器函数
        def filter_func(row: int, parent_index: QModelIndex) -> bool:
            source_model = cast(RegisterTableModel, self.proxy_model.sourceModel())

            # 地址过滤
            if (
                address_filter
                and address_filter.lower()
                not in str(source_model.data(source_model.index(row, 0))).lower()
            ):
                return False

            # 名称过滤
            if (
                name_filter
                and name_filter.lower()
                not in str(source_model.data(source_model.index(row, 1))).lower()
            ):
                return False

            # 描述过滤
            if (
                desc_filter
                and desc_filter.lower()
                not in str(source_model.data(source_model.index(row, 3))).lower()
            ):
                return False

            # 修改过的寄存器过滤
            if show_modified:
                reg = source_model.getRegisterByIndex(row)
                if reg and reg.value == reg.original_value:
                    return False

            return True

        self.proxy_model.setFilterRegularExpression("")
        self.proxy_model.setFilterFixedString("")
        self.proxy_model.setFilterCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)

        # 应用自定义过滤器
        self.proxy_model.setFilterRole(Qt.ItemDataRole.UserRole)  # 使用自定义角色

        # 更新所有行以触发过滤
        source_model = cast(RegisterTableModel, self.proxy_model.sourceModel())
        for row in range(source_model.rowCount()):
            visible = filter_func(row, QModelIndex())
            source_index = source_model.index(row, 0)
            proxy_index = self.proxy_model.mapFromSource(source_index)
            if proxy_index.isValid():
                self.proxy_model.setData(proxy_index, visible, Qt.ItemDataRole.UserRole)

    def update_value_displays(self) -> None:
        """更新值的不同显示格式"""
        if (
            not self.value_edit
            or not self.dec_value_label
            or not self.binary_value_label
        ):
            return

        try:
            value_text = self.value_edit.text()

            # 尝试将值转换为整数
            if value_text.startswith("0x"):
                # 十六进制
                value = int(value_text, 16)
            else:
                # 尝试十进制转换
                value = int(value_text)

            # 更新显示
            self.dec_value_label.setText(str(value))
            self.binary_value_label.setText(bin(value)[2:].zfill(8))

        except ValueError:
            # 无法转换为数字，清空显示
            self.dec_value_label.setText("--")
            self.binary_value_label.setText("--------")

    def loadSampleData(self) -> None:
        """加载示例数据"""
        # 添加一些设备选项
        if self.device_combo:
            self.device_combo.clear()
            self.device_combo.addItem("设备1")
            self.device_combo.addItem("设备2")
            self.device_combo.addItem("设备3")

        # 添加一些寄存器组选项
        if self.register_group_combo:
            self.register_group_combo.clear()
            self.register_group_combo.addItem("控制寄存器")
            self.register_group_combo.addItem("状态寄存器")
            self.register_group_combo.addItem("配置寄存器")

        # 添加一些示例寄存器
        registers = []
        for i in range(20):
            address = f"0x{i*4:04X}"
            name = f"REG_{i}"
            value = f"0x{i*16:04X}"
            description = f"寄存器 {i} 描述，用于控制功能 {i}"
            writable = i % 2 == 0  # 偶数寄存器可写

            register = RegisterData(address, name, value, description, writable)
            registers.append(register)

        # 加载寄存器数据
        self.register_model.loadRegisters(registers)

        # 更新状态
        if self.status_label:
            self.status_label.setText("已加载示例数据")

    def show_error(self, message: str) -> None:
        """显示错误信息

        Args:
            message: 错误信息
        """
        QMessageBox.critical(self, "错误", message)
        if self.status_label:
            self.status_label.setText(f"错误: {message}")

    def on_selection_changed(self) -> None:
        """表格选择变更时的处理"""
        if not self.table_view:
            return

        # 获取当前选中行
        selected_indexes = self.table_view.selectionModel().selectedRows()

        if not selected_indexes:
            # 没有选中行
            self.clear_detail_form()
            self.current_selected_index = -1
            return

        # 获取选中行的模型索引
        proxy_index = selected_indexes[0]
        source_index = self.proxy_model.mapToSource(proxy_index)
        row = source_index.row()
        self.current_selected_index = row

        # 获取寄存器数据
        register = cast(
            RegisterTableModel, self.proxy_model.sourceModel()
        ).getRegisterByIndex(row)

        if register is not None:
            # 更新详细信息表单
            if self.address_edit:
                self.address_edit.setText(register.address)
            if self.name_edit:
                self.name_edit.setText(register.name)
            if self.value_edit:
                self.value_edit.setText(register.value)
            if self.description_edit:
                self.description_edit.setText(register.description)
            if self.writable_checkbox:
                self.writable_checkbox.setChecked(register.writable)

            # 更新值的显示
            self.update_value_displays()

            # 设置只读状态
            if self.address_edit:
                self.address_edit.setReadOnly(not self.editing_new_register)
            if self.name_edit:
                self.name_edit.setReadOnly(not self.editing_new_register)
            if self.value_edit:
                self.value_edit.setReadOnly(
                    not register.writable and not self.editing_new_register
                )
            if self.description_edit:
                self.description_edit.setReadOnly(not self.editing_new_register)
            if self.writable_checkbox:
                self.writable_checkbox.setEnabled(self.editing_new_register)

    def clear_detail_form(self) -> None:
        """清空详细信息表单"""
        if self.address_edit:
            self.address_edit.setText("")
        if self.name_edit:
            self.name_edit.setText("")
        if self.value_edit:
            self.value_edit.setText("")
        if self.description_edit:
            self.description_edit.setText("")
        if self.writable_checkbox:
            self.writable_checkbox.setChecked(True)
        if self.dec_value_label:
            self.dec_value_label.setText("0")
        if self.binary_value_label:
            self.binary_value_label.setText("00000000")

    @Slot()
    def on_new_clicked(self) -> None:
        """新建按钮点击事件"""
        # 确认是否放弃未保存的更改
        modified_count = len(self.register_model.getModifiedRegisters())
        if modified_count > 0:
            reply = QMessageBox.question(
                self,
                "确认新建",
                f"有 {modified_count} 个寄存器的值已修改但未保存。确定要新建并放弃更改吗？",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                QMessageBox.StandardButton.No,
            )

            if reply == QMessageBox.StandardButton.No:
                return

        # 创建新文件
        self.register_controller.newFile()
        if self.status_label:
            self.status_label.setText("已创建新文件")

    @Slot()
    def on_open_clicked(self) -> None:
        """打开按钮点击事件"""
        # 确认是否放弃未保存的更改
        modified_count = len(self.register_model.getModifiedRegisters())
        if modified_count > 0:
            reply = QMessageBox.question(
                self,
                "确认打开",
                f"有 {modified_count} 个寄存器的值已修改但未保存。确定要打开新文件并放弃更改吗？",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                QMessageBox.StandardButton.No,
            )

            if reply == QMessageBox.StandardButton.No:
                return

        # 打开文件对话框
        file_path, _ = QFileDialog.getOpenFileName(
            self, "打开寄存器配置文件", "", "寄存器配置文件 (*.csv *.txt);;所有文件 (*)"
        )

        if file_path:
            # 加载文件
            self.register_controller.loadFromFile(file_path)

    @Slot()
    def on_save_clicked(self) -> None:
        """保存按钮点击事件"""
        # 如果没有当前文件路径，弹出保存对话框
        if not self.register_controller.current_file_path:
            file_path, _ = QFileDialog.getSaveFileName(
                self, "保存寄存器配置文件", "", "寄存器配置文件 (*.csv);;所有文件 (*)"
            )

            if not file_path:
                return

            # 确保文件后缀为.csv
            if not file_path.endswith(".csv"):
                file_path += ".csv"

            # 保存文件
            self.register_controller.saveToFile(file_path)
        else:
            # 直接保存到当前文件
            self.register_controller.saveToFile("")

    @Slot()
    def on_import_clicked(self) -> None:
        """导入设备按钮点击事件"""
        # 获取当前选择的设备和寄存器组
        device = self.device_combo.currentText() if self.device_combo else ""
        register_group = (
            self.register_group_combo.currentText() if self.register_group_combo else ""
        )

        if not device:
            self.show_error("请先选择设备")
            return

        # 确认是否放弃未保存的更改
        modified_count = len(self.register_model.getModifiedRegisters())
        if modified_count > 0:
            reply = QMessageBox.question(
                self,
                "确认导入",
                f"有 {modified_count} 个寄存器的值已修改但未保存。确定要从设备导入并放弃更改吗？",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                QMessageBox.StandardButton.No,
            )

            if reply == QMessageBox.StandardButton.No:
                return

        # 从设备导入
        self.register_controller.importFromDevice(device, register_group)

    @Slot()
    def on_export_clicked(self) -> None:
        """导出设备按钮点击事件"""
        # 检查是否有修改过的寄存器
        modified_registers = self.register_model.getModifiedRegisters()
        if not modified_registers:
            self.show_error("没有修改过的寄存器值需要导出")
            return

        # 确认导出
        reply = QMessageBox.question(
            self,
            "确认导出",
            f"将向设备写入 {len(modified_registers)} 个修改过的寄存器值，确定继续吗？",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No,
        )

        if reply == QMessageBox.StandardButton.Yes:
            # 导出到设备
            self.register_controller.exportToDevice()

    @Slot()
    def on_add_clicked(self) -> None:
        """添加按钮点击事件"""
        # 创建新的寄存器数据
        self.editing_new_register = True

        # 清空并启用表单
        self.clear_detail_form()

        # 设置可编辑
        if self.address_edit:
            self.address_edit.setReadOnly(False)
        if self.name_edit:
            self.name_edit.setReadOnly(False)
        if self.value_edit:
            self.value_edit.setReadOnly(False)
        if self.description_edit:
            self.description_edit.setReadOnly(False)
        if self.writable_checkbox:
            self.writable_checkbox.setEnabled(True)

        # 取消表格选择
        if self.table_view:
            self.table_view.clearSelection()

        self.current_selected_index = -1
        if self.address_edit:
            self.address_edit.setFocus()

    @Slot()
    def on_delete_clicked(self) -> None:
        """删除按钮点击事件"""
        if self.current_selected_index < 0:
            self.show_error("请先选择一个寄存器")
            return

        # 确认删除
        reply = QMessageBox.question(
            self,
            "确认删除",
            "确定要删除选中的寄存器吗？",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No,
        )

        if reply == QMessageBox.StandardButton.Yes:
            # 从模型中删除
            self.register_model.beginRemoveRows(
                QModelIndex(), self.current_selected_index, self.current_selected_index
            )
            del self.register_model.registers[self.current_selected_index]
            self.register_model.endRemoveRows()

            # 清空表单
            self.clear_detail_form()
            self.current_selected_index = -1

    @Slot()
    def on_reset_clicked(self) -> None:
        """重置按钮点击事件"""
        # 确认重置
        reply = QMessageBox.question(
            self,
            "确认重置",
            "确定要重置所有修改过的寄存器值吗？",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No,
        )

        if reply == QMessageBox.StandardButton.Yes:
            # 重置所有修改
            self.register_controller.resetChanges()

            # 更新当前选中项
            self.on_selection_changed()

            if self.status_label:
                self.status_label.setText("已重置所有修改")

    @Slot()
    def on_apply_clicked(self) -> None:
        """应用按钮点击事件"""
        if (
            not self.address_edit
            or not self.name_edit
            or not self.value_edit
            or not self.description_edit
            or not self.writable_checkbox
        ):
            return

        if self.editing_new_register:
            # 添加新寄存器
            address = self.address_edit.text()
            name = self.name_edit.text()
            value = self.value_edit.text()
            description = self.description_edit.text()
            writable = self.writable_checkbox.isChecked()

            # 验证输入
            if not address or not name or not value:
                self.show_error("地址、名称和值不能为空")
                return

            # 创建新寄存器
            register = RegisterData(address, name, value, description, writable)

            # 添加到模型
            self.register_model.addRegister(register)

            # 退出编辑模式
            self.editing_new_register = False

            if self.status_label:
                self.status_label.setText(f"已添加新寄存器: {name}")

        elif self.current_selected_index >= 0:
            # 更新现有寄存器
            reg = cast(
                RegisterTableModel, self.proxy_model.sourceModel()
            ).getRegisterByIndex(self.current_selected_index)

            if reg is not None:
                # 只更新可写的值
                if reg.writable:
                    new_value = self.value_edit.text()
                    if new_value != reg.value:
                        # 更新值
                        self.register_controller.updateRegisterValue(
                            reg.address, reg.name, new_value
                        )
                        if self.status_label:
                            self.status_label.setText(f"已更新寄存器: {reg.name}")
                    else:
                        if self.status_label:
                            self.status_label.setText("值未修改")
                else:
                    self.show_error("该寄存器不可写")

    @Slot()
    def on_cancel_clicked(self) -> None:
        """取消按钮点击事件"""
        if self.editing_new_register:
            # 取消添加新寄存器
            self.editing_new_register = False

            # 恢复选择
            if self.table_view and self.table_view.model().rowCount() > 0:
                self.table_view.selectRow(0)

            if self.status_label:
                self.status_label.setText("已取消添加")
        else:
            # 恢复原值
            self.on_selection_changed()
            if self.status_label:
                self.status_label.setText("已取消修改")

    @Slot()
    def on_registers_saved(self) -> None:
        """寄存器保存成功事件"""
        if self.status_label:
            self.status_label.setText(
                f"已保存到文件: {self.register_controller.current_file_path}"
            )

    @Slot()
    def on_registers_loaded(self) -> None:
        """寄存器加载成功事件"""
        if not self.status_label:
            return

        if self.register_controller.current_file_path:
            self.status_label.setText(
                f"已从文件加载: {self.register_controller.current_file_path}"
            )
        else:
            self.status_label.setText("已从设备加载")

        # 选择第一行
        if self.table_view and self.table_view.model().rowCount() > 0:
            self.table_view.selectRow(0)


# 用于测试
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RegisterEditor()
    window.show()
    sys.exit(app.exec())
