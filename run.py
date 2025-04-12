#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pkjviz 启动脚本
"""

import os
import sys

# 添加src目录到路径
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "src"))

# 导入主模块并运行
from src.main import main

if __name__ == "__main__":
    main()
