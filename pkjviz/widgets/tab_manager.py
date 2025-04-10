"""
标签页管理器和拖拽控件
"""

# 标准库导入
import os
import sys

# 第三方库导入
from qtpy.QtCore import Qt, Signal, QPoint, QMimeData
from qtpy.QtGui import QDrag, QCursor, QPixmap, QPainter, QColor
from qtpy.QtWidgets import (
    QWidget, QTabWidget, QTabBar, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QStyle, QStyleOptionTab
)

class TabDragHandle(QWidget):
    """可拖拽的标签页控件."""
    
    sig_tab_dragged = Signal(int, QPoint)  # 标签被拖拽的信号(标签索引, 目标位置)
    sig_tab_dropped = Signal(int, QPoint)  # 标签被放下的信号(标签索引, 目标位置)
    
    def __init__(self, parent=None):
        """初始化标签拖拽控件."""
        QWidget.__init__(self, parent)
        
        # 设置接受拖放
        self.setAcceptDrops(True)
        
        # 拖拽状态
        self.drag_start_pos = None
        self.dragging = False
        self.drag_index = -1
        
    def mousePressEvent(self, event):
        """鼠标按下事件处理."""
        if event.button() == Qt.LeftButton:
            self.drag_start_pos = event.pos()
        super().mousePressEvent(event)
        
    def mouseMoveEvent(self, event):
        """鼠标移动事件处理."""
        if not (event.buttons() & Qt.LeftButton) or not self.drag_start_pos:
            return
        
        # 计算移动距离，判断是否达到拖拽阈值
        distance = (event.pos() - self.drag_start_pos).manhattanLength()
        if distance < QApplication.startDragDistance():
            return
            
        # 开始拖拽
        self.start_drag()
        
    def start_drag(self):
        """开始拖拽操作."""
        if not hasattr(self.parent(), 'tabBar') or not hasattr(self.parent(), 'currentIndex'):
            return
            
        tab_bar = self.parent().tabBar()
        current_index = self.parent().currentIndex()
        
        # 创建拖拽的图像
        drag_pixmap = self.create_drag_pixmap(tab_bar, current_index)
        
        # 创建拖拽对象
        drag = QDrag(self)
        mime_data = QMimeData()
        mime_data.setData("application/x-tab-drag", bytes(str(current_index), 'utf-8'))
        drag.setMimeData(mime_data)
        drag.setPixmap(drag_pixmap)
        drag.setHotSpot(QPoint(drag_pixmap.width() // 2, 10))
        
        self.dragging = True
        self.drag_index = current_index
        
        # 发出拖拽信号
        self.sig_tab_dragged.emit(current_index, QCursor.pos())
        
        # 执行拖拽
        result = drag.exec_(Qt.MoveAction)
        
        self.dragging = False
        
    def create_drag_pixmap(self, tab_bar, index):
        """为拖拽创建标签页图像."""
        # 获取标签区域
        rect = tab_bar.tabRect(index)
        
        # 创建图像
        pixmap = QPixmap(rect.size())
        pixmap.fill(Qt.transparent)
        
        # 绘制标签
        painter = QPainter(pixmap)
        
        # 创建样式选项
        option = QStyleOptionTab()
        tab_bar.initStyleOption(option, index)
        option.rect = pixmap.rect()
        
        # 绘制标签
        tab_bar.style().drawControl(QStyle.CE_TabBarTab, option, painter, tab_bar)
        
        # 添加半透明效果
        painter.fillRect(pixmap.rect(), QColor(0, 0, 0, 80))
        
        painter.end()
        
        return pixmap
        
    def dragEnterEvent(self, event):
        """拖拽进入事件处理."""
        if event.mimeData().hasFormat("application/x-tab-drag"):
            event.acceptProposedAction()
        
    def dragMoveEvent(self, event):
        """拖拽移动事件处理."""
        if event.mimeData().hasFormat("application/x-tab-drag"):
            event.acceptProposedAction()
        
    def dropEvent(self, event):
        """拖拽放下事件处理."""
        if event.mimeData().hasFormat("application/x-tab-drag"):
            # 获取拖拽的标签索引
            source_index = int(event.mimeData().data("application/x-tab-drag").data().decode('utf-8'))
            
            # 获取拖拽目标位置
            drop_pos = event.pos()
            
            # 发出放下信号
            self.sig_tab_dropped.emit(source_index, drop_pos)
            
            event.acceptProposedAction()


class TabManager(QTabWidget):
    """标签页管理器."""
    
    sig_tab_moved = Signal(int, int)  # 标签被移动的信号(原索引, 新索引)
    sig_tab_detached = Signal(int, QPoint)  # 标签被分离的信号(标签索引, 分离位置)
    
    def __init__(self, parent=None):
        """初始化标签页管理器."""
        QTabWidget.__init__(self, parent)
        
        # 设置标签可移动和关闭
        self.setTabsClosable(True)
        self.setMovable(True)
        
        # 连接信号
        self.tabBar().tabMoved.connect(self.on_tab_moved)
        self.tabCloseRequested.connect(self.on_tab_close_requested)
        
        # 为标签栏添加拖拽功能
        self.drag_handle = TabDragHandle(self)
        self.drag_handle.sig_tab_dragged.connect(self.on_tab_dragged)
        self.drag_handle.sig_tab_dropped.connect(self.on_tab_dropped)
        
        # 设置接受拖放
        self.setAcceptDrops(True)
        
    def on_tab_moved(self, from_index, to_index):
        """标签移动处理."""
        self.sig_tab_moved.emit(from_index, to_index)
        
    def on_tab_close_requested(self, index):
        """标签关闭请求处理."""
        # 默认实现是移除标签页
        widget = self.widget(index)
        self.removeTab(index)
        
        # 如果子类需要特殊处理已移除的部件，可以重写此方法
        # 例如，在这里可以删除部件或将其隐藏
        if widget is not None:
            widget.setParent(None)
        
    def on_tab_dragged(self, index, pos):
        """标签被拖拽处理."""
        # 这里可以实现标签拖拽时的视觉反馈
        pass
        
    def on_tab_dropped(self, index, pos):
        """标签被放下处理."""
        # 检查放下位置是否在标签栏内
        tab_bar = self.tabBar()
        tab_bar_pos = tab_bar.mapFromGlobal(pos)
        
        if not tab_bar.rect().contains(tab_bar_pos):
            # 标签被拖拽到标签栏外 - 分离
            self.detach_tab(index, pos)
        else:
            # 标签在标签栏内 - 获取目标索引
            target_index = tab_bar.tabAt(tab_bar_pos)
            if target_index >= 0 and target_index != index:
                # 移动标签
                self.tabBar().moveTab(index, target_index)
            
    def detach_tab(self, index, pos):
        """分离标签页."""
        # 发出标签分离信号
        self.sig_tab_detached.emit(index, pos)
        
    def add_tab_with_drag(self, widget, title):
        """添加带拖拽功能的标签页."""
        index = self.addTab(widget, title)
        return index 