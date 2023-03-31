# base image
FROM alpine:3.17

# installing of work directory (by default) in image
WORKDIR /calc-bot

# installing of requirements
RUN set -eux; \
	apt-get update; \
	apt-get install -y --no-install-recommends \
        software-properties-common \
	; \
	rm -rf /var/lib/apt/lists/*

RUN add-apt-repository ppa:deadsnakes/ppa && apt-get install -y python3.11

RUN apt-get python3-pip

RUN touch .env

# copying project to image
COPY . .

# installing requirements from pip
RUN pip3 install -r requirements.txt

# start script after container start
ENTRYPOINT ["python3", "app.py"]