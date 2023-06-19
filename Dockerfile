FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive
RUN apt update \
    && apt upgrade -y \
    && apt install -y apt-utils \
    && apt install -y g++-11 python3 python3-pip nvidia-cuda-toolkit nvidia-cuda-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install -U conan \
    && conan profile detect

WORKDIR /app

COPY . .

RUN conan create .
