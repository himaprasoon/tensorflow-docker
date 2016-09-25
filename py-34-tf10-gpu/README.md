##Tensorflow python 3.4 with GPU support on Docker

**Prerequisites:**
1)Docker<br>
2)Nvidia - docker (for running containers which needs gpu support)

####Nvidia docker Installation on Ubuntu
```bash
wget -P /tmp https://github.com/NVIDIA/nvidia-docker/releases/download/v1.0.0-rc.3/nvidia-docker_1.0.0.rc.3-1_amd64.deb
sudo dpkg -i /tmp/nvidia-docker*.deb && rm /tmp/nvidia-docker*.deb
```

### 1) Using himaprasoon/py34-tf10-gpu nvidia-docker image 
After nvidia docker has been installed , pull the himaprasoon/py34-tf10-gpu image from docker hub
```bash
docker pull himaprasoon/py34-tf10-gpu
```
Create a Dockerfile with the following content in a directory of your choice
```bash
FROM himaprasoon/py34-tf10-gpu
ADD yourfile.py /home
WORKDIR "/home/"
ENTRYPOINT ["/usr/bin/python3.4"]
CMD ["yourfile.py"]
```
Build the new docker image
```bash
nvidia-docker build -t username/imagename:optional-tag .
```
Run the previously created docker image
```bash
nvidia-docker run -i username/imagename:optional-tag
```

### 2) Creating image from scratch 
```bash
cd baseimage
```
Append these lines to Dockerfile
```bash
ADD path_to_yourfile.py /home
WORKDIR "/home/"
ENTRYPOINT ["/usr/bin/python3.4"]
CMD ["yourfile.py"]

```
Build the new docker image
```bash
nvidia-docker build -t username/imagename:optional-tag .
```
Run the previously created docker image
```bash
nvidia-docker run -i username/imagename:optional-tag
```


