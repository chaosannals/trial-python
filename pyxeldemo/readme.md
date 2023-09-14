#

[GitHub文档](https://github.com/kitao/pyxel/blob/main/docs/README.cn.md)

## 安装

```bash
# 安装
pip install -U pyxel

# 创建或打开 资源文件
pyxel edit app.pyxres

# 发布应用 [项目目录]  [项目启动文件]
# 会得到 目录名.pyxapp 的文件。
pyxel package ./ app.py

# 启动 pyxapp
pyxel play pyxeldemo.pyxapp

# 需要安装 pip install pyinstaller
# 通过 pyxapp 文件打包 exe
pyxel app2exe pyxeldemo.pyxapp
```
