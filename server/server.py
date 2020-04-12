from flask import Flask
from flask import request
from flask import send_file

app = Flask(__name__)

from pathlib import Path
import sys, os, uuid ,json
# from minio import Minio


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

print("started flask server")
@app.route('/')
def index():
    return 'Deepfake api, <br>endpoints <br>/generate <br> /download to get video '

# @app.route("/download")
# def download_video():
#     try:
#         return send_file("./generated/generated.mp4", attachment_filename="deepfake_01.mp4")
#     except Exception as e:
#         return str(e)

@app.route('/generate', methods=['GET', 'POST'])
def generate_video():
    if request.method == 'POST' or request.method == 'GET' :
        print("post")
        image = request.args.get('image', '')
        video = request.args.get('video', '')
        if (not image) and (not video):
            return """
            <h4>Missing request parameters<br>
            image=<br>
            and<br>
            video=<br>
            example<br>
            localhost:5000/generate?image=http://127.0.0.1:8887/Stills/john_snow.png&video=http://127.0.0.1:8887/ExportedVideo/oran.mp4
            </h4>"""
        print(image)
        print(video)
        
        req = request.get_json()
        print(request.args)
        print(".")
        image_arg = request.args.get('image')
        video_arg = request.args.get('video')
        if image_arg == "" and video_arg == "":
            return 'please enter video and image link  {"video":"URL","image":"URL"}'
        
        print("X")
        temp_file_name = get_temp_file() + ".mp4"
        deepfake(image_arg,video_arg,temp_file_name)
        return send_file("./generated/generated.mp4", attachment_filename="deepfake_01.mp4")
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')