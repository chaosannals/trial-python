# cx_Freeze

无法打包单文件，但是可以打包安装包。

pyinstaller 习惯用命令。

cx_Freeze 更适合使用 setup.py 脚本进行打包安装包。

[pypi](https://pypi.org/project/cx-Freeze/)
[github.io](https://marcelotduarte.github.io/cx_Freeze/)
[github](https://github.com/marcelotduarte/cx_Freeze)

## 简单示例

具体查看[官方文档](https://cx-freeze.readthedocs.io/en/latest/index.html)。

```bash
# 命令行
python setupcui.py bdist_msi

# 图形化
python setupgui.py bdist_msi
```

```bash
# 服务
python setupwinsvc.py bdist_msi

# 在安装目录下运行 安装
winsvc.exe install

# 开始
winsvc.exe start

# 停止
winsvc.exe stop

# 卸载
winsvc.exe remove
```

注：目前服务无法正常启动。等 pywin32 的下个版本再试试。