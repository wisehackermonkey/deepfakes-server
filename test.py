import os, sys
import pathlib
r,w = os.pipe()


os.close(r)
image_path = str(pathlib.Path.cwd()/"deepfake-video"/"ron_swanson_v1.png")
print(open(image_path,"r",encoding="ascii").read())