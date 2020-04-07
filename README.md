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

### test with network files
```
Required request parameters
image=<URL to png or jpg> and video=<URL to mp4 or mov>
```
##### example

```
localhost:5000/generate?image=http://127.0.0.1:8887/Stills/john_snow.png&video=http://127.0.0.1:8887/ExportedVideo/oran.mp4
```

### generate deep fake givin image of circie from game of thrones
##### got punch in to browser
```
http://localhost:5000/generate?image=https://d4mucfpksywv.cloudfront.net/research-covers/glow/demo/media/cersei.png&video=http://127.0.0.1:8887/ExportedVideo/oran.mp4

http://localhost:5000/generate?image=https://d4mucfpksywv.cloudfront.net/research-covers/glow/demo/media/cersei.png&video=http://127.0.0.1:8887/ExportedVideo/oran.mp4


Image Link:
https://raw.githubusercontent.com/wisehackermonkey/deepfake-demo-files/master/gameofthrones-01.png
Video Link:
https://github.com/wisehackermonkey/deepfake-demo-files/blob/master/01.mp4?raw=true

URL
http://localhost:5000/generate?image=https://raw.githubusercontent.com/wisehackermonkey/deepfake-demo-files/master/gameofthrones-01.png&video=https://github.com/wisehackermonkey/deepfake-demo-files/blob/master/04.mp4?raw=true



```



### Next steps
-x fix the docker container to include tk 
- openfaas-ify the cpu only version
- deploy to openfaas 



### build second lay in docker container
```
docker build . -t wisehackermonkey/deepfake-build-2
```

### run second lay in of docker container
```
docker run --rm -it -v ${PWD}:/home/app wisehackermonkey/deepfake-build-2
```

### run final lay in of docker container
```
docker run --rm -it -v ${PWD}:/home/app wisehackermonkey/deepfake-video:latest
```

### view docker image layerhistory
```
docker history wisehackermonkey/deepfake-build-1
```
```
view command history and size
docker history --no-trunc --format "{{.Size}} | {{.CreatedBy}}" wisehackermonkey/deepfake-build-1
```


### open-faas generate 
```
faas-cli new --lang=python3-debian deepfake-video
```

### open-faas build 
```
faas-cli build -f ./deepfake-video
```


### setup simple samba share
```
docker run -it --name samba -p 139:139 -p 445:445  -v ${PWD}:/mount  -d dperson/samba -p
```