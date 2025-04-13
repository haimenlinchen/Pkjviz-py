#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PySide6.QtCore import QObject, Signal, Slot
from typing import List, Dict, Any, Optional

from src.models.register_model import RegisterData, RegisterTableModel


class RegisterController(QObject):
    """寄存器控制器类"""
    
    # 信号定义
    registersSaved = Signal()  # 寄存器保存成功信号
    registersLoaded = Signal() # 寄存器加载成功信号
    error = Signal(str)        # 错误信号
    
    def __init__(self, model: RegisterTableModel, parent: Optional[QObject] = None) -> None:
        """初始化寄存器控制器
        
        Args:
            model: 寄存器表格数据模型
            parent: 父对象
        """
        super().__init__(parent)
        self.model = model
        self.current_file_path = ""
        
    @Slot()
    def newFile(self) -> None:
        """创建新文件，清空寄存器数据"""
        self.model.clear()
        self.current_file_path = ""
        
    @Slot(str)
    def loadFromFile(self, file_path: str) -> None:
        """从文件加载寄存器数据
        
        Args:
            file_path: 文件路径
        """
        try:
            registers = []
            
            # 读取文件
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                
            # 解析文件内容为寄存器数据
            for line in lines:
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                    
                parts = line.split(',')
                if len(parts) >= 3:
                    address = parts[0].strip()
                    name = parts[1].strip()
                    value = parts[2].strip()
                    description = parts[3].strip() if len(parts) > 3 else ""
                    writable = True if len(parts) <= 4 or parts[4].strip().lower() == "true" else False
                    
                    register = RegisterData(address, name, value, description, writable)
                    registers.append(register)
            
            # 更新模型
            self.model.loadRegisters(registers)
            self.current_file_path = file_path
            self.registersLoaded.emit()
            
        except Exception as e:
            self.error.emit(f"加载文件失败: {str(e)}")
    
    @Slot(str)
    def saveToFile(self, file_path: str = "") -> None:
        """保存寄存器数据到文件
        
        Args:
            file_path: 文件路径，如果为空则使用当前文件路径
        """
        try:
            path = file_path if file_path else self.current_file_path
            
            if not path:
                self.error.emit("未指定文件路径")
                return
                
            # 写入文件
            with open(path, 'w', encoding='utf-8') as f:
                f.write("# 地址,名称,值,描述,可写\n")
                
                for reg in self.model.registers:
                    writable_str = "true" if reg.writable else "false"
                    line = f"{reg.address},{reg.name},{reg.value},{reg.description},{writable_str}\n"
                    f.write(line)
            
            # 更新当前文件路径
            if file_path:
                self.current_file_path = file_path
                
            # 应用更改（将当前值设为原始值）
            self.model.applyChanges()
            
            self.registersSaved.emit()
            
        except Exception as e:
            self.error.emit(f"保存文件失败: {str(e)}")
    
    @Slot()
    def resetChanges(self) -> None:
        """重置所有修改"""
        self.model.resetValues()
    
    @Slot(str, str)
    def importFromDevice(self, device_id: str, register_group: str) -> None:
        """从设备导入寄存器数据(示例方法)
        
        Args:
            device_id: 设备ID
            register_group: 寄存器组
        """
        # 在实际应用中，这里会与硬件通信，读取真实设备的寄存器值
        # 这里只是创建一些示例数据
        try:
            registers = []
            
            # 创建一些示例数据
            for i in range(10):
                address = f"0x{i:04X}"
                name = f"REG_{i}"
                value = f"0x{i*16:04X}"
                description = f"寄存器 {i} 描述"
                writable = i % 2 == 0  # 偶数寄存器可写
                
                register = RegisterData(address, name, value, description, writable)
                registers.append(register)
            
            # 更新模型
            self.model.loadRegisters(registers)
            self.current_file_path = ""  # 从设备导入，清空文件路径
            self.registersLoaded.emit()
            
        except Exception as e:
            self.error.emit(f"从设备导入失败: {str(e)}")
    
    @Slot()
    def exportToDevice(self) -> None:
        """导出修改的寄存器值到设备(示例方法)"""
        # 在实际应用中，这里会与硬件通信，将修改的寄存器值写入设备
        try:
            # 获取修改过的寄存器
            modified_registers = self.model.getModifiedRegisters()
            
            if not modified_registers:
                self.error.emit("没有修改过的寄存器值")
                return
                
            # 模拟写入设备操作
            for reg in modified_registers:
                # 这里应该是实际写入设备的代码
                print(f"写入设备: 地址={reg.address}, 值={reg.value}")
            
            # 应用更改
            self.model.applyChanges()
            
        except Exception as e:
            self.error.emit(f"导出到设备失败: {str(e)}")
    
    @Slot(str, str, str)
    def updateRegisterValue(self, address: str, name: str, value: str) -> None:
        """更新寄存器值
        
        Args:
            address: 寄存器地址
            name: 寄存器名称
            value: 新值
        """
        # 查找并更新寄存器值
        for i, reg in enumerate(self.model.registers):
            if reg.address == address and reg.name == name:
                # 通过model的setData更新，以触发正确的信号
                index = self.model.index(i, 2)  # 值列的索引
                self.model.setData(index, value) 