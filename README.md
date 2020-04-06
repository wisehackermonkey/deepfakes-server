# deepfakes-server
 creates deepfake video givin 1 image of a face, and a video of someone talking and generates a fake video of the person in the image talking! ml model and work done by AliaksandrSiarohin https://github.com/AliaksandrSiarohin/first-order-model

```
by oran collins
github.com/wisehackermonkey
oranbusiness@gmail.com
20200405
```




### run flask app
```
turn on debug mode
$env:FLASK_ENV = "development"
set FLASK_APP=server.py # cmd windows
$env:FLASK_APP = "server.py" # powershell windows
```
### run
```
python -m flask run
```

### using postman make the fallowing requests
```
image_path = "http://127.0.0.1:8887/Stills/john_snow.png"
video_path = "http://127.0.0.1:8887/ExportedVideo/orans_cropped_fotage_v1.mp4"

curl -X POST localhost:5000/generate?image=ron_swanson_v1.png&video=face_01.mp4
```

### adding git lfs to large file
```
git lfs track "*.tar"
```