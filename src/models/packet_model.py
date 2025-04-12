#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PySide6.QtCore import Qt, QAbstractTableModel, QModelIndex

class PacketCaptureModel(QAbstractTableModel):
    """数据包捕获模型"""
    
    def __init__(self, parent=None):
        """初始化"""
        super().__init__(parent)
        
        # 列名
        self.column_headers = ["序号", "测试用例名称", "更新时间"]
        
        # 数据包列表
        self.packets = []
    
    def rowCount(self, parent=QModelIndex()):
        """返回行数"""
        return len(self.packets)
    
    def columnCount(self, parent=QModelIndex()):
        """返回列数"""
        return len(self.column_headers)
    
    def data(self, index, role=Qt.DisplayRole):
        """返回数据"""
        if not index.isValid() or index.row() >= len(self.packets):
            return None
        
        if role == Qt.DisplayRole:
            packet = self.packets[index.row()]
            col = index.column()
            
            if col == 0:  # 序号
                return str(packet.get("index", ""))
            elif col == 1:  # 测试用例名称
                return packet.get("test_name", "")
            elif col == 2:  # 更新时间
                return packet.get("update_time", "")
        
        return None
    
    def headerData(self, section, orientation, role=Qt.DisplayRole):
        """返回表头数据"""
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.column_headers[section]
        
        return None
    
    def add_packet(self, packet):
        """添加数据包
        
        Args:
            packet: 数据包字典，包含index, timestamp, mac_address, length, type等字段
        """
        self.beginInsertRows(QModelIndex(), len(self.packets), len(self.packets))
        self.packets.append(packet)
        self.endInsertRows()
    
    def clear(self):
        """清空数据"""
        self.beginResetModel()
        self.packets.clear()
        self.endResetModel()
    
    def get_packet(self, row):
        """获取指定行的数据包
        
        Args:
            row: 行号
        
        Returns:
            dict: 数据包字典，如果行号无效则返回None
        """
        if 0 <= row < len(self.packets):
            return self.packets[row]
        
        return None
    
    def generate_test_data(self):
        """生成测试数据"""
        # 清空现有数据
        self.clear()
        
        # 添加测试数据
        test_packets = [
            {
                "index": 1,
                "test_name": "基础连接测试",
                "update_time": "2023-10-10 08:30:00"
            }
        ]
        
        for packet in test_packets:
            self.add_packet(packet)
        
        return len(test_packets)
    
    def generate_demo_data(self):
        """生成演示数据（比测试数据更丰富）"""
        # 清空现有数据
        self.clear()
        
        # 添加演示数据
        demo_packets = [
            {
                "index": 1,
                "test_name": "ARP请求测试",
                "update_time": "2023-10-12 10:12:35"
            },
            {
                "index": 2,
                "test_name": "ARP响应测试",
                "update_time": "2023-10-12 10:15:45"
            },
            {
                "index": 3,
                "test_name": "HTTP协议测试",
                "update_time": "2023-10-13 09:22:36"
            },
            {
                "index": 4,
                "test_name": "HTTP响应测试",
                "update_time": "2023-10-13 09:25:23"
            },
            {
                "index": 5,
                "test_name": "ICMP请求测试",
                "update_time": "2023-10-14 14:30:21"
            },
            {
                "index": 6,
                "test_name": "ICMP响应测试",
                "update_time": "2023-10-14 14:32:07"
            },
            {
                "index": 7,
                "test_name": "DNS查询测试",
                "update_time": "2023-10-15 16:18:45"
            },
            {
                "index": 8,
                "test_name": "广播测试",
                "update_time": "2023-10-15 16:25:12"
            }
        ]
        
        for packet in demo_packets:
            self.add_packet(packet)
        
        return len(demo_packets) 