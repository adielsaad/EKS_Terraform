FROM python:alpine
RUN pip3 install flask requests gunicorn
EXPOSE 5000
WORKDIR /app
COPY . .
CMD gunicorn --bind 0.0.0.0:5000 wsgi:app

