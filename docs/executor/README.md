# Executor
インフラ側スクリプトを実行するデーモンです。

## Install Python3 (CentOS)

```bash
curl -O https://www.python.org/ftp/python/3.5.1/Python-3.5.1.tgz
tar zxf Python-3.5.1.tgz
cd Python-3.5.1
./configure --prefix=/usr/local
make
make altinstall
```

## Install Python3 (Ubuntu)
```bash
sudo apt-get update -y
sudo apt install -y python3-pip
sudo pip3 install virtualenv
virtualenv ~/virtualenv
source ~/virtualenv/bin/activate
```

## Deploy

```bash
git clone https://github.com/mister-curl/tala.git
cd tala/tala/core/utils
export PYTHONPATH=/home/ubuntu/tala/tala/
celery -A executor worker --loglevel=info
```
