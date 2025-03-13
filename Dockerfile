FROM python:3.9
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

# Ensure PORT is available, defaulting to 5000 if not set
CMD gunicorn --workers=4 --bind 0.0.0.0:${PORT:-5000} app:app
    
