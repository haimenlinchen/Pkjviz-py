"""
发包工具组件
"""

# 标准库导入
import os
import sys

# 第三方库导入
from qtpy.QtCore import Qt, Signal
from qtpy.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QSplitter,
    QToolBar,
    QLabel,
    QComboBox,
    QLineEdit,
    QPushButton,
    QTextEdit,
    QGroupBox,
    QCheckBox,
    QSpinBox,
)


class PacketSender(QWidget):
    """发包工具组件."""

    sig_packet_sent = Signal(str)

    def __init__(self, parent=None):
        """初始化发包工具."""
        QWidget.__init__(self, parent)

        # 样式设置
        self.setStyleSheet(
            """
            PacketSender {
                background-color: #1e1e1e;
                border-radius: 3px;
                border: 1px solid #333333;
            }
            QGroupBox {
                border: 1px solid #333333;
                border-radius: 3px;
                margin-top: 0.5em;
                padding-top: 0.5em;
                color: #cccccc;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 3px 0 3px;
            }
            QLabel {
                color: #cccccc;
            }
            QComboBox, QLineEdit, QPushButton, QSpinBox {
                background-color: #252526;
                border: 1px solid #333333;
                border-radius: 3px;
                color: #cccccc;
                padding: 3px;
            }
            QComboBox:hover, QLineEdit:hover, QPushButton:hover, QSpinBox:hover {
                background-color: #2a2d2e;
            }
            QPushButton:pressed {
                background-color: #3a3d3e;
            }
            QTextEdit {
                background-color: #1e1e1e;
                border: 1px solid #333333;
                color: #cccccc;
            }
        """
        )

        # 主布局
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(10, 10, 10, 10)
        self.layout.setSpacing(10)

        # 顶部工具栏
        self.toolbar = QToolBar(self)
        self.layout.addWidget(self.toolbar)

        # 协议选择
        protocol_label = QLabel("协议:", self)
        self.toolbar.addWidget(protocol_label)

        self.protocol_combo = QComboBox(self)
        self.protocol_combo.addItems(["TCP", "UDP", "Serial", "Custom"])
        self.toolbar.addWidget(self.protocol_combo)

        self.toolbar.addSeparator()

        # 添加/打开协议按钮
        self.add_protocol_button = QPushButton("添加协议", self)
        self.toolbar.addWidget(self.add_protocol_button)

        self.open_button = QPushButton("打开", self)
        self.toolbar.addWidget(self.open_button)

        # 分割器
        self.splitter = QSplitter(Qt.Vertical, self)
        self.layout.addWidget(self.splitter)

        # 上部分 - 发送配置
        self.send_widget = QWidget(self)
        self.send_layout = QVBoxLayout(self.send_widget)
        self.send_layout.setContentsMargins(0, 0, 0, 0)
        self.splitter.addWidget(self.send_widget)

        # 连接设置
        self.connection_group = QGroupBox("连接设置", self)
        self.send_layout.addWidget(self.connection_group)

        self.connection_layout = QHBoxLayout(self.connection_group)

        # TCP/UDP 设置
        self.host_label = QLabel("主机:", self)
        self.connection_layout.addWidget(self.host_label)

        self.host_edit = QLineEdit("127.0.0.1", self)
        self.connection_layout.addWidget(self.host_edit)

        self.port_label = QLabel("端口:", self)
        self.connection_layout.addWidget(self.port_label)

        self.port_spin = QSpinBox(self)
        self.port_spin.setRange(1, 65535)
        self.port_spin.setValue(502)
        self.connection_layout.addWidget(self.port_spin)

        self.connect_button = QPushButton("连接", self)
        self.connection_layout.addWidget(self.connect_button)

        # 数据设置
        self.data_group = QGroupBox("数据设置", self)
        self.send_layout.addWidget(self.data_group)

        self.data_layout = QVBoxLayout(self.data_group)

        # 数据输入区域
        self.data_edit = QTextEdit(self)
        self.data_layout.addWidget(self.data_edit)

        # 数据格式选项
        self.format_layout = QHBoxLayout()
        self.data_layout.addLayout(self.format_layout)

        self.hex_check = QCheckBox("十六进制", self)
        self.hex_check.setChecked(True)
        self.format_layout.addWidget(self.hex_check)

        self.ascii_check = QCheckBox("ASCII", self)
        self.format_layout.addWidget(self.ascii_check)

        self.format_layout.addStretch()

        self.send_button = QPushButton("发送", self)
        self.format_layout.addWidget(self.send_button)

        # 下部分 - 接收显示
        self.receive_widget = QWidget(self)
        self.receive_layout = QVBoxLayout(self.receive_widget)
        self.receive_layout.setContentsMargins(0, 0, 0, 0)
        self.splitter.addWidget(self.receive_widget)

        # 接收设置
        self.receive_group = QGroupBox("接收数据", self)
        self.receive_layout.addWidget(self.receive_group)

        self.receive_data_layout = QVBoxLayout(self.receive_group)

        # 接收数据显示区域
        self.receive_edit = QTextEdit(self)
        self.receive_edit.setReadOnly(True)
        self.receive_data_layout.addWidget(self.receive_edit)

        # 接收控制
        self.receive_control_layout = QHBoxLayout()
        self.receive_data_layout.addLayout(self.receive_control_layout)

        self.clear_button = QPushButton("清除", self)
        self.receive_control_layout.addWidget(self.clear_button)

        self.receive_control_layout.addStretch()

        self.auto_scroll_check = QCheckBox("自动滚动", self)
        self.auto_scroll_check.setChecked(True)
        self.receive_control_layout.addWidget(self.auto_scroll_check)

        # 设置分割器初始大小
        self.splitter.setSizes([300, 300])

        # 连接信号
        self.connect_button.clicked.connect(self.on_connect)
        self.send_button.clicked.connect(self.on_send)
        self.clear_button.clicked.connect(self.on_clear)
        self.protocol_combo.currentIndexChanged.connect(self.on_protocol_changed)

    def on_connect(self):
        """连接按钮点击处理."""
        host = self.host_edit.text()
        port = self.port_spin.value()

        if self.connect_button.text() == "连接":
            # 连接逻辑
            self.append_receive_text(f"正在连接到 {host}:{port}...", "#8888ff")
            # 模拟连接成功
            self.append_receive_text("连接成功", "#88ff88")
            self.connect_button.setText("断开")
        else:
            # 断开连接逻辑
            self.append_receive_text("断开连接", "#ff8888")
            self.connect_button.setText("连接")

    def on_send(self):
        """发送按钮点击处理."""
        data = self.data_edit.toPlainText()

        if not data:
            self.append_receive_text("错误: 没有要发送的数据", "#ff8888")
            return

        # 发送数据逻辑
        protocol = self.protocol_combo.currentText()
        host = self.host_edit.text()
        port = self.port_spin.value()

        self.append_receive_text(f"发送数据 [{protocol}] -> {host}:{port}", "#88ff88")
        self.append_receive_text(f"数据: {data}", "#ffffff")

        # 发出信号
        self.sig_packet_sent.emit(data)

    def on_clear(self):
        """清除按钮点击处理."""
        self.receive_edit.clear()

    def on_protocol_changed(self, index):
        """协议变更处理."""
        protocol = self.protocol_combo.currentText()
        self.append_receive_text(f"切换到 {protocol} 协议", "#8888ff")

        # 根据协议类型调整界面
        if protocol == "Serial":
            self.host_label.setText("端口:")
            self.host_edit.setText("COM1")
            self.port_label.setText("波特率:")
            self.port_spin.setRange(1200, 115200)
            self.port_spin.setValue(9600)
        else:
            self.host_label.setText("主机:")
            self.host_edit.setText("127.0.0.1")
            self.port_label.setText("端口:")
            self.port_spin.setRange(1, 65535)
            self.port_spin.setValue(502)

    def append_receive_text(self, text, color="#cccccc"):
        """向接收区域添加文本."""
        cursor = self.receive_edit.textCursor()
        cursor.movePosition(cursor.End)

        # 设置颜色
        format = cursor.charFormat()
        format.setForeground(
            Qt.GlobalColor.white
            if color == "#ffffff"
            else (
                Qt.GlobalColor.green
                if color == "#88ff88"
                else Qt.GlobalColor.red if color == "#ff8888" else Qt.GlobalColor.blue
            )
        )
        cursor.setCharFormat(format)

        cursor.insertText(text + "\n")

        # 如果自动滚动，则滚动到底部
        if self.auto_scroll_check.isChecked():
            self.receive_edit.setTextCursor(cursor)
            self.receive_edit.ensureCursorVisible()
