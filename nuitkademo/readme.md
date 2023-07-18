# Nuitka

打包工具

[GitHub](https://github.com/Nuitka/Nuitka)

```bash
# 安装包
pip install nuitka

# 验证版本
python -m nuitka --version

# 打包（这种没运行时，运行大概率不行。）
python -m nuitka hello.py

# 把运行时一起打包。
python -m nuitka hello.py --standalone

# 打包单文件
python -m nuitka hello.py --standalone --onefile

# 指定 Windows 图标 需要安装 imageio
pip install imageio
python -m nuitka hello.py --standalone --onefile --windows-icon-from-ico=icon.png


# 打包成 pyd 或 os
python -m nuitka --module hello.py
```
