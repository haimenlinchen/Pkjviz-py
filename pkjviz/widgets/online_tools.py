"""
在线工具面板
"""

# 标准库导入
import os
import sys

# 第三方库导入
from qtpy.QtCore import Qt, Signal, QPoint, QSize
from qtpy.QtGui import QIcon, QPalette, QColor, QCursor
from qtpy.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QSplitter,
    QLabel, QPushButton, QToolBar, QFrame, QToolButton,
    QScrollArea
)

# 本地导入
from pkjviz.widgets.splitview import SplitViewManager, ResizeHandle
from pkjviz.widgets.editor import LogEditor, RegisterEditor
from pkjviz.widgets.packet_sender import PacketSender


class CollapsibleButton(QPushButton):
    """可折叠按钮."""
    
    def __init__(self, text, parent=None):
        """初始化折叠按钮."""
        QPushButton.__init__(self, text, parent)
        
        # 设置样式
        self.setFlat(True)
        self.setFixedWidth(16)
        self.setFixedHeight(16)
        
        # 状态
        self._collapsed = False
        
        # 更新图标
        self.update_icon()
    
    def update_icon(self):
        """更新折叠图标."""
        # 这里可以使用图标，但为简单起见，我们使用文本
        self.setText("▼" if not self._collapsed else "▶")
        
    @property
    def collapsed(self):
        """获取折叠状态."""
        return self._collapsed
        
    @collapsed.setter
    def collapsed(self, value):
        """设置折叠状态."""
        if self._collapsed != value:
            self._collapsed = value
            self.update_icon()


class OnlineToolBar(QWidget):
    """在线工具工具栏."""
    
    sig_collapse = Signal(bool)  # 折叠信号
    
    def __init__(self, title, parent=None):
        """初始化在线工具工具栏."""
        QWidget.__init__(self, parent)
        
        # 设置固定高度
        self.setFixedHeight(30)
        
        # 设置样式
        self.setAutoFillBackground(True)
        pal = self.palette()
        pal.setColor(QPalette.Window, QColor("#333333"))
        self.setPalette(pal)
        
        # 创建布局
        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(10, 0, 10, 0)
        self.layout.setSpacing(5)
        
        # 添加折叠按钮
        self.collapse_button = CollapsibleButton("", self)
        self.collapse_button.clicked.connect(self.on_collapse_clicked)
        self.layout.addWidget(self.collapse_button)
        
        # 添加标题
        self.title_label = QLabel(title, self)
        self.title_label.setStyleSheet("color: #cccccc; font-weight: bold;")
        self.layout.addWidget(self.title_label)
        
        # 布局弹性空间
        self.layout.addStretch()
    
    def on_collapse_clicked(self):
        """折叠按钮点击处理."""
        self.collapse_button.collapsed = not self.collapse_button.collapsed
        self.sig_collapse.emit(self.collapse_button.collapsed)


