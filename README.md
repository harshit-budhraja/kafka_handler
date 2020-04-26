[![Open Source](https://badges.frapsoft.com/os/v2/open-source-175x29.png?v=103)](https://github.com/ellerbrock/open-source-badges/) [![GitHub Stars](https://img.shields.io/github/stars/harshit-budhraja/kafka_handler.svg)](https://github.com/harshit-budhraja/kafka_handler/stargazers) [![GitHub Issues](https://img.shields.io/github/issues/harshit-budhraja/kafka_handler.svg)](https://github.com/harshit-budhraja/kafka_handler/issues) [![Current Version](https://img.shields.io/badge/version-1.0.4-green.svg)](https://pypi.org/project/kafka-handler/)

# kafka_handler

A simple, easy-to-use, beginner-friendly Kafka wrapper based on `confluent_kafka`'s python client. Some specific features and improvements it offers wrapping around the official module are:

* No specific need to import the parent module. We can just install this kafka_handler and we're good to go.
* No manual consumer polling required. This handler takes care of it.
* Efficient callbacks for consumer, making the code much simpler. We just need to take care of the essential aspects of what to do with the message, leave the rest to this handler.


# Installation

This is freely available on Pypi - the official package repository for python. To install it to your environment:

`pip install kafka-handler`

P.S. You can optionally choose to install it to a `virtualenv` of your choice. To do that:

1. Activate your python virtual environment - `source <PATH_TO_YOUR_VENV>/bin/activate`
2. Now install using pip - `pip install kafka-handler`


# Usage

* Import the Handler into your python code.

    `from kafka_handler import Handler`
<br>
* Create an object instance of the handler. You can optionally pass an argument `verbose` as `True` or `False` to enable or disable advanced logging from within the handler. By default, the verbosity is set to `False`.

    `k = Handler(verbose=True)`
<br>

#### Producer

To use the producer, instantiate the producer using the object of the Handler created above.

`producer = k.Producer({'bootstrap.servers': "localhost:9092"})`

You can pass the `options` object that you would otherwise pass to the `confluent_kafka` module here, as is. In the above line, the `bootstrap.server` is passed as an option, where our Kafka Broker is running. To know more about these options, you can refer to https://github.com/confluentinc/confluent-kafka-python.

To produce a message to a topic "TEST_TOPIC":

```
k.produce(producer, "TEST_TOPIC", <YOUR_MESSAGE>)
k.flush(producer)
```

NOTE: Remember to flush the producer buffer after producing the message.

An example of the same can be found in `examples/producer.py`.


#### Consumer

To use the consumer, instantiate the consumer using the object of the Handler created above.

```
consumer = k.Consumer({
    'bootstrap.servers': "localhost:9092",
    'group.id': "test",
    'auto.offset.reset': 'latest',
    'enable.auto.commit': True
})
```

You can pass the `options` object that you would otherwise pass to the `confluent_kafka` module here, as is. In the above line, the `bootstrap.servers`, `group.id`, `auto.offset.reset`, `enable.auto.commit` are some options passed. To know more about these options, you can refer to https://github.com/confluentinc/confluent-kafka-python.

Then, subscribe to some topic(s) like:

`k.subscribe(consumer, ["TEST_TOPIC"])`

To consume an incoming message from the topic, pass a callback function like:

`k.consume(consumer, YOUR_CALLBACK_FUNCTION)`

An example of the same can be found in `examples/consumer.py`.


# Contributions

All suggestions, feedback and contributions are greatly appreciated. Please refer to `CONTRIBUTING.md` for further details.

# License

```
GNU GENERAL PUBLIC LICENSE
Version 3, 29 June 2007
```

 The complete license terms can be found in `LICENSE` file in this repository.