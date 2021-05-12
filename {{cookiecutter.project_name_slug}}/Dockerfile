FROM python:3.8

# VSCode users:
# Before rebuild your devcontainer
# make sure poetry.lock is up-to-date
# (use command make update)

# For VSCode Docker Extension to work
# Please check https://aka.ms/vscode-remote/containers/non-root
ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME

RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y net-tools git build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
xz-utils tk-dev libffi-dev liblzma-dev python-openssl libpq-dev libcurl4-openssl-dev

WORKDIR /tmp

RUN curl -fsSL https://get.docker.com -o get-docker.sh
RUN sh get-docker.sh

RUN curl -L -O https://github.com/aws/aws-sam-cli/releases/latest/download/aws-sam-cli-linux-x86_64.zip
RUN unzip aws-sam-cli-linux-x86_64.zip -d sam-installation
RUN ./sam-installation/install

WORKDIR /app

RUN pip install -U pip poetry
COPY . /app

EXPOSE 3000

CMD ["sh", "entrypoint.sh"]