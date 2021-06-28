FROM python:alpine

WORKDIR /usr/src/app

RUN mkdir ./pyprod

COPY ./pyprod/* /usr/src/app/pyprod

RUN pip install kafka-python python-dotenv

ENTRYPOINT ["python"]

CMD ["-m", "pyprod.consumer"]