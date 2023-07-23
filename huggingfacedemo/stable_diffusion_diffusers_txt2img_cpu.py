from diffusers import DiffusionPipeline
from time import time_ns
import os
import torch

# 依赖库安装
# pip install --upgrade diffusers[torch]
# pip install transformers
# pip install accelerate 这个是可选的
# huggingface 缓存默认目录： ~/.cache/huggingface
#
# 这个是 在线 diffusers 的预训练模型，需要下载配置代理，默认下载 5G 的版本。
# name_or_path = "runwayml/stable-diffusion-v1-5"
# 这个是 离线 CompVis/stable-diffusion 的预训练模型 10G。git@hf.co:CompVis/stable-diffusion-v1-4
here = os.path.dirname(__file__)
name_or_path = f"{here}/stable-diffusion-v1-4"
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
# prompt = "icon sword fire burning ice"
# prompt = "chaos night star nebula  burning torch dragon"

# prompt = "icon sword setting torch burning"
# prompt = 'tavern people traveler torch beer'
# prompt = 'tavern people traveler torch'
# prompt = 'traveler beer medieval tavern'
# prompt = 'traveler medieval piazza plaza'
# prompt = 'traveler medieval village'
# prompt = 'overlook travelers ancient chinese village'
# prompt = 'overlook travelers ancient chinese city'
# prompt = 'aerial photography ancient chinese city'
# prompt = 'ancient chinese boy meditation smoky'
prompt = '3d cartoon ancient chinese boy meditation with nebula'

#
self_dir = os.path.dirname(__file__)
now = time_ns()
print(f'here: {self_dir}')
for i in range(10):
    out_result = pipeline(prompt)
    out_count = len(out_result.images)
    out_path = f"{self_dir}/.out/{now}/{i}.png"
    out_dir = os.path.dirname(out_path)
    if not os.path.isdir(out_dir):
        print(f'makedirs: {out_dir}')
        os.makedirs(out_dir, exist_ok=True)
    print(f'out count: {out_count}')
    image = out_result.images[0]  
    image.save(out_path)