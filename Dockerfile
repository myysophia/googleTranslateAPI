FROM python:3.8-alpine
COPY ./*.py /app
WORKDIR /app
RUN /bin/bash -c 'pwd;ls -l /app'
#RUN  /usr/local/bin/python -m pip install --upgrade pip
#RUN pip3 install redis==3.5.3
cmd ["python", "/app/Google Translate.py"]
