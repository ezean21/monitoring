# A mini monitoring system

> A mini monitoring system for an S3 bucket with kubernetes

## Quick Start

```bash

# Ensure minikue is running as well
minikube status

# Ensure helm v3 is installed as well :)
# Reference -> https://helm.sh/docs/intro/install/
brew install helm
 
# Build
eval $(minikube docker-env)
./docker_build.sh <TAG> 
# TAG is the image tag we want to set 

# Deploy
cd helm
./deploy <TAG>
# where TAG is the same we use in the build image stage
# Note: you can add --debug --dry-run to debug/dry-run

Enjoy :-)

```
