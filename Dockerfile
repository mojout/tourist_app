
FROM python:3.11

WORKDIR /usr/src/tourist_app_drf

COPY ./requirements.txt /usr/src/requirements.txt

RUN pip install -r /usr/src/requirements.txt

COPY . /usr/src/tourist_app_drf

RUN pip install --upgrade pip

#EXPOSE 8000
#
#CMD ["python", "manage.py", "migrate"]
#
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]




# copy project
