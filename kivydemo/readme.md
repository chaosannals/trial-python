# kivy demo

```bash
# 生成加载 kv 文件 __init__.py
python -m kvuip.py

# 打包
python -m PyInstaller kvdemo.spec
```

注： *.spec 是修改过的。注意序号 # 0 开始。

```cmd
set PROXY_HTTP="http://127.0.0.1:1088"
set PROXY_HTTPS="http://127.0.0.1:1088"
```