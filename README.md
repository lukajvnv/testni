# First-Docker-app


[![Build Status](https://travis-ci.org/MilosSimic/First-Docker-app.svg?branch=master)](https://travis-ci.org/MilosSimic/First-Docker-app) [![Built with Spacemacs](https://cdn.rawgit.com/syl20bnr/spacemacs/442d025779da2f62fc86c2082703697714db6514/assets/spacemacs-badge.svg)](http://spacemacs.org)

Simple Flask app that is in Docker container, demonstrating how to build run and map volumes.


## Build Docker image
 ```
 docker build -t myapp:latest .
 ```


## Run from local build
Run container from local build:
 ```
 docker run -d -p 5000:5000 myapp
 ```

Run container with mapped volumes from local build:
 ```
 docker run -d -p 5000:5000 -v path_to_logs_file_on_your_disk:/usr/src/app/myapp/logs myapp
 ```


## Run from Dockerhub
Run container from dockerhub:
 ```
 docker run -d -p 5000:5000 milossimic/simple_flask_app
 ```

Run container from dockerhub with mapped volumes:
 ```
 docker run -d -p 5000:5000 -v path_to_logs_file_on_your_disk:/usr/src/app/myapp/logs milossimic/simple_flask_app
 ```

## Run two containers using docker-compose
To run multiple container it is easier to use docker-compose (navigate to path where docker-compose.yml file is):
 ```
 docker-compose up
 ```
 
 * NOTE: Change the path to location where to store logs inside docker-compose.yml file! 

To stop docker-compose run:
 ```
 docker-compose down
 ```
 
 * NOTE: Change the path to location where to store logs inside docker-compose.yml file! 


## Few other userful commands:
 * List all images:
  ```
  docker-compose down
  ```
  
 * Show active containers:
  ```
  docker ps
  ```
  
 * Show inactive containers:
  ```
  docker ps -a
  ```
  
 * Remove container:
  ```
  docker rm name or hash_of_container
  ```
  
 * Remove image:
  ```
  docker rmi name or hash_of_image
  ```
  
 * Stop active container:
  ```
  docker stop name or hash_of_container
  ```
  
 * Start inactive container:
  ```
  docker start name or hash_of_container
  ```
  
 * Container logs:
  ```
  docker logs name or hash_of_container
  ```
  
 * Pull docker image:
  ```
  docker pull name_of_container
  ```
  
 * NOTE: name of container must be specified on run
 * NOTE: all commands can be found in [official docs](https://docs.docker.com/engine/reference/commandline/docker/#child-commands)


## Dockerhub link
[![Dockerhub](https://www.docker.com/sites/default/files/Dockerized%20Apps_icon.png)](https://hub.docker.com/r/milossimic/simple_flask_app/)

[Image](https://hub.docker.com/r/milossimic/simple_flask_app/) is pushed to dockerhub using Travis CI.

## Kubernetes and Minikube
[![Minikube](https://sweetcode.io/wp-content/uploads/2017/02/imgres.png)](https://kubernetes.io/docs/setup/minikube/)

[Tutorial](https://sweetcode.io/learning-kubernetes-getting-started-minikube/) for kubernetes and minikube

 * Kubernetes list pods:
  ```
  kubectl get pods
  ```
  * Kubernetes list services:
  ```
  kubectl get services
  ```
 * Kubernetes list deployments:
  ```
  kubectl get deployments
  ```
   * Kubernetes apply object:
  ```
  kubectl apply -f filen_name.yaml
  ```
  * Minikube start:
  ```
  minikube start
  ```
  * Minikube stop:
  ```
  minikube stop
  ```
  * Minikube ip address:
  ```
  minikube ip
  ```
  * Minikube dashboard:
  ```
  minikube dashboard
  ```
   * NOTE: all commands can be found in [official docs](https://kubernetes.io/docs/reference/kubectl/kubectl-cmds/)
   
## Travis tutorial
- Tutorial for travis CICD can be found [here](https://github.com/MilosSimic/Travis-tutorial)
- Docker image for Travis CLI can be found [here](https://github.com/MilosSimic/mytravis)
