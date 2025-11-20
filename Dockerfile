FROM python:3.7-slim

WORKDIR /app

# COPY requirement.txt .

# RUN pip install -r requirements.txt 

COPY . . 

RUN apt-get update && apt-get install -y libx11-6 libxext-dev libxrender-dev libxinerama-dev libxi-dev libxrandr-dev libxcursor-dev libxtst-dev tk-dev && rm -rf /var/lib/apt/lists/*

CMD [ "python", "main.py" ]