# OGG 转 MP3 转换器

一个使用 Python 编写的简单、高效的 OGG 音频文件转换为 MP3 格式的桌面应用程序。具有直观的图形用户界面，支持批量转换和拖放操作。

## 🌟 特性

- **直观的图形界面** - 基于 tkinter 开发的现代化界面
- **批量转换** - 支持一次性转换多个 OGG 文件
- **拖放支持** - 直接将文件拖放到程序窗口即可添加
- **文件夹扫描** - 自动扫描文件夹内的所有 OGG 文件
- **进度显示** - 实时显示转换进度和状态
- **自定义输出目录** - 支持选择任意输出位置
- **跨平台支持** - 支持 Windows、macOS 和 Linux 系统
- **错误处理** - 完善的错误处理和用户提示

## 📋 系统要求

- **Python 3.6+**
- **FFmpeg** (必须安装并添加到系统 PATH)
- **支持的音频格式**: OGG → MP3

## 🚀 快速开始

### 1. 安装依赖

```bash
# 克隆项目
git clone https://github.com/your-username/ogg-to-mp3-converter.git
cd ogg-to-mp3-converter

# 安装 Python 依赖
pip install -r requirements.txt
```

### 2. 安装 FFmpeg

#### Windows:
1. 下载 FFmpeg 并解压到 `C:\\ffmpeg`
2. 将 `C:\\ffmpeg\\bin` 添加到系统 PATH 环境变量

#### macOS:
```bash
# 使用 Homebrew 安装
brew install ffmpeg
```

#### Linux:
```bash
# Ubuntu/Debian
sudo apt update
sudo apt install ffmpeg

# CentOS/RHEL
sudo yum install ffmpeg
```

### 3. 运行程序

#### 方法一：直接运行 Python 脚本
```bash
python ogg_to_mp3_converter_fixed.py
```

#### 方法二：Windows 用户使用批处理文件（推荐）
双击运行 `运行程序_修复版.vbs` 文件，程序将在后台静默运行。

## 🎯 使用说明

### 界面介绍

程序界面包含以下主要区域：

1. **文件选择区域** - 添加文件、添加文件夹、清空列表按钮
2. **输出设置** - 选择 MP3 文件的输出目录
3. **文件列表** - 显示待转换的文件列表，支持拖放操作
4. **进度控制** - 进度条、状态信息和开始转换按钮

### 添加文件的方式

1. **点击添加文件** - 选择单个或多个 OGG 文件
2. **点击添加文件夹** - 自动扫描文件夹内的所有 OGG 文件
3. **拖放操作** - 直接将 OGG 文件拖放到文件列表区域
4. **删除文件** - 选中文件后点击"删除选中"按钮

### 转换流程

1. 添加要转换的 OGG 文件
2. 选择输出目录（默认为桌面）
3. 点击"开始转换"按钮
4. 等待转换完成，查看结果

## 📁 项目结构

```
ogg-to-mp3-converter/
├── ogg_to_mp3_converter_fixed.py  # 主程序文件
├── 运行程序_修复版.vbs              # Windows 启动脚本
├── requirements.txt               # Python 依赖包列表
├── README.md                     # 项目说明文档
└── .gitignore                    # Git 忽略文件
```

## 🔧 依赖说明

### Python 包依赖
- `tkinter` - 图形界面框架（Python 标准库）
- `pydub` - 音频处理库
- `pathlib` - 路径操作（Python 标准库）

### 系统依赖
- `FFmpeg` - 音频编解码工具（必须安装）

## 🐛 故障排除

### 常见问题

#### Q: 转换时出现 FFmpeg 错误
A: 请确保 FFmpeg 已正确安装并添加到系统 PATH 环境变量中。

#### Q: 拖放功能不工作
A: 在某些系统上可能需要安装额外的依赖包。请尝试使用"添加文件"按钮代替。

#### Q: 程序无法启动
A: 检查 Python 和所有依赖包是否已正确安装。

#### Q: 转换后的 MP3 文件没有声音
A: 可能是源文件格式问题，请检查原始 OGG 文件是否可正常播放。

### 调试模式

如果需要调试信息，可以修改主程序文件，启用调试输出：

```python
# 在文件开头添加
import logging
logging.basicConfig(level=logging.DEBUG)
```

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

### 开发环境设置

1. Fork 项目
2. 创建功能分支 (`git checkout -b feature/amazing-feature`)
3. 提交更改 (`git commit -m 'Add some amazing feature'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 创建 Pull Request

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 🙏 致谢

- 感谢 [pydub](https://github.com/jiaaro/pydub) 项目提供的音频处理功能
- 感谢 [FFmpeg](https://ffmpeg.org/) 团队开发了强大的多媒体处理工具
- 感谢所有贡献者和用户的支持

## 📞 联系

如有问题或建议，请通过以下方式联系：
- 提交 GitHub Issue
- 发送邮件至：your-email@example.com

---

**注意**: 请确保遵守相关版权法律，仅转换您拥有合法使用权的音频文件。