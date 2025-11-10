import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os
import threading
from pathlib import Path
import pydub
from pydub import AudioSegment
import tempfile
import shutil
import subprocess

class OGGToMP3Converter:
    def __init__(self, root):
        self.root = root
        
        # 语言设置
        self.language = "chinese"  # 默认中文
        
        # 语言字典
        self.language_dict = {
            "chinese": {
                "title": "OGG转MP3转换器",
                "file_selection": "文件选择",
                "add_files": "添加文件",
                "add_folder": "添加文件夹",
                "clear_list": "清空列表",
                "output_settings": "输出设置",
                "output_directory": "输出目录:",
                "browse": "浏览",
                "files_to_convert": "待转换文件",
                "delete_selected": "删除选中",
                "start_conversion": "开始转换",
                "ready": "准备就绪",
                "drag_drop_hint": "拖放OGG文件到这里或使用上方按钮添加文件",
                "no_files_warning": "请先添加要转换的OGG文件",
                "invalid_output_error": "请选择有效的输出目录",
                "conversion_complete": "转换完成",
                "exit_confirm": "确定要退出程序吗？",
                "language_button": "English"
            },
            "english": {
                "title": "OGG to MP3 Converter",
                "file_selection": "File Selection",
                "add_files": "Add Files",
                "add_folder": "Add Folder",
                "clear_list": "Clear List",
                "output_settings": "Output Settings",
                "output_directory": "Output Directory:",
                "browse": "Browse",
                "files_to_convert": "Files to Convert",
                "delete_selected": "Delete Selected",
                "start_conversion": "Start Conversion",
                "ready": "Ready",
                "drag_drop_hint": "Drag and drop OGG files here or use buttons above",
                "no_files_warning": "Please add OGG files to convert first",
                "invalid_output_error": "Please select a valid output directory",
                "conversion_complete": "Conversion Complete",
                "exit_confirm": "Are you sure you want to exit?",
                "language_button": "中文"
            }
        }
        
        self.set_title()
        # 增大窗口并固定大小
        self.root.geometry("900x700")  # 进一步增大窗口尺寸
        self.root.resizable(False, False)
        # 仅禁用最大化按钮，不设置为工具窗口（避免失去焦点关闭）
        self.root.attributes('-toolwindow', 0)  # 设置为0，保持正常窗口行为
        # 设置窗口图标和初始位置
        self.root.eval('tk::PlaceWindow . center')
        # 防止程序在失去焦点时关闭
        self.root.wm_attributes("-topmost", 0)  # 确保不是总在最前
        
        # 设置样式
        self.setup_styles()
        
        # 创建界面
        self.create_widgets()
        
        # 文件列表
        self.files_to_convert = []
        
        # 拖放状态
        self.drag_drop_active = False
        
        # 支持拖放
        self.setup_drag_drop()
        
    def set_title(self):
        """设置窗口标题"""
        self.root.title(self.get_text("title"))
    
    def get_text(self, key):
        """获取对应语言的文本"""
        return self.language_dict[self.language].get(key, key)
    
    def switch_language(self):
        """切换语言"""
        if self.language == "chinese":
            self.language = "english"
        else:
            self.language = "chinese"
        
        # 更新界面文本
        self.update_ui_text()
        
        # 更新语言按钮文本
        self.language_button.config(text=self.get_text("language_button"))
    
    def update_ui_text(self):
        """更新界面所有文本"""
        # 更新标题
        self.set_title()
        
        # 更新各个组件文本
        self.title_label.config(text=self.get_text("title"))
        self.file_frame.config(text=self.get_text("file_selection"))
        self.add_button.config(text=self.get_text("add_files"))
        self.add_folder_button.config(text=self.get_text("add_folder"))
        self.clear_button.config(text=self.get_text("clear_list"))
        self.output_frame.config(text=self.get_text("output_settings"))
        self.output_label.config(text=self.get_text("output_directory"))
        self.browse_button.config(text=self.get_text("browse"))
        self.list_frame.config(text=self.get_text("files_to_convert"))
        self.delete_button.config(text=self.get_text("delete_selected"))
        self.convert_button.config(text=self.get_text("start_conversion"))
        
        # 更新状态
        if self.status_var.get() not in [self.get_text("ready"), "", None]:
            # 只更新默认状态，保留操作状态
            if self.status_var.get() in [self.language_dict["chinese"]["ready"], self.language_dict["english"]["ready"]]:
                self.status_var.set(self.get_text("ready"))
        
    def set_title(self):
        """设置窗口标题"""
        self.root.title(self.get_text("title"))
    
    def get_text(self, key):
        """获取对应语言的文本"""
        return self.language_dict[self.language].get(key, key)
    
    def switch_language(self):
        """切换语言"""
        if self.language == "chinese":
            self.language = "english"
        else:
            self.language = "chinese"
        
        # 更新界面文本
        self.update_ui_text()
        
        # 更新语言按钮文本
        self.language_button.config(text=self.get_text("language_button"))
    
    def update_ui_text(self):
        """更新界面所有文本"""
        # 更新标题
        self.set_title()
        
        # 更新各个组件文本
        self.title_label.config(text=self.get_text("title"))
        self.file_frame.config(text=self.get_text("file_selection"))
        self.add_button.config(text=self.get_text("add_files"))
        self.add_folder_button.config(text=self.get_text("add_folder"))
        self.clear_button.config(text=self.get_text("clear_list"))
        self.output_frame.config(text=self.get_text("output_settings"))
        self.output_label.config(text=self.get_text("output_directory"))
        self.browse_button.config(text=self.get_text("browse"))
        self.list_frame.config(text=self.get_text("files_to_convert"))
        self.delete_button.config(text=self.get_text("delete_selected"))
        self.convert_button.config(text=self.get_text("start_conversion"))
        
        # 更新状态
        if self.status_var.get() not in [self.get_text("ready"), "", None]:
            # 只更新默认状态，保留操作状态
            if self.status_var.get() in [self.language_dict["chinese"]["ready"], self.language_dict["english"]["ready"]]:
                self.status_var.set(self.get_text("ready"))
        
    def setup_styles(self):
        """设置界面样式"""
        style = ttk.Style()
        style.theme_use('clam')
        
        # 配置样式
        style.configure('Title.TLabel', font=('Arial', 16, 'bold'))
        style.configure('Subtitle.TLabel', font=('Arial', 12))
        style.configure('Action.TButton', font=('Arial', 10))
        style.configure('Language.TButton', font=('Arial', 9))
        style.configure('Language.TButton', font=('Arial', 9))
        
    def create_widgets(self):
        """创建界面组件"""
        # 主框架
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # 标题栏框架
        title_frame = ttk.Frame(main_frame)
        title_frame.pack(fill=tk.X, pady=(0, 20))
        
        # 标题
        self.title_label = ttk.Label(title_frame, text=self.get_text("title"), style='Title.TLabel')
        self.title_label.pack(side=tk.LEFT)
        
        # 语言切换按钮
        self.language_button = ttk.Button(title_frame, text=self.get_text("language_button"), 
                                         command=self.switch_language, style='Language.TButton')
        self.language_button.pack(side=tk.RIGHT, padx=(10, 0))
        
        # 文件选择区域
        self.file_frame = ttk.LabelFrame(main_frame, text=self.get_text("file_selection"), padding="10")
        self.file_frame.pack(fill=tk.X, pady=(0, 10))
        
        # 添加文件按钮
        self.add_button = ttk.Button(self.file_frame, text=self.get_text("add_files"), command=self.add_files, style='Action.TButton')
        self.add_button.pack(side=tk.LEFT, padx=(0, 10))
        
        # 添加文件夹按钮
        self.add_folder_button = ttk.Button(self.file_frame, text=self.get_text("add_folder"), command=self.add_folder, style='Action.TButton')
        self.add_folder_button.pack(side=tk.LEFT, padx=(0, 10))
        
        # 清空列表按钮
        self.clear_button = ttk.Button(self.file_frame, text=self.get_text("clear_list"), command=self.clear_files, style='Action.TButton')
        self.clear_button.pack(side=tk.LEFT)
        
        # 输出目录选择
        self.output_frame = ttk.LabelFrame(main_frame, text=self.get_text("output_settings"), padding="10")
        self.output_frame.pack(fill=tk.X, pady=(0, 10))
        
        output_select_frame = ttk.Frame(self.output_frame)
        output_select_frame.pack(fill=tk.X)
        
        self.output_var = tk.StringVar(value=os.path.expanduser("~/Desktop"))
        
        self.output_label = ttk.Label(output_select_frame, text=self.get_text("output_directory"))
        self.output_label.pack(side=tk.LEFT)
        
        output_entry = ttk.Entry(output_select_frame, textvariable=self.output_var, width=50)
        output_entry.pack(side=tk.LEFT, padx=(10, 10), fill=tk.X, expand=True)
        
        self.browse_button = ttk.Button(output_select_frame, text=self.get_text("browse"), command=self.browse_output, style='Action.TButton')
        self.browse_button.pack(side=tk.RIGHT)
        
        # 文件列表区域
        self.list_frame = ttk.LabelFrame(main_frame, text=self.get_text("files_to_convert"), padding="10")
        self.list_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        # 创建列表框和滚动条
        listbox_frame = ttk.Frame(self.list_frame)
        listbox_frame.pack(fill=tk.BOTH, expand=True)
        
        self.listbox = tk.Listbox(listbox_frame, selectmode=tk.EXTENDED)
        scrollbar = ttk.Scrollbar(listbox_frame, orient=tk.VERTICAL, command=self.listbox.yview)
        self.listbox.configure(yscrollcommand=scrollbar.set)
        
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # 删除选中文件按钮
        self.delete_button = ttk.Button(self.list_frame, text=self.get_text("delete_selected"), command=self.delete_selected, style='Action.TButton')
        self.delete_button.pack(pady=(10, 0))
        
        # 转换控制区域
        control_frame = ttk.Frame(main_frame)
        control_frame.pack(fill=tk.X, pady=(0, 10))
        
        # 进度条
        self.progress = ttk.Progressbar(control_frame, mode='determinate')
        self.progress.pack(fill=tk.X, pady=(0, 10))
        
        # 状态标签
        self.status_var = tk.StringVar(value=self.get_text("ready"))
        status_label = ttk.Label(control_frame, textvariable=self.status_var)
        status_label.pack()
        
        # 转换按钮
        self.convert_button = ttk.Button(control_frame, text=self.get_text("start_conversion"), command=self.start_conversion, style='Action.TButton')
        self.convert_button.pack(pady=(10, 0))
        
    def setup_drag_drop(self):
        """设置拖放支持 - 修复版"""
        import platform
        
        def handle_drop_wrapper(files):
            """处理拖放文件的包装函数 - 修复版"""
            added_files = []
            skipped_files = []
            
            for file in files:
                if file.strip():
                    # 处理Windows拖放格式
                    file_path = file.strip()
                    
                    # 处理花括号格式 {file1} {file2}
                    if file_path.startswith('{') and file_path.endswith('}'):
                        file_path = file_path[1:-1]
                    
                    # 处理可能的引号
                    file_path = file_path.strip('"')
                    
                    # 调试信息：打印文件路径
                    print(f"拖放文件路径: {file_path}")
                    
                    if self.add_file_to_list(file_path):
                        added_files.append(os.path.basename(file_path))
                    else:
                        skipped_files.append(os.path.basename(file_path))
            
            if added_files:
                if self.language == "chinese":
                    self.update_status(f"已通过拖放添加 {len(added_files)} 个OGG文件")
                else:
                    self.update_status(f"Added {len(added_files)} OGG files via drag and drop")
            elif skipped_files and files:
                # 显示更详细的错误信息
                if not any(f.lower().endswith('.ogg') for f in files):
                    if self.language == "chinese":
                        self.update_status("拖放的文件不是OGG格式")
                    else:
                        self.update_status("Dropped files are not in OGG format")
                else:
                    if self.language == "chinese":
                        self.update_status(f"文件无法添加: {', '.join(skipped_files)}")
                    else:
                        self.update_status(f"Files cannot be added: {', '.join(skipped_files)}")
        
        # 确保列表框有文件时状态正确
        def update_listbox_state():
            if self.listbox.size() > 0 and self.listbox.get(0) in [self.get_text("drag_drop_hint"), "拖放OGG文件到这里或使用上方按钮添加文件", "Drag and drop OGG files here or use buttons above"]:
                self.listbox.delete(0)
                self.listbox.config(fg='black')
        
        # 为列表框添加拖放提示
        if self.listbox.size() == 0:
            self.listbox.insert(tk.END, self.get_text("drag_drop_hint"))
            self.listbox.config(fg='gray')
            
            def on_first_click(event):
                # 清除提示文本
                update_listbox_state()
            
            self.listbox.bind('<Button-1>', on_first_click)
        
        if platform.system() == "Windows":
            # Windows系统使用tkinterdnd2库
            try:
                from tkinterdnd2 import DND_FILES, TkinterDnD
                
                def handle_drop(event):
                    # 解析拖放数据 - Windows系统可能有特殊格式
                    files_data = event.data
                    
                    # 调试：打印原始拖放数据
                    print(f"原始拖放数据: {files_data}")
                    
                    # 使用正则表达式来更好地处理Windows拖放格式
                    import re
                    
                    # 匹配花括号中的文件路径
                    pattern = r'\{([^}]+)\}'  # 匹配 {内容} 格式
                    matches = re.findall(pattern, files_data)
                    
                    if matches:
                        # 花括号格式的文件
                        files = matches
                        print(f"使用花括号解析: {files}")
                    else:
                        # 普通空格分隔格式
                        files = files_data.split()
                        # 尝试清理路径中的花括号和引号
                        files = [f.strip('{}"') for f in files if f.strip()]
                        print(f"使用空格分隔解析: {files}")
                    
                    # 进一步清理每个文件路径
                    files = [f.strip() for f in files if f.strip()]
                    
                    # 调试：打印解析后的文件路径
                    print(f"最终解析后的文件: {files}")
                    
                    update_listbox_state()
                    handle_drop_wrapper(files)
                
                # 注册拖放到整个窗口和列表框
                self.root.drop_target_register(DND_FILES)
                self.root.dnd_bind('<<Drop>>', handle_drop)
                self.listbox.drop_target_register(DND_FILES)
                self.listbox.dnd_bind('<<Drop>>', handle_drop)
                
                # 添加拖放视觉反馈
                def on_drag_enter(event):
                    self.listbox.config(bg='lightblue')
                    self.drag_drop_active = True
                
                def on_drag_leave(event):
                    self.listbox.config(bg='white')
                    self.drag_drop_active = False
                
                self.listbox.bind('<Enter>', on_drag_enter)
                self.listbox.bind('<Leave>', on_drag_leave)
                
            except ImportError:
                self.setup_fallback_drag_drop()
        else:
            self.setup_fallback_drag_drop()
    
    def setup_fallback_drag_drop(self):
        """备用拖放方案 - 提供视觉反馈和文件选择"""
        def on_drag_enter(event):
            self.listbox.config(bg='lightblue')
            self.drag_drop_active = True
        
        def on_drag_leave(event):
            self.listbox.config(bg='white')
            self.drag_drop_active = False
        
        def on_drop(event):
            self.listbox.config(bg='white')
            self.drag_drop_active = False
            
            # 延迟显示文件对话框，避免拖放和点击冲突
            self.root.after(100, self.show_file_dialog)
        
        # 绑定拖放事件
        self.listbox.bind('<Enter>', on_drag_enter)
        self.listbox.bind('<Leave>', on_drag_leave)
        
        # 为整个窗口添加拖放支持
        self.root.bind('<ButtonRelease-1>', on_drop)
    
    def show_file_dialog(self):
        """显示文件选择对话框作为拖放的备用方案"""
        files = filedialog.askopenfilenames(
            title="选择OGG文件",
            filetypes=[("OGG音频文件", "*.ogg"), ("所有文件", "*.*")]
        )
        if files:
            for file in files:
                self.add_file_to_list(file)
            self.update_status(f"已添加 {len(files)} 个文件")
        
    def add_files(self):
        """添加文件"""
        files = filedialog.askopenfilenames(
            title="选择OGG文件",
            filetypes=[("OGG音频文件", "*.ogg"), ("所有文件", "*.*")]
        )
        for file in files:
            self.add_file_to_list(file)
    
    def add_folder(self):
        """添加文件夹"""
        folder = filedialog.askdirectory(title="选择包含OGG文件的文件夹")
        if folder:
            for root, dirs, files in os.walk(folder):
                for file in files:
                    if file.lower().endswith('.ogg'):
                        file_path = os.path.join(root, file)
                        self.add_file_to_list(file_path)
    
    def add_file_to_list(self, file_path):
        """添加文件到列表"""
        # 清理文件路径，特别是从拖放获取的路径
        original_path = file_path
        file_path = file_path.strip().strip('{}').strip('"')
        
        # 调试信息
        print(f"添加文件 - 原始路径: {original_path}")
        print(f"添加文件 - 清理后路径: {file_path}")
        print(f"文件存在: {os.path.isfile(file_path)}")
        print(f"是OGG文件: {file_path.lower().endswith('.ogg') if file_path else False}")
        
        if file_path and os.path.isfile(file_path):
            if file_path.lower().endswith('.ogg'):
                if file_path not in self.files_to_convert:
                    self.files_to_convert.append(file_path)
                    filename = os.path.basename(file_path)
                    
                    # 确保列表框状态正确
                    if self.listbox.size() == 1 and self.listbox.get(0) in [self.get_text("drag_drop_hint"), "拖放OGG文件到这里或使用上方按钮添加文件", "Drag and drop OGG files here or use buttons above"]:
                        self.listbox.delete(0)
                        self.listbox.config(fg='black')
                    
                    self.listbox.insert(tk.END, filename)
                    if self.language == "chinese":
                        self.update_status(f"已添加: {filename}")
                    else:
                        self.update_status(f"Added: {filename}")
                    return True
                else:
                    print("文件已在列表中")
                    return False
            else:
                print("文件不是OGG格式")
                return False
        else:
            print("文件不存在或路径无效")
            return False
    
    def clear_files(self):
        """清空文件列表"""
        self.files_to_convert.clear()
        self.listbox.delete(0, tk.END)
        if self.language == "chinese":
            self.update_status("文件列表已清空")
        else:
            self.update_status("File list cleared")
    
    def delete_selected(self):
        """删除选中的文件"""
        selected = self.listbox.curselection()
        for index in reversed(selected):
            self.files_to_convert.pop(index)
            self.listbox.delete(index)
        if self.language == "chinese":
            self.update_status(f"删除了 {len(selected)} 个文件")
        else:
            self.update_status(f"Deleted {len(selected)} files")
    
    def browse_output(self):
        """选择输出目录"""
        directory = filedialog.askdirectory(title="选择输出目录")
        if directory:
            self.output_var.set(directory)
    
    def update_status(self, message):
        """更新状态信息"""
        self.status_var.set(message)
        self.root.update_idletasks()
    
    def start_conversion(self):
        """开始转换"""
        if not self.files_to_convert:
            messagebox.showwarning("警告", "请先添加要转换的OGG文件")
            return
        
        output_dir = self.output_var.get()
        if not output_dir or not os.path.isdir(output_dir):
            messagebox.showerror("错误", "请选择有效的输出目录")
            return
        
        # 在新线程中运行转换
        thread = threading.Thread(target=self.convert_files, args=(output_dir,))
        thread.daemon = True
        thread.start()
    
    def convert_files(self, output_dir):
        """转换文件"""
        total_files = len(self.files_to_convert)
        self.progress['maximum'] = total_files
        
        success_count = 0
        error_count = 0
        
        # 设置环境变量，防止FFmpeg弹出控制台窗口
        import os
        env = os.environ.copy()
        env['FFREPORT'] = 'file=ffreport.log:level=error'
        
        for i, input_file in enumerate(self.files_to_convert):
            try:
                self.update_status(f"正在转换: {os.path.basename(input_file)} ({i+1}/{total_files})")
                
                # 构建输出文件路径
                filename = os.path.splitext(os.path.basename(input_file))[0] + ".mp3"
                output_file = os.path.join(output_dir, filename)
                
                # 转换OGG到MP3 - 使用subprocess直接调用ffmpeg，避免控制台窗口
                import subprocess
                import sys
                
                # 使用subprocess.Popen的静默模式
                ffmpeg_cmd = [
                    'ffmpeg',
                    '-i', input_file,
                    '-acodec', 'libmp3lame',
                    '-b:a', '192k',
                    '-y',  # 覆盖输出文件
                    output_file
                ]
                
                # 启动进程，不显示控制台窗口
                if sys.platform == "win32":
                    startupinfo = subprocess.STARTUPINFO()
                    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
                    startupinfo.wShowWindow = 0  # 隐藏窗口
                    
                    process = subprocess.Popen(
                        ffmpeg_cmd,
                        stdout=subprocess.DEVNULL,
                        stderr=subprocess.DEVNULL,
                        startupinfo=startupinfo,
                        env=env
                    )
                else:
                    process = subprocess.Popen(
                        ffmpeg_cmd,
                        stdout=subprocess.DEVNULL,
                        stderr=subprocess.DEVNULL,
                        env=env
                    )
                
                # 等待进程完成
                process.wait()
                
                if process.returncode == 0:
                    success_count += 1
                else:
                    raise Exception(f"FFmpeg转换失败，返回码: {process.returncode}")
                
                self.root.after(0, lambda: self.progress.step(1))
                
            except Exception as e:
                error_count += 1
                error_msg = f"转换失败: {os.path.basename(input_file)} - {str(e)}"
                self.root.after(0, lambda msg=error_msg: self.update_status(msg))
        
        # 显示转换结果
        result_msg = f"转换完成! 成功: {success_count}, 失败: {error_count}"
        self.root.after(0, lambda: self.show_conversion_result(result_msg))
    
    def show_conversion_result(self, message):
        """显示转换结果"""
        self.update_status(message)
        messagebox.showinfo("转换完成", message)
        self.progress['value'] = 0

