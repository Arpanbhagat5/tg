# Use an official Python image
FROM python:3.10

# Set the working directory
WORKDIR /app/backend

# Update and check availability
RUN apt-get update || echo "Failed to update apt repositories"


# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy start.sh and make it executable
COPY start.sh /app/start.sh
RUN chmod +x /app/start.sh

# Copy project files
COPY . .

# Expose the port Django runs on
EXPOSE 8000

# Use start.sh to handle migrations and start Django
CMD ["/app/start.sh"]

