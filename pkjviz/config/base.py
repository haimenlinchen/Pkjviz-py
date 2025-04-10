"""
基本配置模块
"""

# 标准库导入
import os
import sys
import tempfile
from pathlib import Path


def get_home_dir():
    """获取用户主目录."""
    return str(Path.home())


def get_conf_path(filename=None):
    """
    获取配置文件的路径.
    如果 filename 不为 None，返回配置文件的完整路径。
    否则返回包含所有配置文件的目录路径。
    """
    conf_dir = Path(get_home_dir()) / ".pkjviz"

    # 确保配置目录存在
    if not conf_dir.exists():
        try:
            conf_dir.mkdir(parents=True)
        except OSError:
            return None

    if filename is not None:
        return str(conf_dir / filename)
    else:
        return str(conf_dir)


def get_module_path(modname):
    """返回模块的路径."""
    try:
        module = __import__(modname)
    except ImportError:
        return None
    return os.path.dirname(module.__file__)


def get_module_source_path(modname):
    """返回模块源代码路径."""
    module_path = get_module_path(modname)
    if module_path is None:
        return None
    for path in [
        os.path.join(module_path, "__init__.py"),
        os.path.join(module_path, "main.py"),
        os.path.join(module_path, modname + ".py"),
    ]:
        if os.path.isfile(path):
            return path
    return None


def is_dark_theme():
    """
    判断当前是否为暗色主题.
    """
    # 从配置文件读取主题设置，默认为暗色主题
    from pkjviz.config.main import CONF

    theme = CONF.get("main", "theme", fallback="dark")
    return theme.lower() == "dark"
