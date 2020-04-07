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
from demo import load_checkpoints
generator, kp_detector = load_checkpoints(config_path='config/vox-256.yaml', 
                            checkpoint_path='trained_model/vox-cpk.pth.tar',cpu=True)

print("loading models stuff")
from demo import make_animation
from skimage import img_as_ubyte

def deepfake(image,video):
    
    source_image = imageio.imread(image)
    driving_video = imageio.mimread(video)


    #Resize image and video to 256x256

    source_image = resize(source_image, (256, 256))[..., :3]
    driving_video = [resize(frame, (256, 256))[..., :3] for frame in driving_video]

    predictions = make_animation(source_image, driving_video, generator, kp_detector, relative=True,cpu=True)

    #save resulting video
    imageio.mimsave('./generated.mp4', [img_as_ubyte(frame) for frame in predictions])
#     #video can be downloaded from /generated folder
# image_path = str(Path.cwd()/"deepfake-video"/"ron_swanson_v1.png")
# video_path = "./demo/face_01.mp4"

def handle(req):
    req = json.loads(req)

    mc = Minio(os.environ['minio_hostname'],
                  access_key=os.environ['minio_access_key'],
                  secret_key=os.environ['minio_secret_key'],
                  secure=False)

    if req["video"] != "" and req["image"] != "":
        deepfake(req["image"],req["video"])

    dirname = os.path.dirname(__file__)
    file_name = os.path.join(dirname, './generated.mp4')

    mc.fput_object("video", get_temp_file()+".mp4", file_name)
    return file_name


def get_temp_file():
    uuid_value = str(uuid.uuid4())
    return uuid_value