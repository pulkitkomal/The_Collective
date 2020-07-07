FROM python:3-onbuild
COPY . /usr/src/app
RUN pip install -U flask-cors
CMD ["python","app.py"]