class OnlineTools(QWidget):
    """在线工具组件."""
    
    def __init__(self, parent=None):
        """初始化在线工具组件."""
        QWidget.__init__(self, parent)
        
        # 状态
        self._is_collapsed = False
        self._tools_height = 300
        self._editors_collapsed = False
        self._online_tools_collapsed = False
        
        # 创建布局
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        
        # 创建工具栏
        self.toolbar = OnlineToolBar("在线工具", self)
        self.toolbar.sig_collapse.connect(self.on_collapse)
        self.layout.addWidget(self.toolbar)
        
        # 创建内容区域
        self.content = QWidget(self)
        self.content_layout = QVBoxLayout(self.content)
        self.content_layout.setContentsMargins(0, 0, 0, 0)
        self.content_layout.setSpacing(0)
        self.layout.addWidget(self.content)
        
        # 创建调整大小的手柄
        self.resize_handle = ResizeHandle(self)
        self.layout.addWidget(self.resize_handle)
        
        # 创建分割器
        self.splitter = QSplitter(Qt.Horizontal, self)
        self.content_layout.addWidget(self.splitter)
        
        # 创建编辑器区域
        self.editors_widget = QWidget(self)
        self.editors_layout = QVBoxLayout(self.editors_widget)
        self.editors_layout.setContentsMargins(0, 0, 0, 0)
        self.editors_layout.setSpacing(0)
        
        # 创建编辑器工具栏
        self.editors_toolbar = OnlineToolBar("编辑器", self)
        self.editors_toolbar.sig_collapse.connect(self.on_editors_collapse)
        self.editors_layout.addWidget(self.editors_toolbar)
        
        # 创建编辑器容器
        self.editors_container = QWidget(self)
        self.editors_container_layout = QVBoxLayout(self.editors_container)
        self.editors_container_layout.setContentsMargins(0, 0, 0, 0)
        self.editors_container_layout.setSpacing(0)
        self.editors_layout.addWidget(self.editors_container)
        
        # 创建编辑器分割视图
        self.editors_split = SplitViewManager(self)
        self.editors_container_layout.addWidget(self.editors_split)
        
        # 创建寄存器编辑器
        self.register_editor = RegisterEditor(self)
        self.register_editor_panel = self.editors_split.add_panel(self.register_editor)
        
        # 创建日志编辑器
        self.log_editor = LogEditor(self)
        self.log_editor_panel = self.editors_split.add_panel(self.log_editor)
        
        # 添加到分割器
        self.splitter.addWidget(self.editors_widget)
        
        # 创建在线工具区域
        self.tools_widget = QWidget(self)
        self.tools_layout = QVBoxLayout(self.tools_widget)
        self.tools_layout.setContentsMargins(0, 0, 0, 0)
        self.tools_layout.setSpacing(0)
        
        # 创建工具工具栏
        self.tools_toolbar = OnlineToolBar("工具", self)
        self.tools_toolbar.sig_collapse.connect(self.on_tools_collapse)
        self.tools_layout.addWidget(self.tools_toolbar)
        
        # 创建工具容器
        self.tools_container = QWidget(self)
        self.tools_container_layout = QVBoxLayout(self.tools_container)
        self.tools_container_layout.setContentsMargins(10, 10, 10, 10)
        self.tools_container_layout.setSpacing(10)
        self.tools_layout.addWidget(self.tools_container)
        
        # 创建发包工具
        self.packet_sender = PacketSender(self)
        self.tools_container_layout.addWidget(self.packet_sender)
        
        # 添加到分割器
        self.splitter.addWidget(self.tools_widget)
        
        # 设置分割器初始大小
        self.splitter.setSizes([500, 500])
        
        # 鼠标拖动大小调整
        self.dragging = False
        self.resize_handle.mousePressEvent = self.handle_mouse_press
        self.resize_handle.mouseMoveEvent = self.handle_mouse_move
        self.resize_handle.mouseReleaseEvent = self.handle_mouse_release
    
    def handle_mouse_press(self, event):
        """调整手柄鼠标按下事件."""
        if event.button() == Qt.LeftButton:
            self.dragging = True
            self.drag_start_y = event.globalPos().y()
            self.drag_start_height = self.height()
            self.setCursor(QCursor(Qt.SizeVerCursor))
    
    def handle_mouse_move(self, event):
        """调整手柄鼠标移动事件."""
        if self.dragging:
            delta_y = self.drag_start_y - event.globalPos().y()
            new_height = max(100, self.drag_start_height + delta_y)
            self._tools_height = new_height
            self.setFixedHeight(new_height)
    
    def handle_mouse_release(self, event):
        """调整手柄鼠标释放事件."""
        if event.button() == Qt.LeftButton and self.dragging:
            self.dragging = False
            self.setCursor(QCursor(Qt.ArrowCursor))
    
    def on_collapse(self, collapsed):
        """折叠/展开整个面板."""
        self._is_collapsed = collapsed
        
        if collapsed:
            self.content.setVisible(False)
            self.resize_handle.setVisible(False)
            self.setFixedHeight(30)
        else:
            self.content.setVisible(True)
            self.resize_handle.setVisible(True)
            self.setFixedHeight(self._tools_height)
    
    def on_editors_collapse(self, collapsed):
        """折叠/展开编辑器区域."""
        self._editors_collapsed = collapsed
        self.editors_container.setVisible(not collapsed)
    
    def on_tools_collapse(self, collapsed):
        """折叠/展开工具区域."""
        self._online_tools_collapsed = collapsed
        self.tools_container.setVisible(not collapsed)
        
    @property
    def is_collapsed(self):
        """获取折叠状态."""
        return self._is_collapsed
    
    @is_collapsed.setter
    def is_collapsed(self, value):
        """设置折叠状态."""
        self.toolbar.collapse_button.collapsed = value
        self.on_collapse(value)
        
    @property
    def editors_collapsed(self):
        """获取编辑器折叠状态."""
        return self._editors_collapsed
    
    @editors_collapsed.setter
    def editors_collapsed(self, value):
        """设置编辑器折叠状态."""
        self.editors_toolbar.collapse_button.collapsed = value
        self.on_editors_collapse(value)
        
    @property
    def online_tools_collapsed(self):
        """获取工具折叠状态."""
        return self._online_tools_collapsed
    
    @online_tools_collapsed.setter
    def online_tools_collapsed(self, value):
        """设置工具折叠状态."""
        self.tools_toolbar.collapse_button.collapsed = value
        self.on_tools_collapse(value) 