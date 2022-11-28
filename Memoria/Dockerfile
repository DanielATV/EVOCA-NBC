#Download base image ubuntu 20.04
FROM ubuntu:22.04

# Update Ubuntu Software repository
RUN apt-get update

#Nano
RUN apt-get install nano

# Install Python/Modules
RUN apt-get install -y python3

RUN apt-get install -y python3-dev

RUN apt-get install -y python3-pip

RUN pip install numpy

RUN pip install sklearn

RUN pip install joblib

RUN pip install pandas

# Install Make
RUN apt install build-essential

# Copy Files
COPY ./NBC ./NBC

# Change Dir
WORKDIR /NBC/AKCodEVOCA180119

#Permissions
RUN chmod +x AK.sh

RUN chmod +x AK

# Compile
RUN make




