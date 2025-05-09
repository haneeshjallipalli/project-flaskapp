# Use a lightweight Python base image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /devops/devopsuser

# Create a non-root user and group for better security
RUN addgroup --system devopsgroup && adduser --system --ingroup devopsgroup devopsuser

# Switch to the non-root user
USER devopsuser

# Copy the application code and requirements file into the container
COPY . .

USER root 
RUN pip install --upgrade pip

# Install Python dependencies without caching to reduce image size
RUN pip install --no-cache-dir -r requirements.txt

USER devopsuser

# Expose the port the application will run on (default Flask port)
EXPOSE 5000

# Define the entry point to run the Python application
ENTRYPOINT [ "python", "app.py" ]
