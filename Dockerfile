# FROM python:3.7-slim AS builder

# RUN apt-get update && apt-get install -y libx11-6 libxext-dev libxrender-dev libxinerama-dev libxi-dev libxrandr-dev libxcursor-dev libxtst-dev tk-dev && rm -rf /var/lib/apt/lists/*

# RUN python -m venv /venv
# ENV PATH="/venv/bin:$PATH"

# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# FROM python:3.7-slim AS runtime

# RUN apt-get update && apt-get install -y libx11-6 libxext-dev libxrender-dev libxinerama-dev libxi-dev libxrandr-dev libxcursor-dev libxtst-dev tk-dev && rm -rf /var/lib/apt/lists/*

# COPY --from=builder /venv /venv
# ENV PATH="/venv/bin:$PATH"

# WORKDIR /app 

# COPY . . 

# CMD [ "python", "main.py" ]



############################# No dev Headers Version ############################

########################### build stage ###################

FROM python:3.7-slim AS builder

RUN apt-get update && apt-get install -y \
    libgl1 \
    libxext6 \
    libxrender1 \
    libsm6 \
    && rm -rf /var/lib/apt/lists/*

RUN python -m venv /venv
ENV PATH="/venv/bin:$PATH"

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


############## runtime stage #####################


FROM python:3.7-slim AS runtime

RUN apt-get update && apt-get install -y \
    libgl1 \
    libxext6 \
    libxrender1 \
    libsm6 \
    x11-apps \
    && rm -rf /var/lib/apt/lists/*
COPY --from=builder /venv /venv
ENV PATH="/venv/bin:$PATH"

ENV DISPLAY=host.docker.internal:0.0

WORKDIR /app
COPY . .

CMD ["python", "main.py"]
