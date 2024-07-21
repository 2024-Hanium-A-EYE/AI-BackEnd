#!/bin/bash

# update system
sudo apt update && sudo apt install figlet -y

figlet Welcome To
figlet AEYE AI 

# install dependencies
sudo pip install -r dependencies_AI.txt

####################
## install docker ##
####################
figlet Install Docker
sudo apt install -y \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
    
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
  
sudo apt update
sudo apt install -y docker-ce docker-ce-cli containerd.io

# Create the docker group.
sudo groupadd docker

###########################
## install Nvidia Docker ##
###########################
figlet Install 
figlet Nvidia Docker
distribution=$(. /etc/os-release;echo $ID$VERSION_ID) \
   && curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add - \
   && curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | sudo tee /etc/apt/sources.list.d/nvidia-docker.list
   
sudo apt update
sudo apt install -y nvidia-docker2

sudo systemctl restart docker

sudo docker run --rm --gpus all nvidia/cuda:11.0-base nvidia-smi

###########
## READY ##
###########
figlet Ready!


# run server
#figlet Start Server
#cd AEYE_AI_Back_3_2
#python manage.py runserver



