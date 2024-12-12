# In this we look into cloning a github repo. also we will create a docker image, after creating the image we will push it the dockerhub repo. from the dockerhub a collaborator can push and pull the image.
#NOTE: linux and windows have the same docker commands but in linux if the command does not work try with sudo

# 1. open the terminal and type the below command to check the current docker images
#linux
sudo docker images
#windows
docker images

# 2. cloning the demo repo from github
#linux/windows
git clone (repo link)

# 3. open the folder eco-forcast and type
#linux
sudo docker build -t docker-compose . (dot means the current directory)
#windows
docker build -t docker-compose .

# 4. now if want to check if the images is running or not type this
#linux
sudo docker run docker-compose:latest  OR sudo docker run -it docker-compose:latest
#windows
docker run docker-compose:latest  OR docker run -it docker-compose:latest

# 5.to push the image to dockerhub repo. (hasnainshinwari/eco-forcast)  first you had to login from terminal like this:
#linux/
sudo docker login
#windows
docker login

# 6. now pushing image to the repo (hasnainshinwari/eco-forcast)
#linux
sudo docker tag docker-compose:latest  hasnainshinwari/eco-forcast:latest

#7. (optional) now you can delete your image and then check wheather pulling of an image is working or not
  #Deletion:
    #linux
      sudo docker rmi docker-compose --force
    #windows
      docker rmi docker-compose --force
  
    #Pulling it from repo.
      #linux
          sudo docker pull hasnainshinwar/eco-forcast:latest
      #windows
          docker pull hasnainshinwari/eco-forcast:latest

#8. check if it's work or not
#linux
sudo docker run hasnainshinwari/eco-forcast:latest
#windows
docker run hasnainshinwari/eco-forcast:latest
