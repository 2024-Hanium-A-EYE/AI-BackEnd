#!/bin/bash

# 특정 이미지를 변수에 저장합니다.

EXCLUDE_IMAGE_ID=$(docker images -q tensorflow/tensorflow)
# 특정 이미지를 제외한 모든 이미지 ID를 가져와 삭제합니다.
docker rm $(docker ps -aq)

docker images -q | grep -v "$EXCLUDE_IMAGE_ID" | xargs -r docker rmi

