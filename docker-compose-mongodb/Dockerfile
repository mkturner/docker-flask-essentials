# Specify python version
FROM python:3.8.11-slim

# Create and change into working directory
RUN mkdir /counter_app
WORKDIR /counter_app

# Copy project files
ADD . .

# Install dependencies from requirements file
RUN pip install -r requirements.txt

# Allow ingress where app will listen
EXPOSE 5000

# Run app
CMD python manage.py runserver