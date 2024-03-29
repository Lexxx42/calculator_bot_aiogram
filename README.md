# calculator_bot_aiogram

Calculator https://github.com/Lexxx42/calculator is now a telegram bot

* Coded with Python 3.11.1

---

## used libraries

* https://docs.aiogram.dev/en/dev-3.x/

---

## С чего начать?

1. Создать бота у бота отца https://t.me/BotFather
2. Используя команду /newbot или через меню бота-отца
3. установить зависимости из файла requirements.txt командой: pip install -r requirements.txt
4. создать в корне проекта файл .env
5. вставить в .env строку: BOT_TOKEN=ВАШ_ТОКЕН_ТЕЛЕГРАМА, где ВАШ_ТОКЕН_ТЕЛЕГРАМА - токен бота, который получен от
   бота-отца.

*Пример:*

``` shell
BOT_TOKEN=ВАШ_ТОКЕН_ТЕЛЕГРАМА
```

# New features with docker

## If there is an error about lack of access, add current user to the docker group:

```shell
sudo usermod -a -G docker [user]
newgrp docker
```

## Use this sequence of commands to run the container:

1. To run the application in docker, you need to install docker-compose:

```shell
sudo apt install docker-compose 
```

2. Clone the repository

```shell
git clone https://github.com/Lexxx42/calculator_bot_aiogram.git
```

3. Change directory to project dir

```shell
cd calculator_bot_aiogram/
```

4. Add your tokens for telegram bot and yandex weather

```shell
nano .env
```

```
BOT_TOKEN=YOUR_BOT_TOKEN
```

Don't forget to save changes!

5. Start the build

```shell
docker-compose up --build
```

### Added docker image to public repository

[Docker Hub](https://hub.docker.com/repository/docker/alex42konukhov/calculator-bot-aiogram/general)

If you are using docker image from DockerHub use following commands:

1. To pull repository use:

```docker
docker pull alex42konukhov/calculator-bot-aiogram:ubuntu
```

2. Create a container from the image. Should be an error message.

```docker
docker run alex42konukhov/calculator-bot-aiogram:ubuntu
```

3. Create `.env` file and add your telegram token

```
BOT_TOKEN=YOUR_BOT_TOKEN 
```

4. Copy the modified configuration file from your host machine to the container's file system:

```docker
docker cp .env docker_container_id:/calc-bot/.env
```

5. Run docker container in detached mode

```docker
docker start container_id
```
