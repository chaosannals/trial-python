# trial python

## hf 国内镜像

```bash
export HF_ENDPOINT=https://hf-mirror.com
```

```bat
set HF_ENDPOINT=https://hf-mirror.com
```

```powershell
$env:HF_ENDPOINT='https://hf-mirror.com'
```

## pip

```bash
# -U 安装最新版本，已安装老版本则升级。
pip install -U numpy

# -i 指定源
pip install -i https://mirrors.aliyun.com/pypi/simple/ numpy
```

### 打包发布

```bash
# 打包
python setup.py sdist bdist_wheel

# 上传
twine upload dist/*
```

```bash

```

#3 Cx_Freeze

```bash
# 打包 msi
python setup.py bdist_msi
```

## PySide6 

提升头文件写法，头文件: 
c++ 是头文件路径 ui/widget/your_widget.h
python 是模块名， ui.widget.your_widget
