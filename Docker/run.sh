run_docker()
{
  nvidia-docker run -p 3000:3000 --gpus all --rm --name aeye aeye_ai:1.0 &
  FIRST_PID=$!
}

enter_docker()
{
  docker exec -it aeye bash
}

initiate()
{
  run_docker
  sleep 2
  enter_docker
}
# initiate

docker-compose up
