from diffusers import DiffusionPipeline
from time import time_ns
import os
import torch

# 依赖库安装
# pip install --upgrade diffusers[torch]
# pip install transformers
#
# huggingface 缓存默认目录： ~/.cache/huggingface
#
# 这个是 在线 diffusers 的预训练模型，需要下载配置代理，默认下载 5G 的版本。
# name_or_path = "runwayml/stable-diffusion-v1-5"
# 这个是 离线 CompVis/stable-diffusion 的预训练模型 10G。git@hf.co:CompVis/stable-diffusion-v1-4
name_or_path = "F:/.github/stable-diffusion-v1-4"
# 这个是 离线 diffusers 的预训练模型 65G。https://huggingface.co/runwayml/stable-diffusion-v1-5
# name_or_path = "F:/.github/stable-diffusion-v1-5"
pipeline = DiffusionPipeline.from_pretrained(
    name_or_path,
    # torch_dtype=torch.float16, # cpu 没有 half float16
    torch_dtype=torch.float32, 
    local_files_only = True, # 只使用本地文件

    # 在线版，被墙，下载预训练模型要梯子
    # proxies={'https://': 'http://127.0.0.1:10809'},
    # pip install requests[socks]
    # proxies= {'https': 'socks5h://192.168.0.200:10080'},
)

# 没有显卡
#pipeline.to("cuda")

# 没有显卡
del pipeline.vae.encoder

# 提示词
prompt = "Lunatic Dawn"
#
self_dir = os.path.dirname(__file__)
now = time_ns()
print(f'here: {self_dir}')
for i in range(10):
    out_path = f"{self_dir}/.out/{now}/{i}.png"
    out_dir = os.path.dirname(out_path)
    if not os.path.isdir(out_dir):
        print(f'makedirs: {out_dir}')
        os.makedirs(out_dir, exist_ok=True)
    image = pipeline(prompt).images[0]  
    image.save(out_path)