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

# if this is called "PIP_VERSION", pip explodes with "ValueError: invalid truth value '<VERSION>'"
ENV PYTHON_PIP_VERSION 22.3
# https://github.com/docker-library/python/issues/365
ENV PYTHON_SETUPTOOLS_VERSION 65.5.0
# https://github.com/pypa/get-pip
ENV PYTHON_GET_PIP_URL https://github.com/pypa/get-pip/raw/66030fa03382b4914d4c4d0896961a0bdeeeb274/public/get-pip.py
ENV PYTHON_GET_PIP_SHA256 1e501cf004eac1b7eb1f97266d28f995ae835d30250bec7f8850562703067dc6

RUN set -eux; \
    \
    wget -O get-pip.py "$PYTHON_GET_PIP_URL"; \
    echo "$PYTHON_GET_PIP_SHA256 *get-pip.py" | sha256sum -c -; \
    \
    export PYTHONDONTWRITEBYTECODE=1; \
    \
    python get-pip.py \
        --disable-pip-version-check \
        --no-cache-dir \
        --no-compile \
        "pip==$PYTHON_PIP_VERSION" \
        "setuptools==$PYTHON_SETUPTOOLS_VERSION" \
    ; \
    rm -f get-pip.py; \
    \
    pip --version

RUN touch .env

# copying project to image
COPY . .

# installing requirements from pip
RUN pip3 install -r requirements.txt

# start script after container start
ENTRYPOINT ["python3", "app.py"]