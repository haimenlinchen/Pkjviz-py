#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PySide6.QtCore import QObject, Signal

class DiagnosticResult(QObject):
    """诊断结果模型类"""
    
    # 信号
    result_changed = Signal()
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # 诊断信息
        self._code = "DIAG-001"
        self._action = "检查端口配置并重启服务"
        self._table_name = "ACL_TABLE"
        self._table_desc = "访问控制列表表，用于存储ACL规则"
        
        # 字段列表
        self._fields = [
            {"name": "acl_id", "description": "ACL唯一标识符", "value": "1001"},
            {"name": "priority", "description": "规则优先级", "value": "100"},
            {"name": "action", "description": "执行动作", "value": "PERMIT"}
        ]
    
    @property
    def code(self):
        """获取诊断码"""
        return self._code
    
    @code.setter
    def code(self, value):
        """设置诊断码"""
        if self._code != value:
            self._code = value
            self.result_changed.emit()
    
    @property
    def action(self):
        """获取诊断动作"""
        return self._action
    
    @action.setter
    def action(self, value):
        """设置诊断动作"""
        if self._action != value:
            self._action = value
            self.result_changed.emit()
    
    @property
    def table_name(self):
        """获取表名"""
        return self._table_name
    
    @table_name.setter
    def table_name(self, value):
        """设置表名"""
        if self._table_name != value:
            self._table_name = value
            self.result_changed.emit()
    
    @property
    def table_desc(self):
        """获取表描述"""
        return self._table_desc
    
    @table_desc.setter
    def table_desc(self, value):
        """设置表描述"""
        if self._table_desc != value:
            self._table_desc = value
            self.result_changed.emit()
    
    @property
    def fields(self):
        """获取字段列表"""
        return self._fields
    
    def add_field(self, name, description, value):
        """添加字段"""
        self._fields.append({
            "name": name,
            "description": description,
            "value": value
        })
        self.result_changed.emit()
    
    def update_field(self, index, name, description, value):
        """更新字段"""
        if 0 <= index < len(self._fields):
            self._fields[index] = {
                "name": name,
                "description": description,
                "value": value
            }
            self.result_changed.emit()
    
    def remove_field(self, index):
        """删除字段"""
        if 0 <= index < len(self._fields):
            del self._fields[index]
            self.result_changed.emit()
    
    def clear(self):
        """清空数据"""
        self._code = ""
        self._action = ""
        self._table_name = ""
        self._table_desc = ""
        self._fields = []
        self.result_changed.emit() 