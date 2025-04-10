"""
编辑器组件
"""

# 标准库导入
import os
import sys

# 第三方库导入
from qtpy.QtCore import Qt, Signal
from qtpy.QtGui import QColor, QTextCursor
from qtpy.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPlainTextEdit,
    QLabel,
    QToolBar,
    QSplitter,
)


class Editor(QWidget):
    """编辑器组件."""

    sig_text_changed = Signal()

    def __init__(self, parent=None):
        """初始化编辑器."""
        QWidget.__init__(self, parent)

        # 设置布局
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        self.setLayout(self.layout)

        # 创建工具栏
        self.toolbar = QToolBar(self)
        self.layout.addWidget(self.toolbar)

        # 创建编辑器控件
        self.editor = QPlainTextEdit(self)
        self.layout.addWidget(self.editor)

        # 设置编辑器属性
        self.editor.setLineWrapMode(QPlainTextEdit.NoWrap)
        self.editor.textChanged.connect(self.text_changed)

        # 创建状态栏
        self.status_bar = QWidget(self)
        self.status_layout = QHBoxLayout(self.status_bar)
        self.status_layout.setContentsMargins(5, 0, 5, 0)

        self.line_col_label = QLabel("行: 1, 列: 1")
        self.status_layout.addWidget(self.line_col_label)

        self.status_layout.addStretch()

        self.encoding_label = QLabel("UTF-8")
        self.status_layout.addWidget(self.encoding_label)

        self.layout.addWidget(self.status_bar)

        # 连接光标位置变化信号
        self.editor.cursorPositionChanged.connect(self.update_cursor_position)

    def text_changed(self):
        """文本内容变化处理函数."""
        self.sig_text_changed.emit()

    def update_cursor_position(self):
        """更新光标位置显示."""
        cursor = self.editor.textCursor()
        line = cursor.blockNumber() + 1
        col = cursor.columnNumber() + 1
        self.line_col_label.setText(f"行: {line}, 列: {col}")

    def get_text(self):
        """获取编辑器文本内容."""
        return self.editor.toPlainText()

    def set_text(self, text):
        """设置编辑器文本内容."""
        self.editor.setPlainText(text)

    def clear(self):
        """清空编辑器内容."""
        self.editor.clear()


class LogEditor(Editor):
    """日志编辑器组件."""

    def __init__(self, parent=None):
        """初始化日志编辑器."""
        Editor.__init__(self, parent)

        # 设置为只读
        self.editor.setReadOnly(True)

        # 设置样式
        self.editor.setStyleSheet(
            """
            QPlainTextEdit {
                background-color: #1e1e1e;
                color: #f0f0f0;
                font-family: Monospace;
            }
        """
        )

    def append_log(self, text, color=None):
        """添加日志内容."""
        cursor = self.editor.textCursor()
        cursor.movePosition(QTextCursor.End)

        if color is not None:
            format = cursor.charFormat()
            format.setForeground(QColor(color))
            cursor.setCharFormat(format)

        cursor.insertText(text + "\n")
        self.editor.setTextCursor(cursor)
        self.editor.ensureCursorVisible()


class RegisterEditor(Editor):
    """寄存器编辑器组件."""

    def __init__(self, parent=None):
        """初始化寄存器编辑器."""
        Editor.__init__(self, parent)

        # 自定义工具栏
        from pkjviz.utils.qthelpers import create_toolbutton

        self.refresh_button = create_toolbutton(
            self.toolbar, text="刷新", tip="刷新寄存器数据", triggered=self.refresh_data
        )
        self.toolbar.addWidget(self.refresh_button)

        self.toolbar.addSeparator()

        self.read_button = create_toolbutton(
            self.toolbar,
            text="读取",
            tip="读取寄存器数据",
            triggered=self.read_register,
        )
        self.toolbar.addWidget(self.read_button)

        self.write_button = create_toolbutton(
            self.toolbar,
            text="写入",
            tip="写入寄存器数据",
            triggered=self.write_register,
        )
        self.toolbar.addWidget(self.write_button)

    def refresh_data(self):
        """刷新寄存器数据."""
        pass

    def read_register(self):
        """读取寄存器数据."""
        pass

    def write_register(self):
        """写入寄存器数据."""
        pass
