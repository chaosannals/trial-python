from pathlib import Path
from lambda_diffusers import StableDiffusionImageEmbedPipeline
from PIL import Image
import os
import torch

# 这个模型比较老，会有一些 transforms 警告使用了废弃函数。
# git@github.com:LambdaLabsML/lambda-diffusers.git
# pip install -e F:/.github/lambda-diffusers
# git@hf.co:lambdalabs/sd-image-variations-diffusers
# git clone -b 2ddbd90b14bc5892c19925b15185e561bc8e5d0a git@hf.co:lambdalabs/sd-image-variations-diffusers
# 需要指定特殊的分支，不然缺少函数 git@hf.co:lambdalabs/sd-image-variations-diffusers

device = "cuda" if torch.cuda.is_available() else "cpu"
pipe = StableDiffusionImageEmbedPipeline.from_pretrained(
    # "lambdalabs/sd-image-variations-diffusers",
    "F:/.github/sd-image-variations-diffusers",
    revision="2ddbd90b14bc5892c19925b15185e561bc8e5d0a",
    local_files_only = True, # 只使用本地文件
    
    # 在线版，被墙，下载预训练模型要梯子
    # proxies={'https://': 'http://127.0.0.1:10809'},
    # pip install requests[socks]
    # proxies= {'https': 'socks5h://192.168.0.200:10080'},
)
pipe = pipe.to(device)

self_dir = os.path.dirname(__file__)

im = Image.open(f"{self_dir}/stable_diffusion_image_variations_diffusers_img2img.png")
num_samples = 4
image = pipe(num_samples*[im], guidance_scale=3.0)
image = image["sample"]

base_path = Path(f"{self_dir}/.out/im2im")
base_path.mkdir(exist_ok=True, parents=True)
for idx, im in enumerate(image):
    im.save(f"{base_path}/{idx:06}.jpg")