#############################################################
# AEYE AI BackEnd DockerFile
# Created By Yoonchul Chung
# Created At 2024.08.03
# Welcome to Visit Github : https://github.com/Yoonchulchung
#############################################################
FROM python:3.6-slim


#############################################################
# Install Dependencies
WORKDIR /app
COPY dependencies_AI.txt /app/

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip
RUN pip install -r dependencies_AI.txt


#############################################################
# Clean

#############################################################
# Copy DIR
WORKDIR /app/

COPY ../../AEYE_AI_Back_3_2/ /app/

#############################################################
# Result


EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
