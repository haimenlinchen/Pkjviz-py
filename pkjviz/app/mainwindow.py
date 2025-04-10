"""
Pkjviz 主窗口模块
"""

# 标准库导入
import os
import sys
import logging

# 第三方库导入
from qtpy.QtCore import Qt, Signal, Slot
from qtpy.QtGui import QKeySequence
from qtpy.QtWidgets import (
    QApplication,
    QMainWindow,
    QMessageBox,
    QTabBar,
    QDockWidget,
    QSplitter,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
    QMenu,
    QAction
)

# 本地导入
from pkjviz.config.main import CONF
from pkjviz.utils.qthelpers import create_action
from pkjviz.widgets.mode_switch import ModeSwitch
from pkjviz.widgets.device_dialog import ConnectionDialog
from pkjviz.widgets.online_tools import OnlineTools

# 设置日志
logger = logging.getLogger(__name__)


class MainWindow(QMainWindow):
    """Pkjviz 主窗口"""

    # 信号
    sig_setup_finished = Signal()

    def __init__(self, splash=None):
        """初始化主窗口."""
        QMainWindow.__init__(self)

        # 设置窗口属性
        self.setWindowTitle("Pkjviz")
        self.resize(1200, 800)

        # 样式信息
        self.default_style = str(QApplication.instance().style().objectName())

        # 当前模式
        self.current_mode = ModeSwitch.OFFLINE_MODE

        # 当前连接的设备
        self.current_device_id = None
        self.current_device_name = None

        # 创建状态栏
        status = self.statusBar()
        status.setVisible(True)
        status.showMessage("就绪", 5000)

        # 设置中心部件
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.central_layout = QVBoxLayout()
        self.central_layout.setContentsMargins(0, 0, 0, 0)
        self.central_layout.setSpacing(0)
        self.central_widget.setLayout(self.central_layout)

        # 初始化UI
        self.setup()

    def setup(self):
        """设置界面元素."""
        # 创建菜单栏
        self.create_menus()

        # 创建工具栏
        self.create_toolbars()

        # 创建主界面布局
        self.create_main_layout()

        # 创建侧边栏
        self.create_sidebar()

        # 创建主要内容区域
        self.create_content_area()

        # 创建模式切换区域
        self.create_mode_toolbar()

        # 创建在线工具面板
        self.create_online_tools()

        # 发出设置完成信号
        self.sig_setup_finished.emit()

    def create_menus(self):
        """创建主菜单."""
        # 文件菜单
        self.file_menu = self.menuBar().addMenu("文件")
        new_file_action = create_action(
            self, "新建文件", shortcut=QKeySequence.New, triggered=self.new_file
        )
        open_file_action = create_action(
            self, "打开文件...", shortcut=QKeySequence.Open, triggered=self.open_file
        )
        save_file_action = create_action(
            self, "保存", shortcut=QKeySequence.Save, triggered=self.save_file
        )

        self.file_menu.addAction(new_file_action)
        self.file_menu.addAction(open_file_action)
        self.file_menu.addAction(save_file_action)
        self.file_menu.addSeparator()

        exit_action = create_action(
            self, "退出", shortcut=QKeySequence.Quit, triggered=self.close
        )
        self.file_menu.addAction(exit_action)

        # 编辑菜单
        self.edit_menu = self.menuBar().addMenu("编辑")

        # 设备菜单
        self.device_menu = self.menuBar().addMenu("设备")

        connect_action = create_action(
            self, "连接设备...", triggered=self.connect_device
        )
        self.device_menu.addAction(connect_action)

        disconnect_action = create_action(
            self, "断开连接", triggered=self.disconnect_device
        )
        self.device_menu.addAction(disconnect_action)

        # 视图菜单
        self.view_menu = self.menuBar().addMenu("视图")

        # 运行菜单
        self.run_menu = self.menuBar().addMenu("运行")

        # 终端菜单
        self.terminal_menu = self.menuBar().addMenu("终端")

        # 帮助菜单
        self.help_menu = self.menuBar().addMenu("帮助")

    def create_toolbars(self):
        """创建工具栏."""
        self.main_toolbar = self.addToolBar("主工具栏")
        self.main_toolbar.setObjectName("MainToolBar")

    def create_main_layout(self):
        """创建主界面布局."""
        # 创建主分割器
        self.main_splitter = QSplitter(Qt.Horizontal)
        self.central_layout.addWidget(self.main_splitter)

    def create_sidebar(self):
        """创建侧边栏."""
        self.sidebar = QWidget()
        self.sidebar.setMinimumWidth(200)
        self.sidebar.setMaximumWidth(300)
        self.sidebar_layout = QVBoxLayout()
        self.sidebar_layout.setContentsMargins(0, 0, 0, 0)
        self.sidebar_layout.setSpacing(0)
        self.sidebar.setLayout(self.sidebar_layout)

        # 添加到主分割器
        self.main_splitter.addWidget(self.sidebar)

    def create_content_area(self):
        """创建主要内容区域."""
        self.content_area = QWidget()
        self.content_layout = QVBoxLayout()
        self.content_layout.setContentsMargins(0, 0, 0, 0)
        self.content_layout.setSpacing(0)
        self.content_area.setLayout(self.content_layout)

        # 添加到主分割器
        self.main_splitter.addWidget(self.content_area)

        # 设置分割比例
        self.main_splitter.setSizes([1, 3])

    def create_mode_toolbar(self):
        """创建模式切换工具栏."""
        self.mode_switch = ModeSwitch(self)
        self.mode_switch.sig_mode_changed.connect(self.on_mode_changed)
        self.content_layout.addWidget(self.mode_switch)

    def create_online_tools(self):
        """创建在线工具面板."""
        self.online_tools = OnlineTools(self)
        self.content_layout.addWidget(self.online_tools)

        # 默认开始时在线工具不可见
        self.online_tools.setVisible(False)

    def on_mode_changed(self, mode):
        """模式变更处理."""
        self.current_mode = mode

        # 根据模式更新UI
        if mode == ModeSwitch.OFFLINE_MODE:
            self.statusBar().showMessage("离线模式", 5000)
            self.online_tools.setVisible(False)
        elif mode == ModeSwitch.ONLINE_MODE:
            self.statusBar().showMessage("在线模式", 5000)

            # 如果没有连接设备，则提示连接
            if not self.current_device_id:
                reply = QMessageBox.question(
                    self, "连接设备", "在线模式需要连接到设备。是否现在连接?",
                    QMessageBox.Yes | QMessageBox.No,
                    QMessageBox.Yes
                )

                if reply == QMessageBox.Yes:
                    self.connect_device()

            # 显示在线工具
            self.online_tools.setVisible(True)
        elif mode == ModeSwitch.DEMO_MODE:
            self.statusBar().showMessage("演示模式", 5000)
            self.online_tools.setVisible(True)

            # 演示模式下, 使用一个假设备
            self.current_device_id = "demo001"
            self.current_device_name = "演示设备"
            self.statusBar().showMessage(f"已连接到 {self.current_device_name}", 5000)

    def connect_device(self):
        """连接设备."""
        # 显示连接对话框
        dialog = ConnectionDialog(self)
        dialog.sig_connect_device.connect(self.on_device_connected)

        result = dialog.exec_()
        if result == ConnectionDialog.Accepted:
            # 对话框中的连接处理已在信号处理函数中完成
            pass

    def disconnect_device(self):
        """断开设备连接."""
        if self.current_device_id:
            reply = QMessageBox.question(
                self, "断开连接", f"确定要断开与 {self.current_device_name} 的连接吗?",
                QMessageBox.Yes | QMessageBox.No,
                QMessageBox.No
            )

            if reply == QMessageBox.Yes:
                # 断开连接
                self.current_device_id = None
                self.current_device_name = None

                # 如果是在线模式，则切换回离线模式
                if self.current_mode == ModeSwitch.ONLINE_MODE:
                    self.mode_switch.set_mode(ModeSwitch.OFFLINE_MODE)

                self.statusBar().showMessage("已断开连接", 5000)

    @Slot(str, str, str)
    def on_device_connected(self, device_id, username, password):
        """设备连接完成处理."""
        # 在实际应用中，这里应该是真正的连接逻辑
        self.current_device_id = device_id

        # 获取设备名称
        dialog = self.sender()
        if isinstance(dialog, ConnectionDialog):
            self.current_device_name = dialog.get_device_name()

        self.statusBar().showMessage(f"已连接到 {self.current_device_name}", 5000)

        # 如果当前不是在线模式，则切换
        if self.current_mode != ModeSwitch.ONLINE_MODE:
            self.mode_switch.set_mode(ModeSwitch.ONLINE_MODE)

    # ---- 槽函数 ----

    def new_file(self):
        """创建新文件."""
        QMessageBox.information(self, "新建文件", "此功能尚未实现")

    def open_file(self):
        """打开文件."""
        QMessageBox.information(self, "打开文件", "此功能尚未实现")

    def save_file(self):
        """保存文件."""
        QMessageBox.information(self, "保存文件", "此功能尚未实现")

    def closeEvent(self, event):
        """处理窗口关闭事件."""
        reply = QMessageBox.question(
            self, "退出确认", "确定要退出吗?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
