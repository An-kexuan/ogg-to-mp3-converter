# OGG to MP3 Converter / OGG 转 MP3 转换器

A simple and efficient desktop application for converting OGG audio files to MP3 format. Built with Python, featuring an intuitive graphical user interface with support for batch conversion and drag-and-drop operations.

一个使用 Python 编写的简单、高效的 OGG 音频文件转换为 MP3 格式的桌面应用程序。具有直观的图形用户界面，支持批量转换和拖放操作。

## 🌟 Features / 特性

### Core Features / 核心功能
- **Bilingual Interface** - Switch between Chinese and English interface
- **直观的双语界面** - 支持中英文界面切换
- **Intuitive GUI** - Modern interface based on tkinter
- **直观的图形界面** - 基于 tkinter 开发的现代化界面
- **Batch Conversion** - Convert multiple OGG files at once
- **批量转换** - 支持一次性转换多个 OGG 文件
- **Drag & Drop Support** - Directly drag files to the program window
- **拖放支持** - 直接将文件拖放到程序窗口即可添加
- **Folder Scanning** - Automatically scan all OGG files in a folder
- **文件夹扫描** - 自动扫描文件夹内的所有 OGG 文件
- **Progress Display** - Real-time conversion progress and status
- **进度显示** - 实时显示转换进度和状态

### Advanced Features / 高级功能
- **Custom Output Directory** - Select any output location
- **自定义输出目录** - 支持选择任意输出位置
- **Cross-Platform Support** - Works on Windows, macOS, and Linux
- **跨平台支持** - 支持 Windows、macOS 和 Linux 系统
- **Error Handling** - Comprehensive error handling and user prompts
- **错误处理** - 完善的错误处理和用户提示
- **File Management** - Add, remove, and clear file lists easily
- **文件管理** - 轻松添加、删除和清空文件列表

## 📋 System Requirements / 系统要求

### Software Requirements / 软件要求
- **Python 3.6+** (Required)
- **Python 3.6+** (必需)
- **FFmpeg** (Must be installed and added to system PATH)
- **FFmpeg** (必须安装并添加到系统 PATH)

### Supported Formats / 支持的格式
- **Input**: OGG files
- **输入格式**: OGG 文件
- **Output**: MP3 files
- **输出格式**: MP3 文件

## 🚀 Quick Start / 快速开始

### 1. Install Dependencies / 安装依赖

```bash
# Clone the project / 克隆项目
git clone https://github.com/your-username/ogg-to-mp3-converter.git
cd ogg-to-mp3-converter

# Install Python dependencies / 安装 Python 依赖
pip install -r requirements.txt
```

### 2. Install FFmpeg / 安装 FFmpeg

#### Windows:
1. Download FFmpeg and extract to `C:\ffmpeg`
2. Add `C:\ffmpeg\bin` to system PATH environment variable

#### Windows 用户:
1. 下载 FFmpeg 并解压到 `C:\ffmpeg`
2. 将 `C:\ffmpeg\bin` 添加到系统 PATH 环境变量

#### macOS:
```bash
# Install using Homebrew / 使用 Homebrew 安装
brew install ffmpeg
```

#### Linux:
```bash
# Ubuntu/Debian
sudo apt update
sudo apt install ffmpeg

# CentOS/RHEL
sudo yum install ffmpeg

# Ubuntu/Debian 用户
sudo apt update
sudo apt install ffmpeg

# CentOS/RHEL 用户
sudo yum install ffmpeg
```

### 3. Run the Application / 运行程序

#### Method 1: Direct Python Script / 方法一：直接运行 Python 脚本
```bash
python ogg_to_mp3_converter.py
```

#### Method 2: Windows Batch File (Recommended) / 方法二：Windows 批处理文件（推荐）
Double-click `run.vbs` file to run the program silently in the background.
双击运行 `run.vbs` 文件，程序将在后台静默运行。

## 🎯 User Guide / 使用说明

### Interface Overview / 界面介绍

The program interface consists of the following main areas:
程序界面包含以下主要区域：

1. **Language Toggle** - Switch between Chinese and English
- **语言切换按钮** - 在中文和英文之间切换
2. **File Selection Area** - Add files, add folder, clear list buttons
- **文件选择区域** - 添加文件、添加文件夹、清空列表按钮
3. **Output Settings** - Select MP3 file output directory
- **输出设置** - 选择 MP3 文件的输出目录
4. **File List** - Display files to be converted, supports drag and drop
- **文件列表** - 显示待转换的文件列表，支持拖放操作
5. **Progress Control** - Progress bar, status information, and start conversion button
- **进度控制** - 进度条、状态信息和开始转换按钮

### Adding Files / 添加文件的方式

