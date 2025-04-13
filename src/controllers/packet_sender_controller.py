#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PySide6.QtWidgets import QDialog
from PySide6.QtCore import Qt
from PySide6.QtGui import QStandardItemModel, QStandardItem, QIcon
from PySide6.QtUiTools import QUiLoader
import os
from PySide6.QtCore import QFile, QIODevice

class PacketSenderController:
    """数据包发送控制器"""
    
    def __init__(self, main_window):
        """初始化
        
        Args:
            main_window: 主窗口对象
        """
        self.main_window = main_window
        self.dialog = None
        self.ui = None
        
        # 查找UI文件
        self.ui_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 
                                    'ui', 'packet_sender.ui')
    
    def show_dialog(self, selected_device=None):
        """显示数据包发送对话框
        
        Args:
            selected_device: 选中的设备，可以为None
        """
        # 加载UI文件
        ui_file = QFile(self.ui_path)
        if not ui_file.open(QIODevice.ReadOnly):
            self.main_window.log_message(f"无法打开UI文件: {self.ui_path}")
            return
        
        # 创建UI加载器
        loader = QUiLoader()
        
        # 直接加载UI文件到一个新的对话框
        dialog = loader.load(ui_file, self.main_window)
        ui_file.close()
        
        if not dialog:
            self.main_window.log_message("无法加载UI文件")
            return
        
        # 保存对话框引用
        self.dialog = dialog
        
        # 设置窗口标题
        if selected_device:
            self.dialog.setWindowTitle(f"发包工具 - {selected_device}")
        
        # 获取UI元素
        from PySide6.QtWidgets import QPushButton, QTreeView
        
        # 按钮
        self.addProtocolButton = self.dialog.findChild(QPushButton, "addProtocolButton")
        self.openButton = self.dialog.findChild(QPushButton, "openButton")
        self.collapseButton = self.dialog.findChild(QPushButton, "collapseButton")
        self.expandButton = self.dialog.findChild(QPushButton, "expandButton")
        self.sendButton = self.dialog.findChild(QPushButton, "sendButton")
        self.cancelButton = self.dialog.findChild(QPushButton, "cancelButton")
        
        # TreeView
        self.dataPacketTreeView = self.dialog.findChild(QTreeView, "dataPacketTreeView")
        
        # 连接信号
        self._connect_signals()
        
        # 设置界面
        self._init_ui(selected_device)
        
        # 显示对话框
        self.dialog.exec_()
    
    def _init_ui(self, selected_device):
        """初始化界面
        
        Args:
            selected_device: 选中的设备
        """
        # 检查按钮图标，处理不存在的情况
        from PySide6.QtGui import QIcon
        empty_icon = QIcon()  # 创建空图标
        
        icon_buttons = [
            self.addProtocolButton,
            self.openButton,
            self.collapseButton,
            self.expandButton
        ]
        
        for button in icon_buttons:
            if button is not None:
                button.setIcon(empty_icon)  # 使用空图标代替None
        
        # 确保展开和折叠按钮文本正确
        if self.expandButton is not None:
            self.expandButton.setText("展开")
        
        if self.collapseButton is not None:
            self.collapseButton.setText("折叠")
        
        # 设置数据包树模型
        self._setup_packet_tree()
    
    def _setup_packet_tree(self):
        """设置数据包树"""
        # 确保数据包树视图存在
        if self.dataPacketTreeView is None:
            return
            
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(["数据包"])
        
        # 添加示例数据
        ethernet_item = QStandardItem("Ethernet")
        ethernet_item.setEditable(False)
        
        # 添加子项
        source_mac = QStandardItem("源MAC地址: ff:ff:ff:ff:ff:ff")
        source_mac.setEditable(False)
        dest_mac = QStandardItem("目的MAC地址: 00:11:22:33:44:55")
        dest_mac.setEditable(False)
        type_item = QStandardItem("类型: 0x0800 (IPv4)")
        type_item.setEditable(False)
        
        ethernet_item.appendRow(source_mac)
        ethernet_item.appendRow(dest_mac)
        ethernet_item.appendRow(type_item)
        
        # 添加到模型
        model.appendRow(ethernet_item)
        
        # 设置模型
        self.dataPacketTreeView.setModel(model)
        self.dataPacketTreeView.expandAll()
    
    def _connect_signals(self):
        """连接信号"""
        # 按钮信号
        if self.addProtocolButton is not None:
            self.addProtocolButton.clicked.connect(self._add_protocol)
        
        if self.sendButton is not None:
            self.sendButton.clicked.connect(self._send_packet)
        
        if self.cancelButton is not None:
            self.cancelButton.clicked.connect(self.dialog.reject)
        
        # 折叠/展开按钮
        if self.collapseButton is not None and self.dataPacketTreeView is not None:
            self.collapseButton.clicked.connect(self.dataPacketTreeView.collapseAll)
        
        if self.expandButton is not None and self.dataPacketTreeView is not None:
            self.expandButton.clicked.connect(self.dataPacketTreeView.expandAll)
    
    def _add_protocol(self):
        """添加协议"""
        # 这里只是示例，实际应用中应该显示协议选择对话框
        self.main_window.log_message("添加协议")
    
    def _send_packet(self):
        """发送数据包"""
        # 这里只是示例，实际应用中应该发送真正的数据包
        self.main_window.log_message("发送数据包")
        # 只有当dialog存在时才尝试关闭它
        if self.dialog:
            self.dialog.accept()
    
    def create_protocol_tree_model(self):
        """创建协议树模型
        
        Returns:
            QStandardItemModel: 协议树模型
        """
        from PySide6.QtGui import QStandardItemModel, QStandardItem
        
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(["数据包"])
        
        # 添加示例数据
        ethernet_item = QStandardItem("Ethernet")
        ethernet_item.setEditable(False)
        
        # 添加子项
        source_mac = QStandardItem("源MAC地址: ff:ff:ff:ff:ff:ff")
        source_mac.setEditable(False)
        dest_mac = QStandardItem("目的MAC地址: 00:11:22:33:44:55")
        dest_mac.setEditable(False)
        type_item = QStandardItem("类型: 0x0800 (IPv4)")
        type_item.setEditable(False)
        
        ethernet_item.appendRow(source_mac)
        ethernet_item.appendRow(dest_mac)
        ethernet_item.appendRow(type_item)
        
        # 添加IPv4协议
        ipv4_item = QStandardItem("IPv4")
        ipv4_item.setEditable(False)
        
        # 添加IPv4子项
        version = QStandardItem("版本: 4")
        version.setEditable(False)
        src_ip = QStandardItem("源IP: 192.168.1.1")
        src_ip.setEditable(False)
        dst_ip = QStandardItem("目的IP: 192.168.1.2")
        dst_ip.setEditable(False)
        protocol = QStandardItem("协议: 17 (UDP)")
        protocol.setEditable(False)
        
        ipv4_item.appendRow(version)
        ipv4_item.appendRow(src_ip)
        ipv4_item.appendRow(dst_ip)
        ipv4_item.appendRow(protocol)
        
        # 添加到模型
        model.appendRow(ethernet_item)
        model.appendRow(ipv4_item)
        
        return model 