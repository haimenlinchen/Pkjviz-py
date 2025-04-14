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
    QTreeView,
    QTextEdit,
    QTableView,
    QWidget,
    QLabel,
    QListWidget,
    QPushButton,
    QComboBox,
    QSplitter,
    QVBoxLayout,
    QHBoxLayout,
    QTreeWidget,
    QTreeWidgetItem,
    QHeaderView,
    QDialog,
    QTabWidget
)
from PySide6.QtCore import QDir, Qt
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QFont, QStandardItemModel, QStandardItem

from src.models.diagnostic_model import DiagnosticResult
from src.controllers.diagnostic_controller import DiagnosticController
from src.models.acl_model import ACLTableModel
from src.models.device_model import DeviceListModel, Device
from src.models.packet_model import PacketCaptureModel
from src.controllers.packet_sender_controller import PacketSenderController
from src.controllers.login_controller import LoginController
from src.ui.register_editor import RegisterEditor

# 设置资源路径
UI_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "src", "ui"
)
MAIN_UI = os.path.join(UI_DIR, "main_window.ui")

# 应用模式
MODE_OFFLINE = 0
MODE_ONLINE = 1
MODE_DEMO = 2


class PacketSenderWindow(QDialog):
    """发包工具独立窗口类"""
    
    def __init__(self, parent=None, packet_sender_controller=None) -> None:
        super().__init__(parent)
        self.packet_sender_controller = packet_sender_controller
        self.setWindowTitle("发包工具")
        self.setMinimumSize(800, 600)
        
        # 创建布局
        self._create_ui()
        
    def _create_ui(self) -> None:
        """创建UI组件"""
        # 导入需要的模块
        from PySide6.QtWidgets import (
            QWidget, QVBoxLayout, QHBoxLayout, QLabel, QTreeView, 
            QSplitter, QTextEdit, QPushButton, QTableView, QTreeWidget,
            QTreeWidgetItem, QHeaderView
        )
        
        main_layout = QVBoxLayout(self)
        
        # 设置样式
        self.setStyleSheet("""
            QWidget {
                background-color: #F5F5F5;
                color: #333333;
            }
            QLabel {
                font-weight: bold;
                color: #333333;
                background-color: transparent;
            }
            QPushButton {
                background-color: #E0E0E0;
                border: 1px solid #BBBBBB;
                border-radius: 3px;
                padding: 5px 10px;
                color: #333333;
            }
            QPushButton:hover {
                background-color: #D0D0D0;
            }
            QPushButton:pressed {
                background-color: #C0C0C0;
            }
            QTableView, QTreeWidget, QTextEdit {
                background-color: #FFFFFF;
                border: 1px solid #CCCCCC;
                border-radius: 2px;
                color: #333333;
            }
            QHeaderView::section {
                background-color: #E8E8E8;
                color: #333333;
                padding: 4px;
                border: 1px solid #CCCCCC;
            }
            QSplitter::handle {
                background-color: #E0E0E0;
            }
        """)
        
        # 创建工具栏
        tool_bar_layout = QHBoxLayout()
        
        # 添加协议按钮
        add_protocol_button = QPushButton("添加协议")
        if self.packet_sender_controller:
            add_protocol_button.clicked.connect(self.packet_sender_controller._add_protocol)
        tool_bar_layout.addWidget(add_protocol_button)
        
        # 打开按钮
        open_button = QPushButton("打开")
        tool_bar_layout.addWidget(open_button)
        
        # 弹性空间
        tool_bar_layout.addStretch()
        
        # 折叠/展开按钮
        collapse_button = QPushButton("折叠")
        expand_button = QPushButton("展开")
        tool_bar_layout.addWidget(collapse_button)
        tool_bar_layout.addWidget(expand_button)
        
        main_layout.addLayout(tool_bar_layout)
        
        # 创建数据包表格部分
        data_packet_layout = QVBoxLayout()
        
        # 数据包标题和计数布局
        data_packet_header = QHBoxLayout()
        data_packet_label = QLabel("数据包")
        data_packet_header.addWidget(data_packet_label)
        
        data_packet_header.addStretch()
        
        # 添加数据包计数标签
        packet_count_label = QLabel("共 1 个数据包")
        packet_count_label.setStyleSheet("color: #666666; font-weight: normal;")
        data_packet_header.addWidget(packet_count_label)
        
        data_packet_layout.addLayout(data_packet_header)
        
        # 数据包表格
        packet_table = QTableView()
        packet_model = QStandardItemModel()
        packet_model.setHorizontalHeaderLabels(["#", "时间", "源地址", "长度", "协议"])
        
        # 添加示例数据
        row_items = [
            QStandardItem("1"), 
            QStandardItem("00:11:22:33:44:55"), 
            QStandardItem("ff:ff:ff:ff:ff:ff"),
            QStandardItem("64"),
            QStandardItem("Ethernet")
        ]
        packet_model.appendRow(row_items)
        
        packet_table.setModel(packet_model)
        packet_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        data_packet_layout.addWidget(packet_table)
        
        # 创建协议详情和Hex视图部分
        detail_hex_splitter = QSplitter(Qt.Orientation.Horizontal)
        
        # 详情部分
        detail_widget = QWidget()
        detail_layout = QVBoxLayout(detail_widget)
        detail_label = QLabel("详情")
        detail_layout.addWidget(detail_label)
        
        # 创建详情树
        detail_tree = QTreeWidget()
        detail_tree.setHeaderLabels(["属性", "值"])
        
        # 添加示例数据
        ethernet_item = QTreeWidgetItem(["Ethernet"])
        source_mac = QTreeWidgetItem(ethernet_item, ["源MAC地址", "值0"])
        field1 = QTreeWidgetItem(ethernet_item, ["字段1", "值1"])
        field2 = QTreeWidgetItem(ethernet_item, ["字段2", "值2"])
        detail_tree.addTopLevelItem(ethernet_item)
        ethernet_item.setExpanded(True)
        
        detail_layout.addWidget(detail_tree)
        
        # Hex视图部分
        hex_widget = QWidget()
        hex_layout = QVBoxLayout(hex_widget)
        
        # Hex标题和按钮布局
        hex_header = QHBoxLayout()
        hex_label = QLabel("Hex视图")
        hex_header.addWidget(hex_label)
        
        hex_header.addStretch()
        
        # 添加显示按钮
        show_button = QPushButton("显示")
        hex_header.addWidget(show_button)
        
        hex_layout.addLayout(hex_header)
        
        # 创建Hex编辑器
        hex_edit = QTextEdit()
        hex_text = """00 11 22 33 44 55 FF FF FF FF FF FF 08
00 28 00 01 00 00 40 11 7C CD 7F 00 00
00 01 04 00 04 00 00 14 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00"""
        hex_edit.setText(hex_text)
        
        # 设置等宽字体
        font = QFont("monospace")
        font.setPointSize(10)
        hex_edit.setFont(font)
        
        # 额外的Hex视图样式
        hex_edit.setStyleSheet("""
            QTextEdit {
                background-color: #FFFFFF;
                color: #222222;
                border: 1px solid #CCCCCC;
                padding: 4px;
                font-family: monospace;
            }
        """)
        
        hex_layout.addWidget(hex_edit)
        
        # 添加到水平分割器
        detail_hex_splitter.addWidget(detail_widget)
        detail_hex_splitter.addWidget(hex_widget)
        
        # 创建主分割器
        main_splitter = QSplitter(Qt.Orientation.Vertical)
        
        # 创建数据包容器
        data_packet_widget = QWidget()
        data_packet_widget.setLayout(data_packet_layout)
        
        # 添加到主分割器
        main_splitter.addWidget(data_packet_widget)
        main_splitter.addWidget(detail_hex_splitter)
        
        # 设置分割器初始大小
        main_splitter.setSizes([100, 300])
        
        # 添加到主布局
        main_layout.addWidget(main_splitter)
        
        # 添加底部按钮
        button_layout = QHBoxLayout()
        button_layout.addStretch()
        
        send_button = QPushButton("发送")
        send_button.setStyleSheet("""
            QPushButton {
                background-color: #4285F4;
                color: white;
                border: none;
                border-radius: 3px;
                padding: 6px 15px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #3275E4;
            }
            QPushButton:pressed {
                background-color: #2265D4;
            }
        """)
        if self.packet_sender_controller:
            send_button.clicked.connect(self.packet_sender_controller._send_packet)
        button_layout.addWidget(send_button)
        
        main_layout.addLayout(button_layout)
        
        # 连接折叠/展开按钮
        collapse_button.clicked.connect(lambda: detail_tree.collapseAll())
        expand_button.clicked.connect(lambda: detail_tree.expandAll())
        
        # 保存组件引用
        self.detail_tree = detail_tree

    def show_packet_sender(self) -> None:
        """显示发包工具窗口"""
        if not self.packet_sender_window:
            self.packet_sender_window = PacketSenderWindow(self, self.packet_sender_controller)
            
        # 显示发包工具窗口
        self.packet_sender_window.show()
        
        # 将窗口提升到前面
        self.packet_sender_window.raise_()
        self.packet_sender_window.activateWindow()


