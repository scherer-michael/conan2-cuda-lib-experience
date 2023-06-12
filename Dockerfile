FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive
RUN apt update \
    && apt install -y nvidia-cuda-toolkit nvidia-cuda-dev python3-pip g++-11 \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install -U conan \
    && conan profile detect

WORKDIR /app

COPY . .

RUN conan create .