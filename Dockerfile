FROM python:3.10-slim

# Install system dependencies required for Kivy
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    ffmpeg \
    libsdl2-dev \
    libsdl2-image-dev \
    libsdl2-mixer-dev \
    libsdl2-ttf-dev \
    libportmidi-dev \
    libswscale-dev \
    libavformat-dev \
    libavcodec-dev \
    zlib1g-dev \
    gstreamer1.0-plugins-base \
    gstreamer1.0-plugins-good \
    gstreamer1.0-tools \
    gstreamer1.0-x \
    libgl1-mesa-glx \
    && apt-get clean

# Install Python dependencies
RUN pip install --no-cache-dir kivy

# Set working directory
WORKDIR /app

# Copy project files
COPY . /app

# Run the app
CMD ["python3", "lumina_app.py"]

FROM python:3.10-slim

# Install system dependencies for Kivy
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libgl1-mesa-glx \
    libgles2-mesa \
    libsdl2-dev \
    libsdl2-image-dev \
    libsdl2-mixer-dev \
    libsdl2-ttf-dev \
    libgstreamer1.0-dev \
    gstreamer1.0-plugins-base \
    gstreamer1.0-plugins-good \
    gstreamer1.0-tools \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip and install Kivy
RUN pip install --upgrade pip && pip install --no-cache-dir kivy

# Set working directory
WORKDIR /app

# Copy application files
COPY . .

# Run the application
CMD ["python", "main.py"]
FROM python:3.10-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx libgles2-mesa sdl2 sdl2-image sdl2-mixer sdl2-ttf \
    && pip install --no-cache-dir kivy

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Run the application
CMD ["python", "main.py"]

