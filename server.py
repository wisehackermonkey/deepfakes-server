import imageio
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from skimage.transform import resize
from IPython.display import HTML
import warnings

from flask import Flask
from flask import request
from flask import send_file

app = Flask(__name__)

warnings.filterwarnings("ignore")

def display(source, driving, generated=None):
    Writer = animation.writers['ffmpeg']
    writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=1800)
                    
    fig = plt.figure(figsize=(8 + 4 * (generated is not None), 6))

    ims = []
    for i in range(len(driving)):
        cols = [source]
        cols.append(driving[i])
        if generated is not None:
            cols.append(generated[i])
        im = plt.imshow(np.concatenate(cols, axis=1), animated=True)
        plt.axis('off')
        ims.append([im])

    ani = animation.ArtistAnimation(fig, ims, interval=50, repeat_delay=1000)
    ani.save('im.mp4', writer=writer)
    plt.close()
    return ani

print("Loading Machine Learning Model")
from demo import load_checkpoints
generator, kp_detector = load_checkpoints(config_path='config/vox-256.yaml', 
                            checkpoint_path='trained_model/vox-cpk.pth.tar')

print("loading models stuff")
from demo import make_animation
from skimage import img_as_ubyte

def deepfake(image,video):
    
    source_image = imageio.imread(image)
    driving_video = imageio.mimread(video)


    #Resize image and video to 256x256

    source_image = resize(source_image, (256, 256))[..., :3]
    driving_video = [resize(frame, (256, 256))[..., :3] for frame in driving_video]

    predictions = make_animation(source_image, driving_video, generator, kp_detector, relative=True)

    #save resulting video
    imageio.mimsave('./generated/generated.mp4', [img_as_ubyte(frame) for frame in predictions])
    #video can be downloaded from /generated folder


print("started flask server")
@app.route('/')
def index():
    return 'Deepfake api, <br>endpoints <br>/generate <br> /download to get video '

@app.route("/download")
def download_video():
    try:
        return send_file("./generated/generated.mp4", attachment_filename="deepfake_01.mp4")
    except Exception as e:
        return str(e)

@app.route('/generate', methods=['GET', 'POST'])
def generate_video():
    if request.method == 'POST':
        print("post")
        image = request.args.get('image', '')
        video = request.args.get('video', '')

        print(image)
        print(video)
        deepfake(image,video)
        return send_file("./generated/generated.mp4", attachment_filename="deepfake_01.mp4")
    else:
        print("get")
        return "get request made Please use POST instead"