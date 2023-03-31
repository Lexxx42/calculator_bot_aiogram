# base image
FROM debian:bullseye-slim

# installing of work directory (by default) in image
WORKDIR /calc-bot

# installing of requirements
RUN set -eux; \
	apt-get update; \
	apt-get install -y --no-install-recommends \
		python3-pip \
        wget \
	; \
	rm -rf /var/lib/apt/lists/*

RUN cd /usr/src \
    && wget https://www.python.org/ftp/python/3.11.0/Python-3.11.0.tgz \
    && tar -xzf Python-3.11.0.tgz \
    && cd Python-3.11.0 \
    && ./configure --enable-optimizations \
    && make altinstall

RUN update-alternatives --install /usr/bin/python python /usr/local/bin/python3.11 1

RUN touch .env

# copying project to image
COPY . .

# installing requirements from pip
RUN pip3 install -r requirements.txt

# start script after container start
ENTRYPOINT ["python3", "app.py"]