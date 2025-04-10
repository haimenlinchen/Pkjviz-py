"""
项目文件浏览器组件
"""

# 标准库导入
import os
import sys
from pathlib import Path

# 第三方库导入
from qtpy.QtCore import Qt, Signal, QDir, QFileInfo
from qtpy.QtGui import QIcon, QColor
from qtpy.QtWidgets import (
    QWidget, QVBoxLayout, QTreeView, QFileSystemModel,
    QHeaderView, QMenu, QAction, QToolBar, QLineEdit,
    QPushButton, QHBoxLayout, QMessageBox, QInputDialog,
    QFileDialog
)

# 本地导入
from pkjviz.utils.qthelpers import create_action, create_toolbutton


class ProjectFileSystemModel(QFileSystemModel):
    """项目文件系统模型."""
    
    def __init__(self, parent=None):
        """初始化项目文件系统模型."""
        QFileSystemModel.__init__(self, parent)
        
        # 设置筛选器
        self.setFilter(QDir.AllDirs | QDir.Files | QDir.NoDotAndDotDot)
        
        # 设置隐藏文件
        hidden_patterns = ["__pycache__", "*.pyc", "*.pyo", "*.pyd", ".git", ".svn", ".hg"]
        self.setNameFilters(hidden_patterns)
        self.setNameFilterDisables(False)  # 隐藏不匹配的项，而不是禁用
        
    def data(self, index, role):
        """自定义数据展示."""
        if role == Qt.DecorationRole:  # 图标
            if index.column() == 0:
                info = self.fileInfo(index)
                if info.isDir():
                    return QIcon.fromTheme("folder")
                else:
                    # 根据文件类型设置不同图标
                    suffix = info.suffix().lower()
                    if suffix in ["py", "pyw"]:
                        return QIcon.fromTheme("text-x-python")
                    elif suffix in ["txt", "md", "rst"]:
                        return QIcon.fromTheme("text-x-generic")
                    elif suffix in ["json", "xml", "yml", "yaml"]:
                        return QIcon.fromTheme("text-x-script")
                    else:
                        return QIcon.fromTheme("text-x-generic")
                        
        return QFileSystemModel.data(self, index, role)


