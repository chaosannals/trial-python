# [trial-python](https://github.com/chaosannals/trial-python)

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

### Qt5 Ui 文件编译

```sh
pyinstaller -F tool/qt5uic.py
```

### 腾讯地图行政区划

```sh
pyinstaller -F -w pick/txm/txmp.py
```
