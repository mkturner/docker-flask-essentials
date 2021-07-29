# Specify base image, recent version of Python
FROM python:3.8.11-alpine

# Create a working directory
RUN mkdir /opt/flask_app

# Change into WORKDIR, copy requirements file
WORKDIR /opt/flask_app
ADD requirements.txt .

# Install Python Dependencies
RUN pip install -r requirements.txt

# ADD Flask/Project Files into WORKDIR
ADD . .

# Expose port 5000 where Flask will run
EXPOSE 5000

# Set Entry point for Flask
ENV FLASK_APP=hello.py

# Run Flask, Allow ingress
CMD ["flask", "run", "--host", "0.0.0.0"]