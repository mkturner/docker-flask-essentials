# Specify base image, recent version of Python
FROM python:3.8.11-alpine

# Create a working directory
RUN mkdir /app

# Change into WORKDIR, copy requirements & project files
WORKDIR /app
ADD . .

# Install Python Dependencies
RUN pip install -r requirements.txt

# Expose port where gunicorn will listen
EXPOSE 80

# Run Flask on gunicorn
# app:app means app module : app file
# -b means bind ports
# --workers means how many processes to run
# --reload means reload if any changes
CMD ["gunicorn", "app:app", "-b", "0.0.0.0:80", "--workers", "4", "--reload"]