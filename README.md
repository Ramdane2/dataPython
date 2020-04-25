## Docker concepts
Docker is a platform for developers and sysadmins to build, run, and share applications with containers. The use of containers to deploy applications is called containerization. Containers are not new, but their use for easily deploying applications is.

Containerization is increasingly popular because containers are:

Flexible: Even the most complex applications can be containerized.
Lightweight: Containers leverage and share the host kernel, making them much more efficient in terms of system resources than virtual machines.
Portable: You can build locally, deploy to the cloud, and run anywhere.
Loosely coupled: Containers are highly self sufficient and encapsulated, allowing you to replace or upgrade one without disrupting others.
Scalable: You can increase and automatically distribute container replicas across a datacenter.
Secure: Containers apply aggressive constraints and isolations to processes without any configuration required on the part of the user.

## Get started
Install Docker on Ubuntu

### Uninstall old versions
Older versions of Docker were called docker, docker.io, or docker-engine. If these are installed, uninstall them:
```
$ sudo apt-get remove docker docker-engine docker.io containerd runc
```

### SET UP THE REPOSITORY
Update the apt package index and install packages to allow apt to use a repository over HTTPS:
```
$ sudo apt-get update

$ sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common
```
## INSTALL DOCKER ENGINE
Update the apt package index, and install the latest version of Docker Engine and containerd, or go to the next step to install a specific version:
```
 $ sudo apt-get update
 $ sudo apt-get install docker-ce docker-ce-cli containerd.io
 ```
Verify that Docker Engine is installed correctly by running the hello-world image.
```
$ sudo docker run hello-world
````
## Create and start a container
Containers offer a logical packaging mechanism in which applications can be abstracted from the environment in which they actually run. This decoupling allows container-based applications to be deployed easily and consistently, regardless of whether the target environment is a private data center, the public cloud, or even a developer’s personal laptop. This gives developers the ability to create predictable environments that are isolated from the rest of the applications and can be run anywhere.

From an operations standpoint, apart from portability containers also give more granular control over resources giving your infrastructure improved efficiency which can result in better utilization of your compute resources.

### Dockerfile
Create file name "Dockerfile" and copy the content :

```
FROM ubuntu:latest
RUN apt-get update && apt-get -y update
RUN apt-get install -y build-essential python3.6 python3-pip python3-dev
RUN pip3 -q install pip –upgrade
RUN mkdir src
WORKDIR src/
COPY . .
RUN pip3 install -r requirements.txt
RUN pip3 install jupyter
RUN pip3 install Flask
RUN python3 module.py
WORKDIR /src/notebooks
# Add Tini. Tini operates as a process subreaper for jupyter. This prevents kernel crashes.
ENV TINI_VERSION v0.6.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /usr/bin/tini
RUN chmod +x /usr/bin/tini
ENTRYPOINT ["/usr/bin/tini", "--"]
CMD ["jupyter", "notebook", "--port=8000", "--no-browser", "--ip=0.0.0.0", "--allow-root"]
```

### Build image
```
$ docker build -t container-name .
```
### Run container
```
$ docker run -d -p 8000:8888 container-name
```
## Uninstall Docker Engine
If you want uninstall the Docker Engine, CLI, and Containerd packages:
```
$ sudo apt-get purge docker-ce docker-ce-cli containerd.io
```

## Start framework Flask on google cloud VM
copy index.py in your repository
```
from flask import Flask
import json

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello world !"

@app.route('/books')
def books():
    listBook = ''
    with open('./books.json') as json_file:
        data = json.load(json_file)
        for p in data:
            listBook += 'Titre: ' + p['title'] + '\n'
    return listBook


if __name__ == "__main__":
    app.run(host="0.0.0.0")
 ```
