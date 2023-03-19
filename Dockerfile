FROM python:3.8.12
RUN mkdir /storage
WORKDIR /storage
COPY . /storage/
RUN pip install -r requirements.txt
CMD gunicorn --bind 0.0.0.0:8081 form_test.wsgi
