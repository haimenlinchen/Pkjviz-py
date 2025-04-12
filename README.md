# Pkjviz-ui-py

基于PyQt5的Pkjviz可视化界面，提供仿Spyder IDE的界面布局和交互。支持离线和在线两种模式。

## 功能特点

- 类似IDE的界面布局
- 支持离线和在线两种工作模式
- 文件浏览和编辑
- 诊断结果显示
- 设备管理和数据包发送
- 数据包捕获和分析
- 控制台输出

## 安装依赖

```bash
pip install -r requirements.txt
```

## 运行程序

```bash
cd /path/to/Pkjviz-ui-py
python run.py
```

## 工作模式

### 离线模式
- 提供脚本编辑和诊断功能
- 用于开发和测试网络协议脚本

### 在线模式
- 支持网络设备管理
- 提供数据包发送和捕获功能
- 实时分析网络流量

## 项目结构

```
Pkjviz-ui-py/
├── src/
│   ├── controllers/      # 控制器
│   │   ├── diagnostic_controller.py
│   │   └── packet_sender_controller.py
│   ├── models/           # 数据模型
│   │   ├── acl_model.py
│   │   ├── device_model.py
│   │   ├── diagnostic_model.py
│   │   └── packet_model.py
│   ├── ui/               # UI文件
│   │   ├── main_window.ui
│   │   └── packet_sender.ui
│   └── main.py           # 主程序入口
├── tests/                # 测试
├── docs/                 # 文档
├── requirements.txt      # 依赖
└── README.md             # 自述文件
```

## 开发说明

### UI文件

UI文件使用Qt Designer设计，保存在`src/ui`目录下。

### 数据模型

- 诊断结果模型 (DiagnosticResult)
- ACL表格模型 (ACLTableModel)
- 设备列表模型 (DeviceListModel)
- 数据包捕获模型 (PacketCaptureModel)

### 控制器

- 诊断结果控制器 (DiagnosticController)
- 数据包发送控制器 (PacketSenderController)

## 使用说明

1. 启动程序后，默认为离线模式
2. 点击"在线"按钮切换到在线模式
3. 在设备列表中选择设备
4. 点击"发包"按钮打开数据包发送工具
5. 在数据包发送工具中设置数据包内容并发送

## 许可证

MIT # Pkjviz-py
