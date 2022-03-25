# [trial-python](https://github.com/chaosannals/trial-python)

## Pypy

pypy 的命令基本和 pip 相同。

```bash
./pypy3 -m venv .pypyve
./pypy3 -m ensurepip
./pypy3 -m pip list
```

## PyQt5

安装 pyqt5 会带有命令行工具：

```bash
# 生成 UI 文件
pyuic5 -o output.py input.ui

# 生成资源文件
pyrcc5 -o output.py input.qrc
```

## 安装

```bash
pip install -r requirements.txt
```

## 工具

### 密码随机生成

```sh
pyinstaller -F tool/mkpw.py
```

### 图片重设大小

```sh
pyinstaller -F tool/imgrsz.py
```

### 图片切割

```sh
pyinstaller -F tool/imgcut.py
```

### 图片重命名

```sh
pyinstaller -F tool/imgrnm.py
```

### 生成 ICO

```sh
pyinstaller -F tool/mkico.py
```

### Git 目录下项目拉取

```sh
pyinstaller -F tool/gitautopull.py
```

### Qt5 Ui 文件编译

```sh
pyinstaller -F tool/qt5uic.py
```

### 腾讯地图行政区划

```sh
pyinstaller -F -w pick/txm/txmp.py
```

### 内网 IP ping

```sh
pyinstaller -F tool/pinginet.py
```

## 测试

```bash
# 所有测试
python -m unittest discover test -p *.py

# 指定测试
python -m unittest test.index
```
