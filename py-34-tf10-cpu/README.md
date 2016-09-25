##Tensorflow python 3.4  on Docker

**Prerequisites:**
1)Docker<br>


### 1) Using himaprasoon/py34-tf10-cpu docker image 
After docker has been installed , pull the himaprasoon/py34-tf10-cpu image from docker hub
```bash
docker pull himaprasoon/py34-tf10-cpu
```
Create a Dockerfile with the following content in a directory of your choice
```bash
FROM himaprasoon/py34-tf10-cpu
ADD yourfile.py /home
WORKDIR "/home/"
ENTRYPOINT ["/usr/bin/python3.4"]
CMD ["yourfile.py"]
```
Build the new docker image
```bash
docker build -t username/imagename:optional-tag .
```
Run the previously created docker image
```bash
docker run -i username/imagename:optional-tag
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
docker build -t username/imagename:optional-tag .
```
Run the previously created docker image
```bash
docker run -i username/imagename:optional-tag
```


