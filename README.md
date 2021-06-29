# Kafka Producer & Consumer - A First Glance

## Abstract

This is a simple application to demonstrate the Kafka module for Python, with a simple producer and a simple consumer group. The Kafka distribution from [confluent.io][confluent] was used and video course followed was [Apache Kafka for Absolute Beginners][videocourse]

## Environment Variables

These variables can be set in the `.env` file and provide the necessary parameters for the application to run.

- **SERVERS:** The servers URL for the `bootstrap servers` and `broker list` parameters
- **TOPIC:** The topic name
- **DATA_FILE:** The data file location, used as the source data for the producer
- **CONSUMER_GROUP:** The name of the consumer group

## Producer

The producer can be started with the following code

```shell
\> python -m pyprod.producer
```

The producer will send the same `DATA_FILE` repeatedly, at 5-second intervals.

## Consumer

The consumer will read the messages from the topic and display on the console. If using the Python version, this command will run the application:

```shell
\> python -m pyprod.consumer
```

## Docker For the Consumer

A Docker image can be built with the included `Dockerfile`.

### Building the Image

```shell
\> docker build -t kafkaconsumer:0.0.1
```

The tag name can be changed to suit the needs of the application.

### Running the Image in a Named Container

```shell
\> docker run --env-file <environment_file> --name kconsumer01 kafkaconsumer:0.0.1
```

The container name is just a suggestion. The original test was made with a consumer group containing three consumer applications, `kconsumer01`, `kconsumer02`, and `kconsumer03`.

The `environment_file` should contain all environment variables from above.

## Author

Please contact [Gus Garcia][mailto] for any comments, critics, or questions.

[confluent]: https://www.confluent.io
[videocourse]: https://learning.oreilly.com/videos/apache-kafka-for/9781800202054/
[mailto]: mailto:pythongus@gmail.com
