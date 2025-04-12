# Pkjviz-py Poetry 使用指南

本项目使用 Poetry 进行依赖管理和打包。以下是使用说明。

## 安装 Poetry

如果尚未安装 Poetry，请首先安装：

```bash
# osx / linux / bashonwindows
curl -sSL https://install.python-poetry.org | python3 -

# windows powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
```

## 安装项目依赖

在项目根目录执行：

```bash
poetry install
```

## 运行项目

有两种方式运行项目：

### 1. 使用 Poetry 运行

```bash
poetry run pkjviz
```

### 2. 激活虚拟环境后运行

```bash
# 激活虚拟环境
poetry shell

# 然后运行
pkjviz

# 或直接运行
python run.py
```

## 添加新依赖

```bash
# 添加运行依赖
poetry add package-name

# 添加开发依赖
poetry add --group dev package-name
```

## 更新依赖

```bash
# 更新所有依赖
poetry update

# 更新特定依赖
poetry update package-name
```

## 构建项目

```bash
poetry build
```

## 虚拟环境管理

```bash
# 查看虚拟环境信息
poetry env info

# 列出所有虚拟环境
poetry env list

# 删除虚拟环境
poetry env remove python
```

## 导出依赖为 requirements.txt

```bash
poetry export -f requirements.txt --output requirements.txt
```

## 常见问题解决

### PySide6 平台插件问题

如果遇到 "could not find or load the Qt platform plugin" 错误，请尝试：

1. 确保使用 Poetry 虚拟环境：
   ```bash
   poetry shell
   ```

2. 在虚拟环境中重新安装 PySide6：
   ```bash
   poetry add PySide6@latest
   ```

3. 如果在 macOS 上，尝试：
   ```bash
   export QT_DEBUG_PLUGINS=1
   ```
   运行应用，查看详细错误信息。

4. 配置 Qt 插件路径：
   ```bash
   export QT_PLUGIN_PATH=$(poetry run python -c "import PySide6; print(PySide6.__path__[0] + '/Qt/plugins')")
   ``` 