FROM tensorflow/tensorflow:1.12.0-rc1-gpu-py3


#############################################################
# Install Dependencies

RUN pip install keras==2.2.4
RUN pip install pycm==1.9 matplotlib sklearn

RUN pip install --upgrade pip
RUN pip install opencv-python
RUN pip install flask
RUN pip install colorama
#############################################################
# Copy Files
WORKDIR /app/

COPY ../../AI/ /app/ 

#############################################################
# Cleaning

#############################################################
# RUN

CMD ["python", "run.py", "--p", "3000"]

