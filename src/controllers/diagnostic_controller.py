#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PySide6.QtWidgets import QTreeWidgetItem
from PySide6.QtCore import Qt

class DiagnosticController:
    """诊断结果控制器类"""
    
    def __init__(self, diagnostic_model, view):
        """初始化
        
        Args:
            diagnostic_model: 诊断结果数据模型
            view: 主窗口视图对象
        """
        self.model = diagnostic_model
        self.view = view
        
        # 连接信号
        self.model.result_changed.connect(self.update_view)
        
        # 初始化视图
        self.update_view()
    
    def update_view(self):
        """更新视图"""
        # 更新诊断代码和行动
        self.view.ui.diagCodeLabel.setText(self.model.code)
        self.view.ui.diagActionLabel.setText(self.model.action)
        
        # 更新表名和表描述
        self.view.ui.tableNameLabel.setText(self.model.table_name)
        self.view.ui.tableDescContentLabel.setText(self.model.table_desc)
        
        # 更新字段列表
        self.update_fields()
    
    def update_fields(self):
        """更新字段列表"""
        # 清空树控件
        self.view.ui.fieldTreeWidget.clear()
        
        # 添加字段
        for field in self.model.fields:
            item = QTreeWidgetItem()
            item.setText(0, field["name"])
            item.setText(1, field["description"])
            item.setText(2, field["value"])
            
            self.view.ui.fieldTreeWidget.addTopLevelItem(item)
        
        # 调整列宽
        for i in range(3):
            self.view.ui.fieldTreeWidget.resizeColumnToContents(i)
    
    def update_diagnostic(self, code, action, table_name, table_desc, fields):
        """更新诊断结果
        
        Args:
            code: 诊断代码
            action: 诊断动作
            table_name: 表名
            table_desc: 表描述
            fields: 字段列表
        """
        # 更新模型数据
        self.model.code = code
        self.model.action = action
        self.model.table_name = table_name
        self.model.table_desc = table_desc
        
        # 清空原有字段
        self.model._fields = []
        
        # 添加新字段
        for field in fields:
            self.model.add_field(field["name"], field["description"], field["value"])
    
    def clear(self):
        """清空诊断结果"""
        self.model.clear() 