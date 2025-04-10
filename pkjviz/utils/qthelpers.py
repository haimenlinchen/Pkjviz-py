"""
Qt 相关的辅助函数
"""

# 标准库导入
import os
import sys

# 第三方库导入
from qtpy.QtCore import QSize, QObject, Signal, Slot, Qt
from qtpy.QtGui import QIcon, QKeySequence
from qtpy.QtWidgets import QAction


def create_action(parent, text, icon=None, tip=None, shortcut=None,
                triggered=None, toggled=None, data=None,
                register_shortcut=False, context=Qt.WidgetWithChildrenShortcut,
                menurole=None):
    """创建 QAction 对象."""
    from qtpy.QtCore import Qt

    action = QAction(text, parent)
    
    if icon is not None:
        if isinstance(icon, str):
            icon = QIcon(icon)
        action.setIcon(icon)
    
    if tip is not None:
        action.setToolTip(tip)
        action.setStatusTip(tip)
    
    if shortcut is not None:
        action.setShortcut(shortcut)
    
    if triggered is not None:
        action.triggered.connect(triggered)
    
    if toggled is not None:
        action.toggled.connect(toggled)
        action.setCheckable(True)
    
    if data is not None:
        action.setData(data)
    
    if menurole is not None:
        action.setMenuRole(menurole)
    
    return action


def create_toolbutton(parent, text=None, icon=None, tip=None, shortcut=None,
                    triggered=None, toggled=None, auto_raise=True,
                    text_beside_icon=False, text_under_icon=False):
    """创建工具按钮."""
    from qtpy.QtWidgets import QToolButton
    from qtpy.QtCore import Qt
    
    button = QToolButton(parent)
    
    if text is not None:
        button.setText(text)
    
    if icon is not None:
        if isinstance(icon, str):
            icon = QIcon(icon)
        button.setIcon(icon)
    
    if text_beside_icon:
        button.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
    elif text_under_icon:
        button.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
    
    if tip is not None:
        button.setToolTip(tip)
    
    if auto_raise:
        button.setAutoRaise(True)
    
    if triggered is not None:
        button.clicked.connect(triggered)
    
    if toggled is not None:
        button.toggled.connect(toggled)
        button.setCheckable(True)
    
    if shortcut is not None:
        button.setShortcut(shortcut)
    
    return button


def create_plugin_layout(tools_layout):
    """创建标准的插件布局."""
    from qtpy.QtWidgets import QVBoxLayout
    
    layout = QVBoxLayout()
    layout.setContentsMargins(0, 0, 0, 0)
    layout.setSpacing(0)
    layout.addLayout(tools_layout)
    return layout 