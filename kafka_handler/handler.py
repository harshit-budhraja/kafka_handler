# venv:- python3
from confluent_kafka import Producer, Consumer, KafkaError
import sys
import traceback

LOG_PREFIX = "Logs from Kafka Handler: "

class Handler():
    def __init__(self, verbose = False):
        self.verbose = verbose

    def logThis(self, message):
        if self.verbose == True:
            print(LOG_PREFIX + message)
    
    def on_send_success(self, err, msg):
        if err is not None:
            self.logThis('Message delivery failed: {}'.format(err))
        else:
            self.logThis('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))

    def Consumer(self, options):
        self.logThis("Setting consumer to group " + str(options.get("group.id")) + " on server: " + str(options.get("bootstrap.servers")))
        return Consumer(options)

    def Producer(self, options):
        self.logThis("Initialising a producer on server " + str(options.get("bootstrap.servers")))
        return Producer(options)

    def subscribe(self, consumer, topics):
        if isinstance(consumer, Consumer) == True:
            consumer.subscribe(topics)
            self.logThis("Consumer is subscribed to => " + str(topics))
            return True
        else:
            raise Exception(LOG_PREFIX + "Expects a Kafka Consumer object as argument instead of => " + str(type(consumer)))

    def produce(self, producer, topic, message):
        if isinstance(producer, Producer) == True:
            self.logThis("Produced message => \n" + message)
            producer.produce(topic, message, callback=self.on_send_success)
            return True
        else:
            raise Exception(LOG_PREFIX + "Expects a Kafka Producer object as argument instead of => " + str(type(producer)))

    def flush(self, producer):
        if isinstance(producer, Producer) == True:
            producer.flush()
            return True
        else:
            raise Exception(LOG_PREFIX + "Expects a Kafka Producer object as argument instead of => " + str(type(producer)))

    def consume(self, consumer, handleMessageReceived):
        if isinstance(consumer, Consumer) == True:
            while True:
                msg = consumer.poll(1.0)
                if msg is None:
                    continue
                if msg.error():
                    self.logThis("Consumer error: {}".format(msg.error()))
                    continue
                self.logThis('Received message: {}'.format(msg.value().decode('utf-8')))
                try:
                    handleMessageReceived(msg.value().decode('utf-8'))
                except Exception as e:
                    print(e)
                    traceback.print_exc()
            consumer.close()
        else:
            raise Exception(LOG_PREFIX + "Expects a Kafka Consumer object as argument instead of => " + str(type(consumer)))
