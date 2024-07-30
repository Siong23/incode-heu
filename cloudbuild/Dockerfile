FROM siong23/coral-python:v2 
RUN mkdir /coral 
WORKDIR /coral 
RUN git clone https://github.com/Siong23/examples-camera.git --depth 1 
WORKDIR /coral/examples-camera 
RUN sh download_models.sh 
WORKDIR /coral/examples-camera/opencv 
RUN apt-get update && apt-get install -y python3-opencv 
ENV DISPLAY :0 
CMD ["python3", "detect.py"]