def check_dependencies():
    """检查必要的依赖包"""
    missing_deps = []
    
    try:
        import pydub
    except ImportError:
        missing_deps.append("pydub")
    
    try:
        import tkinter
    except ImportError:
        missing_deps.append("tkinter")
    
    return missing_deps

def show_error_dialog(message):
    """显示错误对话框（无控制台窗口时使用）"""
    try:
        import tkinter as tk
        from tkinter import messagebox
        root = tk.Tk()
        root.withdraw()  # 隐藏主窗口
        messagebox.showerror("错误", message)
        root.destroy()
    except:
        # 如果GUI无法显示，尝试使用其他方式
        try:
            import ctypes
            ctypes.windll.user32.MessageBoxW(0, message, "错误", 0)
        except:
            pass

def main():
    """主函数"""
    # 检查依赖
    missing_deps = check_dependencies()
    if missing_deps:
        deps_str = ', '.join(missing_deps)
        error_msg = "缺少必要的依赖包: " + deps_str + "\n\n请先安装依赖: pip install -r requirements.txt"
        show_error_dialog(error_msg)
        return
    
    # 检查FFmpeg
    import subprocess
    try:
        subprocess.run(["ffmpeg", "-version"], capture_output=True, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        # 只显示警告，不阻止程序运行
        pass
    
    # 根据系统选择合适的Tkinter类型
    import platform
    if platform.system() == "Windows":
        try:
            from tkinterdnd2 import TkinterDnD
            root = TkinterDnD.Tk()
        except ImportError:
            root = tk.Tk()
    else:
        root = tk.Tk()
    
    # 显示FFmpeg警告（如果有）
    try:
        subprocess.run(["ffmpeg", "-version"], capture_output=True, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        messagebox.showwarning("警告", "未找到FFmpeg，音频转换可能失败\n请确保FFmpeg已安装并添加到PATH环境变量")
    
    app = OGGToMP3Converter(root)
    
    # 设置窗口协议，防止意外关闭
    def on_closing():
        if messagebox.askokcancel("退出", "确定要退出程序吗？"):
            root.destroy()
    
    root.protocol("WM_DELETE_WINDOW", on_closing)
    
    root.mainloop()

if __name__ == "__main__":
    main()