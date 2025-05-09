#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import Optional, List, Any, Union
from PySide6.QtCore import (
    QObject,
    Signal,
    QAbstractListModel,
    Qt,
    QModelIndex,
    QPersistentModelIndex,
)


class Device(QObject):
    """设备类"""

    # 设备状态常量
    STATUS_OFFLINE = 0
    STATUS_ONLINE = 1

    # 信号
    status_changed = Signal(int)

    def __init__(
        self,
        device_id: str,
        ip_address: str,
        name: Optional[str] = None,
        parent: Optional[QObject] = None,
    ) -> None:
        """初始化设备

        Args:
            device_id: 设备ID
            ip_address: IP地址
            name: 设备名称，如果为None则使用IP地址作为名称
            parent: 父对象
        """
        super().__init__(parent)

        self._id = device_id
        self._ip = ip_address
        self._name = name if name else f"设备{device_id}"
        self._status = self.STATUS_OFFLINE

    @property
    def id(self) -> str:
        """获取设备ID"""
        return self._id

    @property
    def ip_address(self) -> str:
        """获取IP地址"""
        return self._ip

    @property
    def name(self) -> str:
        """获取设备名称"""
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        """设置设备名称"""
        self._name = value

    @property
    def status(self) -> int:
        """获取设备状态"""
        return self._status

    @status.setter
    def status(self, value: int) -> None:
        """设置设备状态"""
        if self._status != value:
            self._status = value
            self.status_changed.emit(value)

    def __str__(self) -> str:
        """字符串表示"""
        return f"{self._name} ({self._ip})"


class DeviceListModel(QAbstractListModel):
    """设备列表模型"""

    # 信号
    device_added = Signal(object)  # Device
    device_removed = Signal(str)  # IP地址

    def __init__(self, parent: Optional[QObject] = None) -> None:
        """初始化设备列表模型"""
        super().__init__(parent)

        # 设备列表
        self._devices: List[Device] = []

    def rowCount(
        self, parent: Union[QModelIndex, QPersistentModelIndex] = QModelIndex()
    ) -> int:
        """返回行数"""
        return len(self._devices)

    def data(
        self,
        index: Union[QModelIndex, QPersistentModelIndex],
        role: int = Qt.ItemDataRole.DisplayRole,
    ) -> Optional[Any]:
        """返回数据"""
        if not index.isValid() or index.row() >= len(self._devices):
            return None

        device = self._devices[index.row()]

        if role == Qt.ItemDataRole.DisplayRole:
            return str(device)
        elif role == Qt.ItemDataRole.UserRole:
            return device

        return None

    def add_device(self, device: Device) -> bool:
        """添加设备

        Args:
            device: 设备对象

        Returns:
            bool: 是否成功添加
        """
        # 检查是否已存在
        for existing_device in self._devices:
            if existing_device.ip_address == device.ip_address:
                return False

        # 添加设备
        self.beginInsertRows(QModelIndex(), len(self._devices), len(self._devices))
        self._devices.append(device)
        self.endInsertRows()

        # 发送信号
        self.device_added.emit(device)

        return True

    def remove_device(self, ip_address: str) -> bool:
        """删除设备

        Args:
            ip_address: 设备IP地址

        Returns:
            bool: 是否成功删除
        """
        for i, device in enumerate(self._devices):
            if device.ip_address == ip_address:
                self.beginRemoveRows(QModelIndex(), i, i)
                removed_device = self._devices.pop(i)
                self.endRemoveRows()

                # 发送信号
                self.device_removed.emit(removed_device.ip_address)

                return True

        return False

    def get_device(self, ip_address: str) -> Optional[Device]:
        """根据IP地址获取设备

        Args:
            ip_address: 设备IP地址

        Returns:
            Device: 设备对象，如果不存在则返回None
        """
        for device in self._devices:
            if device.ip_address == ip_address:
                return device

        return None

    def clear(self) -> None:
        """清空设备列表"""
        self.beginResetModel()
        self._devices.clear()
        self.endResetModel()

    def get_all_devices(self) -> List[Device]:
        """获取所有设备"""
        return list(self._devices)

    def scan_devices(self) -> int:
        """扫描网络设备

        注意：这里只是模拟扫描，实际应用中应该实现真正的网络扫描
        """
        # 模拟发现的设备
        devices = [
            Device("1", "192.168.1.1", "设备1"),
            Device("2", "192.168.1.2", "设备2"),
            Device("3", "192.168.1.3", "设备3"),
        ]

        # 清空现有设备
        self.clear()

        # 添加设备
        for device in devices:
            self.add_device(device)

        return len(devices)
