FROM ubuntu:20.04

# 作業ディレクトリを指定
WORKDIR /workspace

# gitとpython3をインストール
RUN apt-get update && apt-get install -y git python3 python3-pip

# opencv-pythonをインストール
RUN pip3 install --upgrade pip && pip3 install opencv-python

# workspaceフォルダにリポジトリをクローン
RUN cd /workspace && git clone https://github.com/SO000000/transparent-img.git
