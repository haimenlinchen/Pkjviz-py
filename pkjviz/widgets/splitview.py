"""
分屏视图组件
"""

# 标准库导入
import os
import sys
from typing import Dict, List, Optional

# 第三方库导入
from qtpy.QtCore import Qt, Signal, QPoint
from qtpy.QtWidgets import QWidget, QSplitter, QVBoxLayout, QHBoxLayout, QLabel


class ResizeHandle(QWidget):
    """分割器调整手柄."""

    def __init__(self, parent=None):
        """初始化调整手柄."""
        QWidget.__init__(self, parent)

        # 设置大小策略
        self.setFixedHeight(5)
        self.setCursor(Qt.SizeVerCursor)

        # 设置样式
        self.setStyleSheet(
            """
            ResizeHandle {
                background-color: #333333;
            }
            ResizeHandle:hover {
                background-color: #3a3d3e;
            }
        """
        )


class SplitViewManager(QWidget):
    """分割视图管理器."""

    sig_layout_changed = Signal()

    def __init__(self, parent=None):
        """初始化分割视图管理器."""
        QWidget.__init__(self, parent)

        # 设置布局
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        # 创建分割器
        self.splitter = QSplitter(Qt.Vertical, self)
        self.splitter.setChildrenCollapsible(False)
        self.splitter.setHandleWidth(1)
        self.splitter.splitterMoved.connect(self.splitter_moved)

        self.layout.addWidget(self.splitter)

        # 跟踪添加的面板
        self.panels = []

    def add_panel(self, panel, stretch=0):
        """添加面板到分割器."""
        self.splitter.addWidget(panel)
        self.panels.append(panel)

        if stretch > 0:
            self.splitter.setStretchFactor(len(self.panels) - 1, stretch)

        return panel

    def insert_panel(self, index, panel, stretch=0):
        """在指定位置插入面板."""
        self.splitter.insertWidget(index, panel)
        self.panels.insert(index, panel)

        if stretch > 0:
            self.splitter.setStretchFactor(index, stretch)

        return panel

    def remove_panel(self, panel):
        """移除面板."""
        if panel in self.panels:
            index = self.panels.index(panel)
            self.panels.remove(panel)
            panel.setParent(None)
            return index
        return -1

    def get_panel(self, index):
        """获取指定索引的面板."""
        if 0 <= index < len(self.panels):
            return self.panels[index]
        return None

    def get_panel_count(self):
        """获取面板数量."""
        return len(self.panels)

    def get_panel_sizes(self):
        """获取所有面板的大小."""
        return self.splitter.sizes()

    def set_panel_sizes(self, sizes):
        """设置所有面板的大小."""
        self.splitter.setSizes(sizes)

    def splitter_moved(self, pos, index):
        """分割器移动处理."""
        self.sig_layout_changed.emit()


class EditorSplitViewManager(SplitViewManager):
    """编辑器分割视图管理器."""

    def __init__(self, parent=None):
        """初始化编辑器分割视图管理器."""
        SplitViewManager.__init__(self, parent)

        # 编辑器分割视图的标记
        self.is_editor_manager = True

    def add_editor(self, editor, title="Editor"):
        """添加编辑器到分割器."""
        # 创建编辑器容器
        container = QWidget()
        layout = QVBoxLayout(container)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        # 添加标题栏
        title_bar = QWidget()
        title_bar.setFixedHeight(30)
        title_bar.setStyleSheet(
            """
            background-color: #252526;
            border-bottom: 1px solid #333333;
        """
        )

        title_layout = QHBoxLayout(title_bar)
        title_layout.setContentsMargins(10, 0, 10, 0)

        title_label = QLabel(title)
        title_label.setStyleSheet("color: #cccccc;")
        title_layout.addWidget(title_label)

        layout.addWidget(title_bar)
        layout.addWidget(editor)

        # 添加调整手柄
        resize_handle = ResizeHandle()
        layout.addWidget(resize_handle)

        # 添加到分割器
        return self.add_panel(container)

    def remove_editor(self, editor_container):
        """移除编辑器."""
        return self.remove_panel(editor_container)