1. **Click "Add Files"** - Select individual or multiple OGG files
- **点击"添加文件"** - 选择单个或多个 OGG 文件
2. **Click "Add Folder"** - Automatically scan all OGG files in a folder
- **点击"添加文件夹"** - 自动扫描文件夹内的所有 OGG 文件
3. **Drag & Drop** - Drag OGG files directly to the file list area
- **拖放操作** - 直接将 OGG 文件拖放到文件列表区域
4. **Delete Files** - Select files and click "Delete Selected"
- **删除文件** - 选中文件后点击"删除选中"按钮

### Conversion Process / 转换流程

1. Add OGG files to convert
- 添加要转换的 OGG 文件
2. Select output directory (default is Desktop)
- 选择输出目录（默认为桌面）
3. Click "Start Conversion" button
- 点击"开始转换"按钮
4. Wait for conversion to complete and view results
- 等待转换完成，查看结果

## 📁 Project Structure / 项目结构

```
ogg-to-mp3-converter/
├── ogg_to_mp3_converter.py      # Main program file / 主程序文件
├── run.vbs                      # Windows startup script / Windows 启动脚本
├── requirements.txt             # Python dependencies / Python 依赖包列表
├── README.md                    # Project documentation / 项目说明文档
└── .gitignore                   # Git ignore file / Git 忽略文件
```

## 🔧 Dependencies / 依赖说明

### Python Package Dependencies / Python 包依赖
- `tkinter` - GUI framework (Python standard library)
- `tkinter` - 图形界面框架（Python 标准库）
- `pydub` - Audio processing library
- `pydub` - 音频处理库
- `pathlib` - Path operations (Python standard library)
- `pathlib` - 路径操作（Python 标准库）

### System Dependencies / 系统依赖
- `FFmpeg` - Audio codec tool (Required)
- `FFmpeg` - 音频编解码工具（必须安装）

## 🐛 Troubleshooting / 故障排除

### Common Issues / 常见问题

#### Q: FFmpeg errors during conversion
A: Ensure FFmpeg is correctly installed and added to system PATH.

#### Q: 转换时出现 FFmpeg 错误
A: 请确保 FFmpeg 已正确安装并添加到系统 PATH 环境变量中。

#### Q: Drag and drop doesn't work
A: Some systems may require additional dependencies. Try using the "Add Files" button instead.

#### Q: 拖放功能不工作
A: 在某些系统上可能需要安装额外的依赖包。请尝试使用"添加文件"按钮代替。

#### Q: Program won't start
A: Check if Python and all dependencies are properly installed.

#### Q: 程序无法启动
A: 检查 Python 和所有依赖包是否已正确安装。

#### Q: Converted MP3 files have no sound
A: This might be a source file format issue. Check if the original OGG file plays normally.

#### Q: 转换后的 MP3 文件没有声音
A: 可能是源文件格式问题，请检查原始 OGG 文件是否可正常播放。

#### Q: Language switching doesn't update all text
A: The program dynamically updates interface text. If some text remains unchanged, try restarting the application.

#### Q: 语言切换后部分文本未更新
A: 程序会动态更新界面文本。如果某些文本保持不变，请尝试重启应用程序。

### Debug Mode / 调试模式

If you need debugging information, you can enable debug output by modifying the main program file:
如果需要调试信息，可以修改主程序文件，启用调试输出：

```python
# Add at the beginning of the file / 在文件开头添加
import logging
logging.basicConfig(level=logging.DEBUG)
```

## 🤝 Contributing / 贡献

We welcome issues and pull requests!
欢迎提交 Issue 和 Pull Request！

### Development Setup / 开发环境设置

1. Fork the project
- Fork 项目
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
- 创建功能分支 (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
- 提交更改 (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
- 推送到分支 (`git push origin feature/amazing-feature`)
5. Create a Pull Request
- 创建 Pull Request

## 📄 License / 许可证

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 🙏 Acknowledgments / 致谢

- Thanks to [pydub](https://github.com/jiaaro/pydub) for audio processing capabilities
- 感谢 [pydub](https://github.com/jiaaro/pydub) 项目提供的音频处理功能
- Thanks to [FFmpeg](https://ffmpeg.org/) team for powerful multimedia processing tools
- 感谢 [FFmpeg](https://ffmpeg.org/) 团队开发了强大的多媒体处理工具
- Thanks to all contributors and users for their support
- 感谢所有贡献者和用户的支持

## 📞 Contact / 联系

For questions or suggestions, please contact us through:
如有问题或建议，请通过以下方式联系：
- Submit GitHub Issues
- 提交 GitHub Issue
- Send email to: 2695145381@qq.com
- 发送邮件至：2695145381@qq.com

---

**Note**: Please ensure compliance with relevant copyright laws and only convert audio files that you have legal rights to use.
**注意**: 请确保遵守相关版权法律，仅转换您拥有合法使用权的音频文件。