FROM ubuntu:latest

RUN apt update -y
RUN apt install -y python3-pip python3 build-essential

ADD . /flask-app
WORKDIR /flask-app
RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3"]
CMD ["flask-docker.py"]