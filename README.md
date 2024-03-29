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


pip install torch==1.4.0+cpu torchvision==0.5.0+cpu -f https://download.pytorch.org/whl/torch_stable.html
### example string
```
{"video":"URL","image":"URL"}

```
##### Example from local server
```
{"video":"http://127.0.0.1:8887/ExportedVideo/oran.mp4","image":"http://127.0.0.1:8887/Stills/john_snow.png"}
http://127.0.0.1:8887/ExportedVideo/oran.mp4
http://127.0.0.1:8887/Stills/john_snow.png
```


#### example test run with full image
```
docker run -it --rm   -v ${PWD}:/home/app/test wisehackermonkey/deepfake-video:latest /bin/sh
```
MINIO_HOSTNAME
MINIO_ACCESS_KEY
MINIO_SECRET_KEY



export minio_hostname="64.227.84.118:9000"
export minio_access_key="USQcf6bPKr"
export minio_secret_key="M6c6nNmrYj3FK3vCDLQqdjZXdgH5RJVgqZhGsH9Y"

import imageio;source_image = imageio.mimread("http://64.227.84.118:9000/maylogs/oran.mp4?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=USQcf6bPKr%2F20200407%2F%2Fs3%2Faws4_request&X-Amz-Date=20200407T032614Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=5e9855c7c5d80e53ed5a1dff273d64c2680328cf697c3d53ff2411b299653657");print(source_image)


import imageio;source_image = imageio.mimread("http://127.0.0.1:8887/ExportedVideo/oran.mp4");print(source_image)


https://i.imgur.com/N0OfBon.png
https://streamable.com/s/xqhkzi/yrcyge

{"video":"https://streamable.com/s/xqhkzi/yrcyge","image":"https://i.imgur.com/N0OfBon.png"}

faas-cli build ; faas-cli deploy;docker run -it --rm  deepfake-video:latest /bin/sh


{"video":"https://cdn-b-east.streamable.com/video/mp4/xqhkzi.mp4?token=vBfDOn4mQ4MoUbSMftzMxw&expires=1586415240","image":"https://i.imgur.com/N0OfBon.png"}
nano function/handler.py
python3 index.py


https://blog.alexellis.io/openfaas-storage-for-your-functions/


## Build the webserver
```
docker build . -t simple-webserver-v1 
```
## Run the webserver
```
docker run -it -p 8000:80 --rm simple-webserver-v1:latest
```

### for development
docker run -it -p 8000:80 --rm -v ${PWD}/src:/usr/share/nginx/html simple-webserver-v1:latest

## visit
> localhost:8000


### fix cors issues by making a revser peroxy that returns all requests with cors disabled

docker run -it --rm -p 10900:8080 redocly/cors-anywhere:latest




### how to run stack 
##### for more info: [Tutorial Here](https://docs.docker.com/engine/swarm/stack-deploy/)
```
locally only
docker-compose up -d

Across swarm
docker stack deploy --compose-file docker-compose.yml deepfake-video
```

### view status
```
docker stack services deepfake-video
```

### Take down stack
```
docker stack rm  deepfake-video
```

### minio run
```
docker run -d --restart always -p 9000:9000 --name mino_bucket -e "MINIO_ACCESS_KEY=USQcf6bPKr" -e "MINIO_SECRET_KEY=M6c6nNmrYj3FK3vCDLQqdjZXdgH5RJVgqZhGsH9Y" -v $(pwd)/db:/data minio/minio server /data

```




### Next steps
- x fix the docker container to include tk 
- x openfaas-ify the cpu only version
- x deploy to openfaas 
- x pull 
- build deepfake image on digitalocean
- test endpoint postman
- add/fix minio to docker compose file
- make depoyable via docker stack

-----
#### streach goals
- html test if connected to backend






### If there is issues with GIT LFS run this command
```
INSTALL GIT LFS
>curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | sudo bash
>sudo apt-get install git-lfs && git lfs install
>git lfs pull
>git lfs checkout
```
-----------

### Test string for deepfake openfaas function
```
test string
{"video":"http://157.245.162.16:1337/face_01.mp4","image":"http://157.245.162.16:1337/ron_swanson_v1.png"}
```



### Run time for generating a deepfake of length 8 seconds
```
5:39 minutes
```


### build flask deepfake server
```
docker build ./server -t flask-deepfake

DEBUG
docker run -it --rm -v ${PWD}/public:/home/app/function/public/ -p 5000:5000 flask-deepfake:latest 
```
### devolpment/debug http server
```
docker run -it -p 80:80  -v ${PWD}/website/src:/usr/share/nginx/html   matriphe/alpine-nginx:html
```

## deploy
```
>docker-compose build
>docker-compose up -d
```
