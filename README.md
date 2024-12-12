# Earthquake Forecaster
In this project, we will focus on cloning a GitHub repository and building a Docker image. Once the image is created, it will be pushed to a Docker Hub repository. From Docker Hub, collaborators will have the ability to pull or push the image for further use and development.

### Open the terminal and type the below command to check the current docker images
Linux `sudo docker images` <br>
Windows `docker images`

### Cloning the demo repo from github
Linux/Windows `git clone (github repo link)` <br>

### Open the folder eco-forcast and type
Linux `sudo docker build -t docker-compose . ` (dot means the current directory) <br>
Windows `docker build -t docker-compose . `

### Now if want to check if the images is running or not type this
Linux `sudo docker run docker-compose:latest`  OR `sudo docker run -it docker-compose:latest` <br>
Windows `docker run docker-compose:latest`  OR `docker run -it docker-compose:latest`

### To push the image to dockerhub repo. (hasnainshinwari/eco-forcast)  first you had to login from terminal like this:
Linux `sudo docker login` <br>
Windows `docker login`

### Now give a tag(name) hasnainshinwari/eco-forcast to the project
Linux `sudo docker tag docker-compose:latest  hasnainshinwari/eco-forcast:latest` <br>

### Pushing an image to the dockerhub
linux `sudo docker push hasnainshinwari/eco-forcast:latest ` <br>

### (optional) now you can delete your image and then check wheather pulling of an image is working or not
Deletion:
  Linux `sudo docker rmi docker-compose --force` <br>
  Windows `docker rmi docker-compose --force` 
    
### Pulling it from the dockerhub.
  Linux `sudo docker pull hasnainshinwar/eco-forcast:latest` <br>
  Windows `docker pull hasnainshinwari/eco-forcast:latest`

### check if the container is work or not
Linux `sudo docker run hasnainshinwari/eco-forcast:latest` <br>
Windows `docker run hasnainshinwari/eco-forcast:late`
