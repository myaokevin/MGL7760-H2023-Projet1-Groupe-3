#!/bin/bash

if [[ "$1" == "Start" ]];
then 
bash ./db/import.sh &
docker-compose up -d
dwn(){
    docker rm -f $(docker ps -a -q)
    docker volume rm $(docker volume ls -q)
}
dall(){
    docker rm -f $(docker ps -a -q)
    docker volume rm $(docker volume ls -q)
}

if [[ "$1" == "Stop" ]];  
then dwn()

if [[ "$1" == "DALL" ]];  
then dall()
fi
#gggggg