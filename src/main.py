#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QFileSystemModel,
    QMessageBox,
    QListWidgetItem,
)
from PySide6.QtCore import QDir, Qt
from PySide6.QtUiTools import QUiLoader

from src.models.diagnostic_model import DiagnosticResult
from src.controllers.diagnostic_controller import DiagnosticController
from src.models.acl_model import ACLTableModel
from src.models.device_model import DeviceListModel, Device
from src.models.packet_model import PacketCaptureModel
from src.controllers.packet_sender_controller import PacketSenderController

# 设置资源路径
UI_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "src", "ui"
)
MAIN_UI = os.path.join(UI_DIR, "main_window.ui")

# 应用模式
MODE_OFFLINE = 0
MODE_ONLINE = 1
MODE_DEMO = 2


class PkjvizMainWindow(QMainWindow):
    """Pkjviz主窗口类"""

    def __init__(self) -> None:
        super().__init__()

        # 应用模式
        self.app_mode = MODE_OFFLINE

        # 加载UI
        loader = QUiLoader()
        ui_widget = loader.load(MAIN_UI)

        # 设置中心部件
        self.setCentralWidget(ui_widget)

        # 保存UI引用
        self.ui = ui_widget

        # 初始化模型
        self.init_models()

        # 初始化控制器
        self.init_controllers()

        # 初始化UI组件
        self.init_ui()

        # 连接信号和槽
        self.connect_signals()

        # 设置状态栏
        self.statusBar().showMessage("就绪")

    def init_models(self) -> None:
        """初始化数据模型"""
        # 诊断结果模型
        self.diagnostic_model = DiagnosticResult(self)

        # ACL表格模型
        self.acl_model = ACLTableModel(self)

        # 设备列表模型
        self.device_model = DeviceListModel(self)

        # 数据包捕获模型
        self.packet_model = PacketCaptureModel(self)

    def init_controllers(self) -> None:
        """初始化控制器"""
        # 诊断结果控制器
        self.diagnostic_controller = DiagnosticController(self.diagnostic_model, self)

        # 数据包发送控制器
        self.packet_sender_controller = PacketSenderController(self)

    def init_ui(self) -> None:
        """初始化UI组件"""
        # 设置文件浏览器
        self.file_model = QFileSystemModel()
        self.file_model.setRootPath(QDir.homePath())
        self.ui.fileExplorerTreeView.setModel(self.file_model)
        self.ui.fileExplorerTreeView.setRootIndex(
            self.file_model.index(QDir.homePath())
        )

        # 只显示文件名列
        for i in range(1, self.file_model.columnCount()):
            self.ui.fileExplorerTreeView.hideColumn(i)

        # 初始化其他UI组件
        self.ui.codeEditor.setPlaceholderText("# 在这里输入Python代码")

        # 处理设备列表
        # 使用QListWidget的方式添加设备项，而不是设置模型
        self.device_model.scan_devices()  # 扫描设备但不设置模型

        # 设置数据包捕获模型
        self.ui.packetCaptureTableView.setModel(self.packet_model)

        # 确保设备相关组件默认隐藏（离线模式）
        self.ui.deviceListWidget.setVisible(False)
        self.ui.deviceListView.setVisible(False)
        self.ui.deviceToolsWidget.setVisible(False)
        self.ui.selectedDeviceLabel.setVisible(False)
        self.ui.deviceListLabel.setVisible(False)

        # 初始状态为离线模式
        self.set_app_mode(MODE_OFFLINE)

    def connect_signals(self) -> None:
        """连接信号和槽"""
        # 按钮事件
        self.ui.newButton.clicked.connect(self.new_file)
        self.ui.openButton.clicked.connect(self.open_file)
        self.ui.saveButton.clicked.connect(self.save_file)
        self.ui.runButton.clicked.connect(self.run_code)
        self.ui.stopButton.clicked.connect(self.stop_execution)

        # 在线/离线模式切换
        self.ui.offlineButton.clicked.connect(lambda: self.set_app_mode(MODE_OFFLINE))
        self.ui.onlineButton.clicked.connect(lambda: self.set_app_mode(MODE_ONLINE))
        self.ui.displayButton.clicked.connect(lambda: self.set_app_mode(MODE_DEMO))

        # 环境选择事件
        self.ui.envComboBox.currentIndexChanged.connect(self.environment_changed)

        # 文件浏览器事件
        self.ui.fileExplorerTreeView.doubleClicked.connect(self.open_selected_file)

        # 设备管理事件
        self.ui.refreshButton.clicked.connect(self.refresh_devices)
        self.ui.sendPacketButton.clicked.connect(self.send_packet)
        self.ui.deviceListView.itemDoubleClicked.connect(self.device_double_clicked)

    def set_app_mode(self, mode: int) -> None:
        """设置应用模式

        Args:
            mode: 应用模式，MODE_OFFLINE、MODE_ONLINE或MODE_DEMO
        """
        self.app_mode = mode

        # 重置所有模式按钮状态
        self.ui.offlineButton.setEnabled(True)
        self.ui.onlineButton.setEnabled(True)
        self.ui.displayButton.setEnabled(True)

        if mode == MODE_OFFLINE:
            # 离线模式
            self.log_message("切换到离线模式")
            # 隐藏设备相关组件
            self.ui.deviceListWidget.setVisible(False)
            self.ui.deviceListView.setVisible(False)
            self.ui.deviceToolsWidget.setVisible(False)
            self.ui.selectedDeviceLabel.setVisible(False)
            self.ui.deviceListLabel.setVisible(False)

            # 显示Log编辑器
            self.ui.logWidget.setVisible(True)

            # 设置数据浏览器
            self.ui.dataBrowserWidget.setVisible(True)
            self.ui.dataBrowserLabel.setText("寄存器数据编辑器")

            # 设置对应按钮状态
            self.ui.offlineButton.setEnabled(False)
        elif mode == MODE_ONLINE:
            # 在线模式
            self.log_message("切换到在线模式")
            # 显示设备相关组件
            self.ui.deviceListWidget.setVisible(True)
            self.ui.deviceListView.setVisible(True)
            self.ui.deviceToolsWidget.setVisible(True)
            self.ui.selectedDeviceLabel.setVisible(True)
            self.ui.deviceListLabel.setVisible(True)

            # 显示Log编辑器
            self.ui.logWidget.setVisible(True)

            # 设置数据浏览器为数据包捕获
            self.ui.dataBrowserWidget.setVisible(True)
            self.ui.dataBrowserLabel.setText("数据包捕获")

            # 设置对应按钮状态
            self.ui.onlineButton.setEnabled(False)

            # 扫描设备
            self.refresh_devices()

            # 生成测试数据
            self.packet_model.generate_test_data()
            self.ui.packetCaptureTableView.resizeColumnsToContents()
        else:  # MODE_DEMO
            # 演示模式
            self.log_message("切换到演示模式")

            # 隐藏设备相关组件
            self.ui.deviceListWidget.setVisible(False)
            self.ui.deviceListView.setVisible(False)
            self.ui.deviceToolsWidget.setVisible(False)
            self.ui.selectedDeviceLabel.setVisible(False)
            self.ui.deviceListLabel.setVisible(False)

            # 隐藏Log编辑器
            self.ui.logWidget.setVisible(False)

            # 设置数据浏览器为演示数据
            self.ui.dataBrowserLabel.setText("演示数据")
            self.ui.dataBrowserWidget.setVisible(True)

            # 生成演示数据（比测试数据更丰富）
            self.packet_model.generate_demo_data()
            self.ui.packetCaptureTableView.resizeColumnsToContents()

            # 设置对应按钮状态
            self.ui.displayButton.setEnabled(False)

    def new_file(self) -> None:
        """创建新文件"""
        # 添加新标签页
        self.log_message("创建新文件")

    def open_file(self) -> None:
        """打开文件"""
        self.log_message("打开文件对话框")

    def save_file(self) -> None:
        """保存文件"""
        self.log_message("保存当前文件")

    def run_code(self) -> None:
        """运行代码"""
        self.log_message("开始执行代码")

        # 模拟运行结果
        self.diagnostic_controller.update_diagnostic(
            code="DIAG-001",
            action="检查端口配置并重启服务",
            table_name="ACL_TABLE",
            table_desc="访问控制列表表，用于存储ACL规则",
            fields=[
                {"name": "acl_id", "description": "ACL唯一标识符", "value": "1001"},
                {"name": "priority", "description": "规则优先级", "value": "100"},
                {"name": "action", "description": "执行动作", "value": "PERMIT"},
            ],
        )

    def stop_execution(self) -> None:
        """停止执行"""
        self.log_message("停止执行")

        # 清空诊断结果
        self.diagnostic_controller.clear()

    def environment_changed(self, index: int) -> None:
        """环境变更事件"""
        env = self.ui.envComboBox.itemText(index)
        self.log_message(f"切换环境: {env}")

    def open_selected_file(self, index: int) -> None:
        """打开选中的文件"""
        path = self.file_model.filePath(index)
        if os.path.isfile(path):
            self.log_message(f"打开文件: {path}")

    def refresh_devices(self) -> None:
        """刷新设备列表"""
        # 如果是离线模式或演示模式，不执行操作
        if self.app_mode == MODE_OFFLINE or self.app_mode == MODE_DEMO:
            return

        self.log_message("刷新设备列表")
        # 清空当前列表
        self.ui.deviceListView.clear()
        # 获取设备并添加到列表
        count = self.device_model.scan_devices()
        # 从模型中获取设备并添加到列表控件
        for i in range(count):
            device_name = self.device_model.data(
                self.device_model.index(i, 0), Qt.DisplayRole
            )
            device_data = self.device_model.data(
                self.device_model.index(i, 0), Qt.UserRole
            )
            item = QListWidgetItem(device_name)
            item.setData(Qt.UserRole, device_data)
            self.ui.deviceListView.addItem(item)
        self.log_message(f"发现 {count} 个设备")

    def send_packet(self) -> None:
        """发送数据包"""
        # 如果是离线模式或演示模式，不执行操作
        if self.app_mode == MODE_OFFLINE or self.app_mode == MODE_DEMO:
            return

        # 获取选中的设备
        selected_items = self.ui.deviceListView.selectedItems()
        if not selected_items:
            QMessageBox.warning(self, "警告", "请先选择一个设备")
            return

        # 获取设备
        item = selected_items[0]
        device = item.data(Qt.UserRole)

        if device:
            self.log_message(f"打开发包工具: {device}")
            self.packet_sender_controller.show_dialog(device)

    def device_double_clicked(self, item: QListWidgetItem) -> None:
        """设备双击事件"""
        # 如果是离线模式或演示模式，不执行操作
        if self.app_mode == MODE_OFFLINE or self.app_mode == MODE_DEMO:
            return

        # 注意这里的参数应该是QListWidgetItem，而不是QModelIndex
        device = item.data(Qt.UserRole)
        if device:
            self.log_message(f"连接到设备: {device}")

    def log_message(self, message: str) -> None:
        """在控制台添加日志消息"""
        import time

        time_str = f"[{time.strftime('%H:%M:%S')}]"
        self.ui.consoleTextEdit.append(f"{time_str} {message}")


def main() -> None:
    """主函数"""
    app = QApplication(sys.argv)
    window = PkjvizMainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
