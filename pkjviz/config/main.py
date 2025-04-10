"""
主配置模块
"""

# 标准库导入
import os
import sys
from configparser import ConfigParser

# 本地导入
from pkjviz.config.base import get_conf_path

# 配置
CONF = ConfigParser()

# 应用程序设置
CONF.add_section("main")
CONF.set("main", "theme", "dark")
CONF.set("main", "language", "zh_CN")
CONF.set("main", "window_size", "1200,800")

# 编辑器设置
CONF.add_section("editor")
CONF.set("editor", "font", "Monospace")
CONF.set("editor", "font_size", "10")
CONF.set("editor", "show_line_numbers", "True")
CONF.set("editor", "auto_completion", "True")
CONF.set("editor", "highlight_current_line", "True")

# 网络设置
CONF.add_section("network")
CONF.set("network", "timeout", "30")
