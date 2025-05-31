#Use an official Python runtime as the base image
FROM python:3.10-slim

#Set working directory in the container
WORKDIR /app

#Install system dependencies
RUN apt-get update && apt-get install -y

nginx

supervisor

&& rm -rf /var/lib/apt/lists/*

#Copy requirements.txt and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

#Copy the project files into the container
COPY . .

#Configure Nginx
COPY nginx.conf /etc/nginx/sites-available/default
RUN ln -sf /etc/nginx/sites-available/default /etc/nginx/sites-enabled/default

Configure Supervisor to manage uWSGI and Nginx
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

Expose port 80 for Nginx
EXPOSE 80

Start Supervisor to manage processes
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
