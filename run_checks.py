#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
运行项目的所有检查工具，包括：
- mypy 类型检查
- pytest 单元测试
"""

import os
import sys
import subprocess
from typing import List, Dict, Tuple, Optional


def run_command(cmd: List[str]) -> Tuple[int, str, str]:
    """运行命令并返回结果
    
    Args:
        cmd: 要运行的命令和参数
        
    Returns:
        Tuple[int, str, str]: 返回码、标准输出、标准错误
    """
    proc = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    stdout, stderr = proc.communicate()
    return proc.returncode, stdout, stderr


def run_mypy() -> bool:
    """运行mypy类型检查
    
    Returns:
        bool: 检查是否通过
    """
    print("运行 mypy 类型检查...")
    returncode, stdout, stderr = run_command(["mypy", "src"])
    
    if stdout:
        print(stdout)
    if stderr:
        print(stderr, file=sys.stderr)
        
    if returncode == 0:
        print("✅ 类型检查通过")
        return True
    else:
        print(f"❌ 类型检查失败 (返回码: {returncode})")
        return False


def run_pytest() -> bool:
    """运行pytest单元测试
    
    Returns:
        bool: 测试是否通过
    """
    print("\n运行 pytest 单元测试...")
    returncode, stdout, stderr = run_command(["pytest", "-v"])
    
    if stdout:
        print(stdout)
    if stderr:
        print(stderr, file=sys.stderr)
        
    if returncode == 0:
        print("✅ 单元测试通过")
        return True
    else:
        print(f"❌ 单元测试失败 (返回码: {returncode})")
        return False


def main() -> int:
    """主函数
    
    Returns:
        int: 程序返回码
    """
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    mypy_success = run_mypy()
    pytest_success = run_pytest()
    
    # 所有检查都通过才返回成功
    if mypy_success and pytest_success:
        print("\n✅✅ 所有检查通过!")
        return 0
    else:
        print("\n❌❌ 检查未通过!")
        return 1


if __name__ == "__main__":
    sys.exit(main()) 