class ProjectBrowser(QWidget):
    """项目文件浏览器组件."""
    
    sig_file_opened = Signal(str)  # 文件打开信号(文件路径)
    
    def __init__(self, parent=None):
        """初始化项目文件浏览器."""
        QWidget.__init__(self, parent)
        
        # 设置布局
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        
        # 创建工具栏
        self.toolbar = QToolBar(self)
        self.toolbar.setObjectName("ProjectToolbar")
        self.layout.addWidget(self.toolbar)
        
        # 添加打开文件夹按钮
        self.open_folder_action = create_toolbutton(
            self, text="打开文件夹", 
            tip="打开一个项目文件夹",
            triggered=self.open_folder
        )
        self.toolbar.addWidget(self.open_folder_action)
        
        # 添加刷新按钮
        self.refresh_action = create_toolbutton(
            self, text="刷新", 
            tip="刷新项目文件",
            triggered=self.refresh
        )
        self.toolbar.addWidget(self.refresh_action)
        
        # 创建文件系统模型
        self.model = ProjectFileSystemModel(self)
        
        # 创建树形视图
        self.tree_view = QTreeView(self)
        self.tree_view.setModel(self.model)
        self.tree_view.setAnimated(False)
        self.tree_view.setIndentation(20)
        self.tree_view.setSortingEnabled(True)
        self.tree_view.sortByColumn(0, Qt.AscendingOrder)
        self.tree_view.setEditTriggers(QTreeView.NoEditTriggers)
        self.tree_view.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tree_view.customContextMenuRequested.connect(self.show_context_menu)
        self.tree_view.doubleClicked.connect(self.on_item_double_clicked)
        
        # 隐藏不需要的列
        self.tree_view.setHeaderHidden(True)
        for i in range(1, self.model.columnCount()):
            self.tree_view.hideColumn(i)
        
        self.layout.addWidget(self.tree_view)
        
        # 保存当前打开的项目路径
        self.current_project_path = None
        
        # 创建快捷键
        self.setup_shortcuts()
        
    def setup_shortcuts(self):
        """设置快捷键."""
        # 暂时没有添加快捷键
        pass
        
    def open_folder(self):
        """打开项目文件夹."""
        folder_path = QFileDialog.getExistingDirectory(
            self, "选择项目文件夹", 
            os.path.expanduser("~"),
            QFileDialog.ShowDirsOnly
        )
        
        if folder_path:
            self.set_project_root(folder_path)
    
    def set_project_root(self, path):
        """设置项目根目录."""
        if not os.path.isdir(path):
            QMessageBox.warning(self, "错误", f"路径不存在: {path}")
            return
            
        # 设置根目录
        root_index = self.model.setRootPath(path)
        self.tree_view.setRootIndex(root_index)
        
        # 展开第一级
        self.tree_view.expand(root_index)
        
        # 保存当前项目路径
        self.current_project_path = path
        
        # 设置窗口标题
        self.parent().setWindowTitle(f"Pkjviz - {os.path.basename(path)}")
        
    def refresh(self):
        """刷新项目树."""
        if self.current_project_path:
            self.model.refresh(self.model.index(self.current_project_path))
            
    def on_item_double_clicked(self, index):
        """双击项目处理."""
        file_path = self.model.filePath(index)
        
        if os.path.isfile(file_path):
            # 发出文件打开信号
            self.sig_file_opened.emit(file_path)
    
    def show_context_menu(self, position):
        """显示上下文菜单."""
        index = self.tree_view.indexAt(position)
        if not index.isValid():
            return
            
        file_path = self.model.filePath(index)
        is_dir = os.path.isdir(file_path)
        
        # 创建上下文菜单
        menu = QMenu(self)
        
        # 添加打开文件选项 (仅对文件有效)
        if not is_dir:
            open_action = menu.addAction("打开")
            open_action.triggered.connect(lambda: self.sig_file_opened.emit(file_path))
        
        # 添加新建选项 (仅对目录有效)
        if is_dir:
            new_menu = menu.addMenu("新建")
            
            # 新建文件
            new_file_action = new_menu.addAction("文件")
            new_file_action.triggered.connect(lambda: self.create_new_file(file_path))
            
            # 新建目录
            new_dir_action = new_menu.addAction("目录")
            new_dir_action.triggered.connect(lambda: self.create_new_directory(file_path))
        
        menu.addSeparator()
        
        # 重命名选项
        rename_action = menu.addAction("重命名")
        rename_action.triggered.connect(lambda: self.rename_item(file_path))
        
        # 删除选项
        delete_action = menu.addAction("删除")
        delete_action.triggered.connect(lambda: self.delete_item(file_path))
        
        # 显示菜单
        menu.exec_(self.tree_view.viewport().mapToGlobal(position))
        
    def create_new_file(self, parent_dir):
        """创建新文件."""
        file_name, ok = QInputDialog.getText(
            self, "新建文件", 
            "请输入文件名:",
            QLineEdit.Normal,
            "新文件.txt"
        )
        
        if ok and file_name:
            # 创建文件
            file_path = os.path.join(parent_dir, file_name)
            
            try:
                # 检查文件是否已存在
                if os.path.exists(file_path):
                    QMessageBox.warning(self, "错误", f"文件已存在: {file_name}")
                    return
                    
                # 创建文件
                with open(file_path, 'w') as f:
                    pass  # 创建空文件
                    
                # 刷新
                self.refresh()
                
            except Exception as e:
                QMessageBox.critical(self, "错误", f"创建文件失败: {str(e)}")
    
    def create_new_directory(self, parent_dir):
        """创建新目录."""
        dir_name, ok = QInputDialog.getText(
            self, "新建目录", 
            "请输入目录名:",
            QLineEdit.Normal,
            "新目录"
        )
        
        if ok and dir_name:
            # 创建目录
            dir_path = os.path.join(parent_dir, dir_name)
            
            try:
                # 检查目录是否已存在
                if os.path.exists(dir_path):
                    QMessageBox.warning(self, "错误", f"目录已存在: {dir_name}")
                    return
                    
                # 创建目录
                os.mkdir(dir_path)
                
                # 刷新
                self.refresh()
                
            except Exception as e:
                QMessageBox.critical(self, "错误", f"创建目录失败: {str(e)}")
    
    def rename_item(self, file_path):
        """重命名项目."""
        old_name = os.path.basename(file_path)
        parent_dir = os.path.dirname(file_path)
        
        new_name, ok = QInputDialog.getText(
            self, "重命名", 
            "请输入新名称:",
            QLineEdit.Normal,
            old_name
        )
        
        if ok and new_name and new_name != old_name:
            # 创建新路径
            new_path = os.path.join(parent_dir, new_name)
            
            try:
                # 检查新名称是否已存在
                if os.path.exists(new_path):
                    QMessageBox.warning(self, "错误", f"文件或目录已存在: {new_name}")
                    return
                    
                # 重命名
                os.rename(file_path, new_path)
                
                # 刷新
                self.refresh()
                
            except Exception as e:
                QMessageBox.critical(self, "错误", f"重命名失败: {str(e)}")
    
    def delete_item(self, file_path):
        """删除项目."""
        is_dir = os.path.isdir(file_path)
        name = os.path.basename(file_path)
        
        # 确认删除
        msg = f"确定要删除{'目录' if is_dir else '文件'} \"{name}\"?"
        if is_dir:
            msg += "\n\n注意: 此操作将删除目录中的所有内容!"
            
        reply = QMessageBox.question(
            self, "确认删除", msg,
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )
        
        if reply == QMessageBox.Yes:
            try:
                if is_dir:
                    # 删除目录 (及其内容)
                    import shutil
                    shutil.rmtree(file_path)
                else:
                    # 删除文件
                    os.remove(file_path)
                    
                # 刷新
                self.refresh()
                
            except Exception as e:
                QMessageBox.critical(self, "错误", f"删除失败: {str(e)}")
                
    def get_current_project_path(self):
        """获取当前项目路径."""
        return self.current_project_path 