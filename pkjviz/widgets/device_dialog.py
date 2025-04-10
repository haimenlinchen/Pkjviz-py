"""
设备连接对话框
"""

# 标准库导入
import os
import sys

# 第三方库导入
from qtpy.QtCore import Qt, Signal, QSize
from qtpy.QtGui import QIcon, QColor
from qtpy.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QGridLayout,
    QLabel, QLineEdit, QPushButton, QListWidget, QListWidgetItem,
    QFrame, QMessageBox, QCheckBox
)

class DeviceListItem(QListWidgetItem):
    """设备列表项."""
    
    def __init__(self, device_name, device_id, device_type, parent=None):
        """初始化设备列表项."""
        QListWidgetItem.__init__(self, parent)
        
        self.device_name = device_name
        self.device_id = device_id
        self.device_type = device_type
        
        # 设置显示文本
        self.setText(device_name)
        
        # 设置提示信息
        self.setToolTip(f"ID: {device_id}\n类型: {device_type}")
        
        # 设置图标 (可以根据设备类型设置不同图标)
        # self.setIcon(QIcon("path/to/icon.png"))
        
        # 设置样式
        # 例如，可以根据设备类型设置不同背景色等


class ConnectionDialog(QDialog):
    """设备连接对话框."""
    
    sig_connect_device = Signal(str, str, str)  # 连接设备信号(设备ID, 用户名, 密码)
    
    def __init__(self, parent=None):
        """初始化设备连接对话框."""
        QDialog.__init__(self, parent)
        
        # 设置窗口属性
        self.setWindowTitle("连接设备")
        self.setMinimumSize(400, 450)
        self.setModal(True)
        
        # 设置样式表
        self.setStyleSheet("""
            ConnectionDialog {
                background-color: #1e1e1e;
                color: #cccccc;
            }
            QLabel {
                color: #cccccc;
            }
            QLineEdit {
                background-color: #252526;
                border: 1px solid #333333;
                border-radius: 3px;
                color: #cccccc;
                padding: 5px;
            }
            QPushButton {
                background-color: #252526;
                border: 1px solid #333333;
                border-radius: 3px;
                color: #cccccc;
                padding: 5px 15px;
            }
            QPushButton:hover {
                background-color: #2a2d2e;
            }
            QPushButton:pressed {
                background-color: #3a3d3e;
            }
            QPushButton#connectButton {
                background-color: #0e639c;
                border: 1px solid #1177bb;
                color: white;
            }
            QPushButton#connectButton:hover {
                background-color: #1177bb;
            }
            QPushButton#connectButton:pressed {
                background-color: #0d5986;
            }
            QListWidget {
                background-color: #252526;
                border: 1px solid #333333;
                border-radius: 3px;
                color: #cccccc;
            }
            QListWidget::item {
                padding: 5px;
                border-bottom: 1px solid #333333;
            }
            QListWidget::item:selected {
                background-color: #0e639c;
                color: white;
            }
            QListWidget::item:hover {
                background-color: #2a2d2e;
            }
            QFrame#separator {
                background-color: #333333;
            }
            QCheckBox {
                color: #cccccc;
            }
            QCheckBox::indicator {
                width: 13px;
                height: 13px;
                border: 1px solid #555555;
                background-color: #252526;
            }
            QCheckBox::indicator:checked {
                background-color: #0e639c;
            }
        """)
        
        # 创建布局
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(20, 20, 20, 20)
        self.layout.setSpacing(15)
        
        # 添加标题
        self.title_label = QLabel("可用设备", self)
        self.title_label.setStyleSheet("font-size: 16px; font-weight: bold;")
        self.layout.addWidget(self.title_label)
        
        # 设备列表
        self.device_list = QListWidget(self)
        self.device_list.setMinimumHeight(200)
        self.device_list.itemClicked.connect(self.on_device_selected)
        self.layout.addWidget(self.device_list)
        
        # 添加几个示例设备
        self.add_sample_devices()
        
        # 添加分隔线
        self.separator = QFrame(self)
        self.separator.setFrameShape(QFrame.HLine)
        self.separator.setFrameShadow(QFrame.Sunken)
        self.separator.setObjectName("separator")
        self.layout.addWidget(self.separator)
        
        # 连接信息表单
        self.form_layout = QGridLayout()
        self.form_layout.setVerticalSpacing(10)
        self.form_layout.setHorizontalSpacing(15)
        
        # 设备名称
        self.device_name_label = QLabel("设备:", self)
        self.form_layout.addWidget(self.device_name_label, 0, 0)
        
        self.device_name_value = QLabel("未选择", self)
        self.form_layout.addWidget(self.device_name_value, 0, 1)
        
        # 用户名
        self.username_label = QLabel("用户名:", self)
        self.form_layout.addWidget(self.username_label, 1, 0)
        
        self.username_field = QLineEdit(self)
        self.username_field.setPlaceholderText("输入用户名")
        self.form_layout.addWidget(self.username_field, 1, 1)
        
        # 密码
        self.password_label = QLabel("密码:", self)
        self.form_layout.addWidget(self.password_label, 2, 0)
        
        self.password_field = QLineEdit(self)
        self.password_field.setPlaceholderText("输入密码")
        self.password_field.setEchoMode(QLineEdit.Password)
        self.form_layout.addWidget(self.password_field, 2, 1)
        
        # 记住密码选项
        self.remember_check = QCheckBox("记住密码", self)
        self.form_layout.addWidget(self.remember_check, 3, 1)
        
        self.layout.addLayout(self.form_layout)
        
        # 按钮布局
        self.button_layout = QHBoxLayout()
        self.button_layout.setSpacing(10)
        
        # 取消按钮
        self.cancel_button = QPushButton("取消", self)
        self.cancel_button.clicked.connect(self.reject)
        self.button_layout.addWidget(self.cancel_button)
        
        # 布局弹性空间
        self.button_layout.addStretch()
        
        # 连接按钮
        self.connect_button = QPushButton("连接", self)
        self.connect_button.setObjectName("connectButton")
        self.connect_button.clicked.connect(self.on_connect)
        self.button_layout.addWidget(self.connect_button)
        
        self.layout.addLayout(self.button_layout)
        
        # 存储当前选中的设备ID
        self.current_device_id = None
        self.current_device_name = None
        
    def add_sample_devices(self):
        """添加示例设备到列表."""
        sample_devices = [
            {"name": "开发板 #1", "id": "dev001", "type": "开发板"},
            {"name": "测试设备 #2", "id": "test002", "type": "测试设备"},
            {"name": "示例设备 #3", "id": "sample003", "type": "演示设备"},
            {"name": "远程设备 #4", "id": "remote004", "type": "远程设备"},
            {"name": "本地设备 #5", "id": "local005", "type": "本地设备"},
        ]
        
        for device in sample_devices:
            item = DeviceListItem(device["name"], device["id"], device["type"])
            self.device_list.addItem(item)
    
    def on_device_selected(self, item):
        """设备选择处理."""
        if isinstance(item, DeviceListItem):
            self.current_device_id = item.device_id
            self.current_device_name = item.device_name
            self.device_name_value.setText(item.device_name)
    
    def on_connect(self):
        """连接按钮点击处理."""
        if not self.current_device_id:
            QMessageBox.warning(self, "警告", "请先选择一个设备")
            return
        
        username = self.username_field.text()
        if not username:
            QMessageBox.warning(self, "警告", "请输入用户名")
            return
        
        password = self.password_field.text()
        if not password:
            QMessageBox.warning(self, "警告", "请输入密码")
            return
        
        # 触发连接信号
        self.sig_connect_device.emit(self.current_device_id, username, password)
        
        # 关闭对话框
        self.accept()
        
    def get_device_name(self):
        """获取当前选中的设备名称."""
        return self.current_device_name 