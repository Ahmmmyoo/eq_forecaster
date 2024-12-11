# Earthquake Forecaster

### To setup docker environment through docker-hub

Pull the image from docker-hub:
`docker pull hasnainshinwari/eco-forcast:latest`

Build the image:
`docker build -t hasnainshinwari/eco-forcast:latest .`

Run the container:
`docker run -it -p 8501:8501 hasnainshinwari/eco-forcast:latest bash`

Mount your local directory containing the Streamlit files to the container. This way, any changes you make locally will be immediately available inside the container. (Instead of running the container directly):
`docker run -it -p 8501:8501 -v $(pwd):/app hasnainshinwari/eco-forcast:latest /bin/bash`

Run the streamlit app:
`streamlit run src/overview.py --server.port 8501 --server.address 0.0.0.0`

To exit the docker container:
`exit`

### To push the updated build to docker-hub

Login:
`Login through docker desktop, if you havent already`

Push the image:
`docker push hasnainshinwari/eco-forcast:latest`