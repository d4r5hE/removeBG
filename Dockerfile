FROM python:3.9.1-alpine

WORKDIR /removeBG

ADD . /removeBG

RUN pip install -r requirements.txt

CMD ["python","app.py"]
