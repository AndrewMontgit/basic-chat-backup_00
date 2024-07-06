FROM evennia/evennia:latest

# Copy requirements.txt from the project directory to the container
COPY requirements.txt /usr/src/game/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r /usr/src/game/requirements.txt

# Copy the mygame directory to the container
COPY mygame /usr/src/game

# Set the working directory
WORKDIR /usr/src/game

# Default command to run Evennia
CMD ["evennia", "start", "-l"]
