from pathlib import Path
import sys, os
from minio import Minio
import json


# import imageio
# import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib.animation as animation
# from skimage.transform import resize
# import warnings

# warnings.filterwarnings("ignore")


# print("Loading Machine Learning Model")
# from demo import load_checkpoints
# generator, kp_detector = load_checkpoints(config_path='config/vox-256.yaml', 
#                             checkpoint_path='trained_model/vox-cpk.pth.tar',cpu=True)

# print("loading models stuff")
# from demo import make_animation
# from skimage import img_as_ubyte

# def deepfake(image,video):
    
#     source_image = imageio.imread(image)
#     driving_video = imageio.mimread(video)


#     #Resize image and video to 256x256

#     source_image = resize(source_image, (256, 256))[..., :3]
#     driving_video = [resize(frame, (256, 256))[..., :3] for frame in driving_video]

#     predictions = make_animation(source_image, driving_video, generator, kp_detector, relative=True,cpu=True)

#     #save resulting video
#     imageio.mimsave('./generated/generated.mp4', [img_as_ubyte(frame) for frame in predictions])
#     #video can be downloaded from /generated folder
# image_path = str(Path.cwd()/"deepfake-video"/"ron_swanson_v1.png")
# video_path = "./demo/face_01.mp4"

def handle(req):
    req = json.loads(req)

    mc = Minio(os.environ['minio_hostname'],
                  access_key=os.environ['minio_access_key'],
                  secret_key=os.environ['minio_secret_key'],
                  secure=False)

    """handle a request to the function
    Args:
        req (str): request body
    """
    # deepfake(image_path,video_path)
    dirname = os.path.dirname(__file__)
    path = os.path.join(dirname, 'ron_swanson_v1.png')


    return html

    # sys.stdout = open(image_path,"w")
    # with open(image_path,"r",encoding='cp1252') as file:
    #     sys.stdout = file
    # return req

    
    # with open(image_path, "r") as image_file:
    #     # print(image_file,end="")
    #     return image_file.read()
# handle("")