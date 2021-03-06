from pathlib import Path
import sys, os, uuid ,json
from minio import Minio


import imageio
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from skimage.transform import resize
import warnings

warnings.filterwarnings("ignore")


print("Loading Machine Learning Model")
from function.demo import load_checkpoints
generator, kp_detector = load_checkpoints(config_path='function/config/vox-256.yaml', 
                            checkpoint_path='function/vox-cpk.pth.tar',cpu=True)

print("loading models stuff")
from function.demo import make_animation
from skimage import img_as_ubyte

print(".")
def get_temp_file():
    uuid_value = str(uuid.uuid4())
    return uuid_value

def deepfake(image,video,temp_file_name):
    
    print("Loading images")
    source_image = imageio.imread(image)
    driving_video = imageio.mimread(video)
    print("Loaded images")

    #Resize image and video to 256x256

    source_image = resize(source_image, (256, 256))[..., :3]
    driving_video = [resize(frame, (256, 256))[..., :3] for frame in driving_video]

    predictions = make_animation(source_image, driving_video, generator, kp_detector, relative=True,cpu=True)

    #save resulting video
    imageio.mimsave('/home/app/function/public/'+ temp_file_name+".mp4", [img_as_ubyte(frame) for frame in predictions])

print(".")


def handle(req):
    req = json.loads(req)
    # mc = Minio(os.environ['minio_hostname'],
    #               access_key=os.environ['minio_access_key'],
    #               secret_key=os.environ['minio_secret_key'],
    #               secure=False)

    print(".")
    if req["video"] == "" and req["image"] == "":
        return 'please enter video and image link  {"video":"URL","image":"URL"}'
    
    print("X")
    temp_file_name = get_temp_file() + ".mp4"
    deepfake(req["image"],req["video"],temp_file_name)
    print("O")
    return temp_file_name

print(".")
# handle('{"video":"http://157.245.162.16:1337/face_01.mp4","image":"http://157.245.162.16:1337/ron_swanson_v1.png"}')
