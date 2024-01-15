# txtai 示例

## 库

```bash
# 全部
pip install txtai[all]

# WEB API 服务器
pip install txtai[api]

# 
pip install txtai[cloud]

# 
pip install txtai[console]

# 
pip install txtai[database]

#
pip install txtai[graph]

#
pip install txtai[model]

#
pip install txtai[pipeline]

#
pip install txtai[similarity]

#
pip install txtai[workflow]

# 可以组合
pip install txtai[pipeline,workflow]
```

## 使用国内 HF 镜像源

```bash
export HF_ENDPOINT=https://hf-mirror.com
```

```bat
set HF_ENDPOINT=https://hf-mirror.com
```

```powershell
$env:HF_ENDPOINT='https://hf-mirror.com'
```

https://hf-mirror.com/sentence-transformers/all-MiniLM-L6-v2

git clone https://hf-mirror.com/sentence-transformers/all-MiniLM-L6-v2
