#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PySide6.QtCore import Qt, QAbstractTableModel, QModelIndex

class ACLTableModel(QAbstractTableModel):
    """ACL表格数据模型"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # 定义列名
        self.column_headers = ["ID", "优先级", "动作", "描述"]
        
        # 初始化数据
        self.acl_data = [
            {"id": "1001", "priority": "100", "action": "PERMIT", "description": "允许管理员访问"},
            {"id": "1002", "priority": "200", "action": "DENY", "description": "拒绝外部网络访问"},
            {"id": "1003", "priority": "300", "action": "PERMIT", "description": "允许内部网络访问"},
        ]
    
    def rowCount(self, parent=QModelIndex()):
        """返回行数"""
        return len(self.acl_data)
    
    def columnCount(self, parent=QModelIndex()):
        """返回列数"""
        return len(self.column_headers)
    
    def data(self, index, role=Qt.DisplayRole):
        """返回数据"""
        if not index.isValid():
            return None
        
        if role == Qt.DisplayRole:
            row = index.row()
            col = index.column()
            
            if col == 0:
                return self.acl_data[row]["id"]
            elif col == 1:
                return self.acl_data[row]["priority"]
            elif col == 2:
                return self.acl_data[row]["action"]
            elif col == 3:
                return self.acl_data[row]["description"]
        
        return None
    
    def headerData(self, section, orientation, role=Qt.DisplayRole):
        """返回表头数据"""
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.column_headers[section]
        
        return None
    
    def add_acl(self, acl_id, priority, action, description):
        """添加ACL规则"""
        self.beginInsertRows(QModelIndex(), len(self.acl_data), len(self.acl_data))
        self.acl_data.append({
            "id": acl_id,
            "priority": priority,
            "action": action,
            "description": description
        })
        self.endInsertRows()
        
        return True
    
    def remove_acl(self, row):
        """删除ACL规则"""
        if row < 0 or row >= len(self.acl_data):
            return False
        
        self.beginRemoveRows(QModelIndex(), row, row)
        del self.acl_data[row]
        self.endRemoveRows()
        
        return True
    
    def update_acl(self, row, acl_id, priority, action, description):
        """更新ACL规则"""
        if row < 0 or row >= len(self.acl_data):
            return False
        
        self.acl_data[row] = {
            "id": acl_id,
            "priority": priority,
            "action": action,
            "description": description
        }
        
        self.dataChanged.emit(self.index(row, 0), self.index(row, self.columnCount() - 1))
        return True 