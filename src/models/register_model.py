#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PySide6.QtCore import Qt, QAbstractTableModel, QModelIndex, QPersistentModelIndex
from PySide6.QtGui import QColor
from typing import Dict, List, Any, Optional, Union


class RegisterData:
    """寄存器数据类"""
    
    def __init__(self, address: str = "", name: str = "", value: str = "", 
                 description: str = "", writable: bool = True) -> None:
        self.address = address          # 寄存器地址
        self.name = name                # 寄存器名称 
        self.value = value              # 寄存器值
        self.description = description  # 寄存器描述
        self.writable = writable        # 是否可写
        self.original_value = value     # 原始值，用于比较是否修改


class RegisterTableModel(QAbstractTableModel):
    """寄存器表格数据模型"""
    
    # 列定义
    COLUMNS = ["地址", "名称", "值", "描述", "可写"]
    
    def __init__(self, parent: Optional[Any] = None) -> None:
        super().__init__(parent)
        self.registers: List[RegisterData] = []
    
    def rowCount(self, parent: Union[QModelIndex, QPersistentModelIndex] = QModelIndex()) -> int:
        if parent.isValid():
            return 0
        return len(self.registers)
    
    def columnCount(self, parent: Union[QModelIndex, QPersistentModelIndex] = QModelIndex()) -> int:
        if parent.isValid():
            return 0
        return len(self.COLUMNS)
    
    def data(self, index: Union[QModelIndex, QPersistentModelIndex], role: int = Qt.ItemDataRole.DisplayRole) -> Any:
        if not index.isValid() or index.row() >= len(self.registers):
            return None
        
        register = self.registers[index.row()]
        col = index.column()
        
        if role == Qt.ItemDataRole.DisplayRole or role == Qt.ItemDataRole.EditRole:
            if col == 0:
                return register.address
            elif col == 1:
                return register.name
            elif col == 2:
                return register.value
            elif col == 3:
                return register.description
            elif col == 4:
                return "是" if register.writable else "否"
        
        elif role == Qt.ItemDataRole.BackgroundRole:
            # 如果值被修改，使用淡黄色背景高亮显示
            if col == 2 and register.value != register.original_value:
                return QColor(255, 255, 200)
        
        return None
    
    def headerData(self, section: int, orientation: Qt.Orientation, role: int = Qt.ItemDataRole.DisplayRole) -> Any:
        if role == Qt.ItemDataRole.DisplayRole and orientation == Qt.Orientation.Horizontal:
            return self.COLUMNS[section]
        return None
    
    def flags(self, index: Union[QModelIndex, QPersistentModelIndex]) -> Qt.ItemFlag:
        if not index.isValid():
            return Qt.ItemFlag.NoItemFlags
        
        # 只允许编辑值列
        if index.column() == 2 and self.registers[index.row()].writable:
            return super().flags(index) | Qt.ItemFlag.ItemIsEditable
        
        return super().flags(index)
    
    def setData(self, index: Union[QModelIndex, QPersistentModelIndex], value: Any, role: int = Qt.ItemDataRole.EditRole) -> bool:
        if not index.isValid() or index.column() != 2 or not self.registers[index.row()].writable:
            return False
        
        if role == Qt.ItemDataRole.EditRole:
            self.registers[index.row()].value = value
            self.dataChanged.emit(index, index)
            return True
        
        return False
    
    def addRegister(self, register: RegisterData) -> None:
        """添加一个寄存器数据"""
        self.beginInsertRows(QModelIndex(), len(self.registers), len(self.registers))
        self.registers.append(register)
        self.endInsertRows()
    
    def clear(self) -> None:
        """清除所有寄存器数据"""
        self.beginResetModel()
        self.registers.clear()
        self.endResetModel()
    
    def loadRegisters(self, registers: List[RegisterData]) -> None:
        """加载寄存器数据列表"""
        self.beginResetModel()
        self.registers = registers
        self.endResetModel()
    
    def getRegisterByIndex(self, index: int) -> Optional[RegisterData]:
        """通过索引获取寄存器数据"""
        if 0 <= index < len(self.registers):
            return self.registers[index]
        return None
    
    def getModifiedRegisters(self) -> List[RegisterData]:
        """获取所有被修改的寄存器数据"""
        return [reg for reg in self.registers if reg.value != reg.original_value]
    
    def resetValues(self) -> None:
        """重置所有修改，恢复到原始值"""
        for i, reg in enumerate(self.registers):
            if reg.value != reg.original_value:
                reg.value = reg.original_value
        
        # 通知视图更新
        self.dataChanged.emit(
            self.index(0, 2), 
            self.index(len(self.registers) - 1, 2)
        )
    
    def applyChanges(self) -> None:
        """应用所有修改，将当前值设为原始值"""
        for reg in self.registers:
            reg.original_value = reg.value
        
        # 通知视图更新
        self.dataChanged.emit(
            self.index(0, 2), 
            self.index(len(self.registers) - 1, 2)
        ) 