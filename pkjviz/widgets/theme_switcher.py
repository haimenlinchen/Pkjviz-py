"""
主题切换组件
"""

# 标准库导入
import os
import sys
import json

# 第三方库导入
from qtpy.QtCore import Qt, Signal
from qtpy import QtWidgets, QtGui

# 本地导入
from pkjviz.config.main import CONF


class ThemeSwitcher(QtWidgets.QWidget):
    """主题切换组件."""
    
    # 主题常量
    DARK_THEME = "dark"
    LIGHT_THEME = "light"
    
    # 主题变更信号
    sig_theme_changed = Signal(str)  # 主题变更信号(主题名)
    
    def __init__(self, parent=None):
        """初始化主题切换组件."""
        QtWidgets.QWidget.__init__(self, parent)
        
        # 创建布局
        self.layout = QtWidgets.QHBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(5)
        
        # 添加标签
        self.theme_label = QtWidgets.QLabel("主题:", self)
        self.layout.addWidget(self.theme_label)
        
        # 创建主题切换按钮
        self.light_button = QtWidgets.QPushButton("浅色", self)
        self.light_button.setCheckable(True)
        self.light_button.clicked.connect(lambda: self.set_theme(self.LIGHT_THEME))
        self.layout.addWidget(self.light_button)
        
        self.dark_button = QtWidgets.QPushButton("深色", self)
        self.dark_button.setCheckable(True)
        self.dark_button.clicked.connect(lambda: self.set_theme(self.DARK_THEME))
        self.layout.addWidget(self.dark_button)
        
        # 创建按钮组
        self.button_group = QtWidgets.QButtonGroup(self)
        self.button_group.addButton(self.light_button)
        self.button_group.addButton(self.dark_button)
        self.button_group.setExclusive(True)
        
        # 从配置中加载当前主题
        self.current_theme = CONF.get('appearance', 'theme', default=self.DARK_THEME)
        self.update_button_states()
        
        # 应用当前主题
        self.apply_theme(self.current_theme)
        
    def update_button_states(self):
        """更新按钮状态."""
        if self.current_theme == self.LIGHT_THEME:
            self.light_button.setChecked(True)
        else:
            self.dark_button.setChecked(True)
            
    def set_theme(self, theme):
        """设置主题."""
        if theme != self.current_theme:
            self.current_theme = theme
            
            # 保存到配置
            CONF.set('appearance', 'theme', theme)
            
            # 应用主题
            self.apply_theme(theme)
            
            # 发出主题变更信号
            self.sig_theme_changed.emit(theme)
            
    def apply_theme(self, theme):
        """应用主题到应用程序."""
        if theme == self.LIGHT_THEME:
            self.apply_light_theme()
        else:
            self.apply_dark_theme()
            
    def apply_dark_theme(self):
        """应用深色主题."""
        app = QtWidgets.QApplication.instance()
        
        # 使用样式表方式应用深色主题
        app.setStyleSheet("""
            QWidget {
                background-color: #2d2d2d;
                color: #d4d4d4;
            }
            
            QLineEdit, QTextEdit, QPlainTextEdit {
                background-color: #1e1e1e;
                color: #d4d4d4;
                border: 1px solid #3f3f3f;
            }
            
            QPushButton {
                background-color: #353535;
                color: #d4d4d4;
                border: 1px solid #555555;
                padding: 5px;
            }
            
            QPushButton:hover {
                background-color: #454545;
            }
            
            QPushButton:pressed {
                background-color: #2a82da;
            }
            
            QToolTip {
                color: #ffffff;
                background-color: #2d2d2d;
                border: 1px solid #505050;
            }
            
            QSplitter::handle {
                background-color: #505050;
            }
            
            QScrollBar:vertical {
                border: none;
                background: #2d2d2d;
                width: 10px;
                margin: 0px 0px 0px 0px;
            }
            
            QScrollBar::handle:vertical {
                background: #505050;
                min-height: 20px;
                border-radius: 5px;
            }
            
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                height: 0px;
            }
            
            QScrollBar:horizontal {
                border: none;
                background: #2d2d2d;
                height: 10px;
                margin: 0px 0px 0px 0px;
            }
            
            QScrollBar::handle:horizontal {
                background: #505050;
                min-width: 20px;
                border-radius: 5px;
            }
            
            QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {
                width: 0px;
            }
            
            QTabBar::tab {
                background-color: #2d2d2d;
                color: #d4d4d4;
                border: 1px solid #505050;
                padding: 5px 10px;
            }
            
            QTabBar::tab:selected {
                background-color: #3a3a3a;
                border-bottom-color: #2a82da;
            }
            
            QMenu {
                background-color: #2d2d2d;
                color: #d4d4d4;
                border: 1px solid #505050;
            }
            
            QMenu::item:selected {
                background-color: #2a82da;
            }
            
            QHeaderView::section {
                background-color: #353535;
                color: #d4d4d4;
                padding: 5px;
                border: 1px solid #505050;
            }
            
            QTreeView, QListView, QTableView {
                background-color: #1e1e1e;
                alternate-background-color: #262626;
                color: #d4d4d4;
            }
            
            QTreeView::item:selected, QListView::item:selected, QTableView::item:selected {
                background-color: #2a82da;
            }
        """)
        
    def apply_light_theme(self):
        """应用浅色主题."""
        app = QtWidgets.QApplication.instance()
        
        # 使用样式表方式应用浅色主题
        app.setStyleSheet("""
            QWidget {
                background-color: #f0f0f0;
                color: #000000;
            }
            
            QLineEdit, QTextEdit, QPlainTextEdit {
                background-color: #ffffff;
                color: #000000;
                border: 1px solid #c0c0c0;
            }
            
            QPushButton {
                background-color: #e9e9e9;
                color: #000000;
                border: 1px solid #c0c0c0;
                padding: 5px;
            }
            
            QPushButton:hover {
                background-color: #d9d9d9;
            }
            
            QPushButton:pressed {
                background-color: #0078d7;
                color: #ffffff;
            }
            
            QToolTip {
                color: #000000;
                background-color: #f0f0f0;
                border: 1px solid #c0c0c0;
            }
            
            QSplitter::handle {
                background-color: #c0c0c0;
            }
            
            QScrollBar:vertical {
                border: none;
                background: #f0f0f0;
                width: 10px;
                margin: 0px 0px 0px 0px;
            }
            
            QScrollBar::handle:vertical {
                background: #c0c0c0;
                min-height: 20px;
                border-radius: 5px;
            }
            
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                height: 0px;
            }
            
            QScrollBar:horizontal {
                border: none;
                background: #f0f0f0;
                height: 10px;
                margin: 0px 0px 0px 0px;
            }
            
            QScrollBar::handle:horizontal {
                background: #c0c0c0;
                min-width: 20px;
                border-radius: 5px;
            }
            
            QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {
                width: 0px;
            }
            
            QTabBar::tab {
                background-color: #e9e9e9;
                color: #000000;
                border: 1px solid #c0c0c0;
                padding: 5px 10px;
            }
            
            QTabBar::tab:selected {
                background-color: #ffffff;
                border-bottom-color: #0078d7;
            }
            
            QMenu {
                background-color: #ffffff;
                color: #000000;
                border: 1px solid #c0c0c0;
            }
            
            QMenu::item:selected {
                background-color: #0078d7;
                color: #ffffff;
            }
            
            QHeaderView::section {
                background-color: #e9e9e9;
                color: #000000;
                padding: 5px;
                border: 1px solid #c0c0c0;
            }
            
            QTreeView, QListView, QTableView {
                background-color: #ffffff;
                alternate-background-color: #f9f9f9;
                color: #000000;
            }
            
            QTreeView::item:selected, QListView::item:selected, QTableView::item:selected {
                background-color: #0078d7;
                color: #ffffff;
            }
        """)
        
    def get_current_theme(self):
        """获取当前主题."""
        return self.current_theme 