class PkjvizMainWindow(QMainWindow):
    """Pkjviz主窗口类"""

    def __init__(self) -> None:
        super().__init__()

        # 应用模式
        self.app_mode = MODE_OFFLINE

        # 发包工具窗口
        self.packet_sender_window = None

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
        
        # 登录控制器
        self.login_controller = LoginController(self)

    def init_ui(self) -> None:
        """初始化UI组件"""
        # 设置文件浏览器
        self.file_model = QFileSystemModel()
        self.file_model.setRootPath(QDir.homePath())
        file_explorer = self.ui.findChild(QTreeView, "fileExplorerTreeView")
        if file_explorer:
            file_explorer.setModel(self.file_model)
            file_explorer.setRootIndex(
                self.file_model.index(QDir.homePath())
            )

            # 只显示文件名列
            for i in range(1, self.file_model.columnCount()):
                file_explorer.hideColumn(i)

        # 初始化其他UI组件
        code_editor = self.ui.findChild(QTextEdit, "codeEditor")
        if code_editor:
            code_editor.setPlaceholderText("# 在这里输入Python代码")

        # 设置数据包捕获模型
        packet_capture_view = self.ui.findChild(QTableView, "packetCaptureTableView")
        if packet_capture_view:
            packet_capture_view.setModel(self.packet_model)

        # 添加寄存器编辑器
        register_editor_tab = self.ui.findChild(QWidget, "registerEditorTab")
        if register_editor_tab:
            register_editor = RegisterEditor(register_editor_tab)
            layout = QVBoxLayout(register_editor_tab)
            layout.setContentsMargins(0, 0, 0, 0)
            layout.addWidget(register_editor)
            register_editor_tab.setLayout(layout)

        # 确保设备相关组件默认隐藏（离线模式）
        device_list_widget = self.ui.findChild(QWidget, "deviceListWidget")
        device_list_view = self.ui.findChild(QListWidget, "deviceListView")
        device_tools_widget = self.ui.findChild(QWidget, "deviceToolsWidget")
        selected_device_label = self.ui.findChild(QLabel, "selectedDeviceLabel")
        device_list_label = self.ui.findChild(QLabel, "deviceListLabel")

        if device_list_widget:
            device_list_widget.setVisible(False)
        if device_list_view:
            device_list_view.setVisible(False)
        if device_tools_widget:
            device_tools_widget.setVisible(False)
        if selected_device_label:
            selected_device_label.setVisible(False)
        if device_list_label:
            device_list_label.setVisible(False)

        # 初始状态为离线模式
        self.set_app_mode(MODE_OFFLINE)

    def connect_signals(self) -> None:
        """连接信号和槽"""
        # 查找按钮
        new_button = self.ui.findChild(QPushButton, "newButton")
        open_button = self.ui.findChild(QPushButton, "openButton")
        save_button = self.ui.findChild(QPushButton, "saveButton")
        run_button = self.ui.findChild(QPushButton, "runButton")
        stop_button = self.ui.findChild(QPushButton, "stopButton")
        offline_button = self.ui.findChild(QPushButton, "offlineButton")
        online_button = self.ui.findChild(QPushButton, "onlineButton")
        display_button = self.ui.findChild(QPushButton, "displayButton")
        refresh_button = self.ui.findChild(QPushButton, "refreshButton")
        send_packet_button = self.ui.findChild(QPushButton, "sendPacketButton")
        packet_tool_button = self.ui.findChild(QPushButton, "packetToolButton")
        register_editor_button = self.ui.findChild(QPushButton, "registerEditorButton")
        
        # 查找其他组件
        env_combo_box = self.ui.findChild(QComboBox, "envComboBox")
        file_explorer_tree_view = self.ui.findChild(QTreeView, "fileExplorerTreeView")
        device_list_view = self.ui.findChild(QListWidget, "deviceListView")
        
        # 按钮事件
        if new_button:
            new_button.clicked.connect(self.new_file)
        if open_button:
            open_button.clicked.connect(self.open_file)
        if save_button:
            save_button.clicked.connect(self.save_file)
        if run_button:
            run_button.clicked.connect(self.run_code)
        if stop_button:
            stop_button.clicked.connect(self.stop_execution)

        # 在线/离线模式切换
        if offline_button:
            offline_button.clicked.connect(lambda: self.set_app_mode(MODE_OFFLINE))
        if online_button:
            online_button.clicked.connect(lambda: self.set_app_mode(MODE_ONLINE))
        if display_button:
            display_button.clicked.connect(lambda: self.set_app_mode(MODE_DEMO))

        # 环境选择事件
        if env_combo_box:
            env_combo_box.currentIndexChanged.connect(self.environment_changed)

        # 文件浏览器事件
        if file_explorer_tree_view:
            file_explorer_tree_view.doubleClicked.connect(self.open_selected_file)

        # 设备管理事件
        if refresh_button:
            refresh_button.clicked.connect(self.refresh_devices)
        if send_packet_button:
            send_packet_button.clicked.connect(self.send_packet)
        if device_list_view:
            device_list_view.itemDoubleClicked.connect(self.device_double_clicked)
            
        # 发包工具按钮
        if packet_tool_button:
            packet_tool_button.clicked.connect(self.show_packet_sender)
            
        # 寄存器编辑器按钮
        if register_editor_button:
            register_editor_button.clicked.connect(self.show_register_editor)
            
    def set_app_mode(self, mode: int) -> None:
        """设置应用模式

        Args:
            mode: 应用模式，MODE_OFFLINE、MODE_ONLINE或MODE_DEMO
        """
        self.app_mode = mode

        # 查找UI组件
        device_list_widget = self.ui.findChild(QWidget, "deviceListWidget")
        device_list_view = self.ui.findChild(QListWidget, "deviceListView")
        device_tools_widget = self.ui.findChild(QWidget, "deviceToolsWidget")
        selected_device_label = self.ui.findChild(QLabel, "selectedDeviceLabel")
        device_list_label = self.ui.findChild(QLabel, "deviceListLabel")
        log_widget = self.ui.findChild(QWidget, "logWidget")
        data_browser_widget = self.ui.findChild(QWidget, "dataBrowserWidget")
        data_browser_label = self.ui.findChild(QLabel, "dataBrowserLabel")
        offline_button = self.ui.findChild(QPushButton, "offlineButton")
        online_button = self.ui.findChild(QPushButton, "onlineButton")
        display_button = self.ui.findChild(QPushButton, "displayButton")
        packet_tool_button = self.ui.findChild(QPushButton, "packetToolButton")
        register_editor_button = self.ui.findChild(QPushButton, "registerEditorButton")

        # 重置所有模式按钮状态
        if offline_button:
            offline_button.setEnabled(True)
        if online_button:
            online_button.setEnabled(True)
        if display_button:
            display_button.setEnabled(True)
            
        # 让发包工具按钮在所有模式下都显示
        if packet_tool_button:
            packet_tool_button.setVisible(True)
            # 默认设置为不可点击
            packet_tool_button.setEnabled(False)
            
        # 让寄存器编辑器按钮在所有模式下都显示
        if register_editor_button:
            register_editor_button.setVisible(True)
            # 默认设置为可点击
            register_editor_button.setEnabled(True)

        if mode == MODE_OFFLINE:
            # 离线模式
            self.log_message("切换到离线模式")
            # 隐藏设备相关组件
            if device_list_widget:
                device_list_widget.setVisible(False)
            if device_list_view:
                device_list_view.setVisible(False)
            if device_tools_widget:
                device_tools_widget.setVisible(False)
            if selected_device_label:
                selected_device_label.setVisible(False)
            if device_list_label:
                device_list_label.setVisible(False)

            # 显示Log编辑器
            if log_widget:
                log_widget.setVisible(True)

            # 设置数据浏览器
            if data_browser_widget:
                data_browser_widget.setVisible(True)
            if data_browser_label:
                data_browser_label.setVisible(True)
                data_browser_label.setText("寄存器数据编辑器")

            # 设置对应按钮状态
            if offline_button:
                offline_button.setEnabled(False)
            
            # 在离线模式下发包工具按钮不可点击
            if packet_tool_button:
                packet_tool_button.setEnabled(False)
            
            # 在离线模式下寄存器编辑器按钮可点击
            if register_editor_button:
                register_editor_button.setEnabled(True)
            
            # 隐藏发包工具
            if hasattr(self, "packet_sender_window") and self.packet_sender_window:
                self.packet_sender_window.hide()
                
        elif mode == MODE_ONLINE:
            # 在线模式
            self.log_message("切换到在线模式")
            # 显示设备相关组件
            if device_list_widget:
                device_list_widget.setVisible(True)
            if device_list_view:
                device_list_view.setVisible(True)
            if device_tools_widget:
                device_tools_widget.setVisible(True)
            if selected_device_label:
                selected_device_label.setVisible(True)
            if device_list_label:
                device_list_label.setVisible(True)

            # 隐藏Log编辑器
            if log_widget:
                log_widget.setVisible(False)

            # 在在线模式下不显示数据包捕获
            if data_browser_widget:
                data_browser_widget.setVisible(False)
            if data_browser_label:
                data_browser_label.setVisible(False)
                
            # 显示发包工具按钮并设置为可点击
            if packet_tool_button:
                packet_tool_button.setEnabled(True)
            
            # 设置对应按钮状态
            if online_button:
                online_button.setEnabled(False)
                
        elif mode == MODE_DEMO:
            # 演示模式
            self.log_message("切换到演示模式")
            # 隐藏设备相关组件
            if device_list_widget:
                device_list_widget.setVisible(False)
            if device_list_view:
                device_list_view.setVisible(False)
            if device_tools_widget:
                device_tools_widget.setVisible(False)
            if selected_device_label:
                selected_device_label.setVisible(False)
            if device_list_label:
                device_list_label.setVisible(False)

            # 隐藏Log编辑器
            if log_widget:
                log_widget.setVisible(False)

            # 设置数据浏览器
            if data_browser_widget:
                data_browser_widget.setVisible(True)
            if data_browser_label:
                data_browser_label.setVisible(True)
                data_browser_label.setText("模拟数据")

            # 设置按钮状态
            if display_button:
                display_button.setEnabled(False)
            
            # 在演示模式下发包工具按钮不可点击
            if packet_tool_button:
                packet_tool_button.setEnabled(False)
            
            # 在演示模式下寄存器编辑器按钮不可点击
            if register_editor_button:
                register_editor_button.setEnabled(False)
            
            # 隐藏发包工具
            if hasattr(self, "packet_sender_window") and self.packet_sender_window:
                self.packet_sender_window.hide()

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
        """发送数据包
        
        在线模式下，聚焦到编辑区下方的发包工具
        离线模式下，打开发包工具对话框
        """
        # 如果是离线模式或演示模式，不执行操作
        if self.app_mode == MODE_OFFLINE or self.app_mode == MODE_DEMO:
            self.log_message("当前模式不支持连接设备")
            return
        
        # 获取当前选中的设备
        selected_device = None
        device_list_view = self.ui.findChild(QListWidget, "deviceListView")
        if device_list_view and device_list_view.currentItem():
            selected_device = device_list_view.currentItem().data(Qt.UserRole)
            
            # 弹出登录窗口
            if selected_device:
                self.log_message(f"正在连接设备: {selected_device}...")
                login_success = self.login_controller.show_login_dialog(selected_device)
                if login_success:
                    self.log_message(f"成功连接到设备: {selected_device}")
                    # 设置选中设备标签
                    selected_device_label = self.ui.findChild(QLabel, "selectedDeviceLabel")
                    if selected_device_label:
                        selected_device_label.setText(f"当前设备: {selected_device}")
                    
                    # 在线模式下，显示发包工具
                    if self.app_mode == MODE_ONLINE:
                        if not hasattr(self.ui, "packetSenderWidget"):
                            self._create_packet_sender_widget()
                        else:
                            self.ui.packetSenderWidget.setVisible(True)
                else:
                    self.log_message(f"连接设备失败: {selected_device}")
                    return
            else:
                self.log_message("设备信息无效")
                return
        else:
            self.log_message("请先选择要连接的设备")
            return

    def device_double_clicked(self, item: QListWidgetItem) -> None:
        """设备双击事件"""
        # 如果是离线模式或演示模式，不执行操作
        if self.app_mode == MODE_OFFLINE or self.app_mode == MODE_DEMO:
            return

        # 获取设备对象
        device = item.data(Qt.UserRole)
        if device:
            self.log_message(f"正在连接设备: {device}...")
            # 弹出登录窗口
            login_success = self.login_controller.show_login_dialog(device)
            if login_success:
                self.log_message(f"成功连接到设备: {device}")
                # 设置选中设备标签
                selected_device_label = self.ui.findChild(QLabel, "selectedDeviceLabel")
                if selected_device_label:
                    selected_device_label.setText(f"当前设备: {device}")
                
                # 在线模式下，显示发包工具
                if self.app_mode == MODE_ONLINE:
                    if not hasattr(self.ui, "packetSenderWidget"):
                        self._create_packet_sender_widget()
                    else:
                        self.ui.packetSenderWidget.setVisible(True)
            else:
                self.log_message(f"连接设备失败: {device}")

    def log_message(self, message: str) -> None:
        """在控制台输出日志
        
        Args:
            message: 日志消息
        """
        import datetime
        time_str = datetime.datetime.now().strftime("[%H:%M:%S]")
        self.ui.consoleTextEdit.append(f"{time_str} {message}")

    def show_packet_sender(self) -> None:
        """显示发包工具窗口"""
        if not self.packet_sender_window:
            self.packet_sender_window = PacketSenderWindow(self, self.packet_sender_controller)
            
        # 显示发包工具窗口
        self.packet_sender_window.show()
        
        # 将窗口提升到前面
        self.packet_sender_window.raise_()
        self.packet_sender_window.activateWindow()

    def show_register_editor(self) -> None:
        """显示寄存器编辑器"""
        # 找到寄存器编辑器标签页
        editor_tab_widget = self.ui.findChild(QTabWidget, "editorTabWidget")
        register_editor_tab = self.ui.findChild(QWidget, "registerEditorTab")
        
        if editor_tab_widget and register_editor_tab:
            # 寻找寄存器编辑器的索引
            for i in range(editor_tab_widget.count()):
                if editor_tab_widget.widget(i) == register_editor_tab:
                    # 激活寄存器编辑器标签页
                    editor_tab_widget.setCurrentIndex(i)
                    break
            
        self.log_message("打开寄存器编辑器")


def main() -> None:
    """主函数"""
    app = QApplication(sys.argv)
    window = PkjvizMainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
