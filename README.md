# docker_playground

Docker files for Docker Playground container(s)

# Building all container
```sh
docker-compose build
```

## Build a single container

```sh
docker-compose build ros-mavros
```

# Run all containers
```sh
docker-compose up
```

## Run a single container
```sh
docker run --name test --network host --rm -it docker_playground_ros-simple:latest
```

# Check containers
```sh
docker ps
```
