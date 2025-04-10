"""
Pkjviz 主应用程序模块
"""

# 标准库导入
import os
import sys
import logging

# 第三方库导入
from qtpy.QtCore import QTimer, Qt
from qtpy.QtWidgets import QApplication, QSplashScreen
from qtpy.QtGui import QPixmap

# 本地导入
from pkjviz.app.mainwindow import MainWindow
from pkjviz.config.main import CONF

# 配置日志
logger = logging.getLogger(__name__)


def initialize():
    """
    初始化应用程序环境.
    """
    # 设置日志
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    # 确保配置目录存在
    from pkjviz.config.base import get_conf_path
    conf_dir = get_conf_path()
    if conf_dir is None:
        logger.error("无法创建配置目录.")
        sys.exit(1)


def create_application():
    """
    创建并返回 Qt 应用程序实例.
    """
    # 创建应用程序
    app = QApplication([])
    
    # 设置应用程序属性
    app.setApplicationName("Pkjviz")
    app.setOrganizationName("Pkjviz")
    app.setOrganizationDomain("pkjviz.org")
    
    # 设置样式表
    style = """
    QMainWindow, QDialog {
        background-color: #1e1e1e;
        color: #cccccc;
    }
    QMenuBar {
        background-color: #252526;
        color: #cccccc;
    }
    QMenuBar::item {
        background-color: #252526;
        color: #cccccc;
    }
    QMenuBar::item:selected {
        background-color: #3a3d3e;
    }
    QMenu {
        background-color: #252526;
        color: #cccccc;
        border: 1px solid #333333;
    }
    QMenu::item:selected {
        background-color: #3a3d3e;
    }
    QToolBar {
        background-color: #333333;
        border: none;
    }
    QStatusBar {
        background-color: #252526;
        color: #cccccc;
    }
    QSplitter::handle {
        background-color: #333333;
    }
    QTabBar::tab {
        background-color: #252526;
        color: #cccccc;
        border: 1px solid #333333;
        padding: 5px 10px;
        border-top-left-radius: 3px;
        border-top-right-radius: 3px;
    }
    QTabBar::tab:selected {
        background-color: #1e1e1e;
        border-bottom-color: #1e1e1e;
    }
    """
    app.setStyleSheet(style)
    
    return app


def create_splash_screen():
    """
    创建并返回启动画面.
    """
    # 这里应该加载启动画面图像，但暂时使用纯色背景
    pixmap = QPixmap(400, 300)
    pixmap.fill(Qt.darkGray)
    
    splash = QSplashScreen(pixmap)
    splash.showMessage("正在加载 Pkjviz...", 
                      Qt.AlignBottom | Qt.AlignCenter, 
                      Qt.white)
    splash.show()
    
    return splash


def main():
    """
    主函数.
    """
    # 初始化环境
    initialize()
    
    # 创建应用程序
    app = create_application()
    
    # 创建启动画面
    splash = create_splash_screen()
    app.processEvents()
    
    # 创建主窗口
    window = MainWindow(splash=splash)
    
    # 显示主窗口并关闭启动画面
    QTimer.singleShot(1000, lambda: window.show())
    QTimer.singleShot(1500, lambda: splash.close())
    
    # 运行应用程序
    return app.exec_()


if __name__ == '__main__':
    sys.exit(main()) 