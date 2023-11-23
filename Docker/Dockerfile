# Use an official Python runtime as a base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the Python script into the container at /app
COPY SecGenPass.py Docker/httpServer.py /app/

# Add appuser and Set the entrypoint script as executable and change ownership
RUN adduser --disabled-password --gecos '' appuser && \
    chmod +x /app/httpServer.py && \
    chown -R appuser /app

# Expose the container's port
EXPOSE 80

# Change to the non-root user
USER appuser

# Define the entrypoint script to start the HTTP server
ENTRYPOINT ["/app/httpServer.py"]
