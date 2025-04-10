"""
模式切换控件
"""

# 标准库导入
import os
import sys

# 第三方库导入
from qtpy.QtCore import Qt, Signal, QSize
from qtpy.QtGui import QIcon, QColor, QPalette
from qtpy.QtWidgets import (
    QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QButtonGroup,
    QLabel, QFrame
)

class ModeSwitchButton(QPushButton):
    """模式切换按钮."""
    
    def __init__(self, text, icon=None, parent=None):
        """初始化模式切换按钮."""
        QPushButton.__init__(self, text, parent)
        
        if icon:
            self.setIcon(QIcon(icon))
        
        # 设置样式
        self.setCheckable(True)
        self.setFlat(True)
        self.setFixedHeight(30)
        self.setMinimumWidth(80)
        
        # 设置样式表
        self.setStyleSheet("""
            ModeSwitchButton {
                border-radius: 3px;
                border: 1px solid transparent;
                padding: 4px 8px;
                color: #cccccc;
                background-color: transparent;
                text-align: center;
            }
            ModeSwitchButton:hover {
                background-color: #3a3d3e;
            }
            ModeSwitchButton:checked {
                background-color: #0e639c;
                border: 1px solid #1177bb;
                color: white;
            }
        """)


class ModeSwitch(QWidget):
    """模式切换组件."""
    
    OFFLINE_MODE = 0
    ONLINE_MODE = 1
    DEMO_MODE = 2
    
    sig_mode_changed = Signal(int)  # 模式变更信号
    
    def __init__(self, parent=None):
        """初始化模式切换组件."""
        QWidget.__init__(self, parent)
        
        # 设置背景
        self.setAutoFillBackground(True)
        pal = self.palette()
        pal.setColor(QPalette.Window, QColor("#252526"))
        self.setPalette(pal)
        
        # 创建布局
        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(5, 5, 5, 5)
        self.layout.setSpacing(10)
        
        # 添加模式标签
        self.mode_label = QLabel("模式:", self)
        self.mode_label.setStyleSheet("color: #cccccc;")
        self.layout.addWidget(self.mode_label)
        
        # 创建模式切换按钮
        self.button_group = QButtonGroup(self)
        self.button_group.setExclusive(True)
        self.button_group.idClicked.connect(self.on_mode_button_clicked)
        
        # 离线模式按钮
        self.offline_button = ModeSwitchButton("离线", None, self)
        self.button_group.addButton(self.offline_button, self.OFFLINE_MODE)
        self.layout.addWidget(self.offline_button)
        
        # 添加分隔符
        self.separator1 = QFrame(self)
        self.separator1.setFrameShape(QFrame.VLine)
        self.separator1.setFrameShadow(QFrame.Sunken)
        self.separator1.setStyleSheet("color: #444444;")
        self.layout.addWidget(self.separator1)
        
        # 在线模式按钮
        self.online_button = ModeSwitchButton("在线", None, self)
        self.button_group.addButton(self.online_button, self.ONLINE_MODE)
        self.layout.addWidget(self.online_button)
        
        # 添加分隔符
        self.separator2 = QFrame(self)
        self.separator2.setFrameShape(QFrame.VLine)
        self.separator2.setFrameShadow(QFrame.Sunken)
        self.separator2.setStyleSheet("color: #444444;")
        self.layout.addWidget(self.separator2)
        
        # 演示模式按钮
        self.demo_button = ModeSwitchButton("演示", None, self)
        self.button_group.addButton(self.demo_button, self.DEMO_MODE)
        self.layout.addWidget(self.demo_button)
        
        # 布局扩展
        self.layout.addStretch()
        
        # 设置默认模式
        self.set_mode(self.OFFLINE_MODE)
        
    def set_mode(self, mode):
        """设置当前模式."""
        if mode == self.OFFLINE_MODE:
            self.offline_button.setChecked(True)
        elif mode == self.ONLINE_MODE:
            self.online_button.setChecked(True)
        elif mode == self.DEMO_MODE:
            self.demo_button.setChecked(True)
        
        # 触发模式变化信号
        self.sig_mode_changed.emit(mode)
        
    def get_mode(self):
        """获取当前模式."""
        if self.offline_button.isChecked():
            return self.OFFLINE_MODE
        elif self.online_button.isChecked():
            return self.ONLINE_MODE
        elif self.demo_button.isChecked():
            return self.DEMO_MODE
        return self.OFFLINE_MODE
        
    def on_mode_button_clicked(self, id):
        """模式按钮点击处理."""
        self.sig_mode_changed.emit(id) 