#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PySide6.QtWidgets import QDialog, QMessageBox, QLineEdit, QLabel, QPushButton
from PySide6.QtCore import Qt, QFile, QIODevice
from PySide6.QtUiTools import QUiLoader
import os

class LoginController:
    """设备登录控制器"""
    
    def __init__(self, main_window):
        """初始化
        
        Args:
            main_window: 主窗口对象
        """
        self.main_window = main_window
        self.dialog = None
        
        # 查找UI文件
        self.ui_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 
                                    'ui', 'login_dialog.ui')
    
    def show_login_dialog(self, device):
        """显示登录对话框
        
        Args:
            device: 设备对象
        
        Returns:
            bool: 是否登录成功
        """
        # 加载UI文件
        ui_file = QFile(self.ui_path)
        if not ui_file.open(QFile.ReadOnly):
            self.main_window.log_message(f"无法打开UI文件: {self.ui_path}")
            return False
        
        # 创建UI加载器
        loader = QUiLoader()
        
        # 直接加载UI文件到一个新的对话框
        dialog = loader.load(ui_file, self.main_window)
        ui_file.close()
        
        if not dialog:
            self.main_window.log_message("无法加载登录对话框UI文件")
            return False
        
        # 保存对话框引用
        self.dialog = dialog
        
        # 设置设备信息
        device_label = self.dialog.findChild(QLabel, "deviceLabel")
        if device_label and hasattr(device, 'name') and hasattr(device, 'ip_address'):
            device_label.setText(f"设备：{device.name} ({device.ip_address})")
        
        # 获取UI元素
        username_edit = self.dialog.findChild(QLineEdit, "usernameEdit")
        password_edit = self.dialog.findChild(QLineEdit, "passwordEdit")
        login_button = self.dialog.findChild(QPushButton, "loginButton")
        cancel_button = self.dialog.findChild(QPushButton, "cancelButton")
        
        # 连接信号
        if login_button:
            login_button.clicked.connect(lambda: self._verify_login(device))
        if cancel_button:
            cancel_button.clicked.connect(self.dialog.reject)
        
        # 设置默认焦点到用户名输入框
        if username_edit:
            username_edit.setFocus()
        
        # 显示对话框并获取结果
        result = self.dialog.exec()
        
        # 返回登录结果
        return result == QDialog.Accepted
    
    def _verify_login(self, device):
        """验证登录信息
        
        Args:
            device: 设备对象
        """
        # 获取用户名和密码
        username_edit = self.dialog.findChild(QLineEdit, "usernameEdit")
        password_edit = self.dialog.findChild(QLineEdit, "passwordEdit")
        
        if not username_edit or not password_edit:
            return
        
        username = username_edit.text().strip()
        password = password_edit.text()
        
        # 验证用户名和密码不能为空
        if not username or not password:
            QMessageBox.warning(self.dialog, "登录失败", "用户名和密码不能为空！")
            return
        
        # 模拟验证过程，实际应用中应该与后端服务交互验证
        # 这里仅作为示例，任何非空用户名密码都能登录成功
        self.main_window.log_message(f"验证设备 {device} 的登录信息: 用户名={username}")
        
        # 模拟登录成功
        if device:
            device.status = device.STATUS_ONLINE  # 设置设备状态为在线
            self.main_window.log_message(f"登录成功: {username}@{device}")
            self.dialog.accept()  # 关闭对话框并返回接受结果
        else:
            QMessageBox.critical(self.dialog, "登录失败", "设备信息无效！") 