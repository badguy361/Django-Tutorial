FROM python:3.8.12
RUN mkdir /storage
WORKDIR /storage
COPY . /storage/
RUN pip install -r requirements.txt
CMD python manage.py runserver 0.0.0.0:8080
