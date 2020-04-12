FROM wisehackermonkey/deepfake-build-2


WORKDIR /home/app

COPY server.py          .
COPY requirements.txt   .

COPY ./requirements.txt /home/app/requirements.txt


RUN pip3 install -r requirements.txt

COPY ./function /home/app/function
# COPY ./public /home/app/public

# RUN mkdir -p /home/app/public

ENTRYPOINT [ "python3" ]

CMD [ "server.py" ]