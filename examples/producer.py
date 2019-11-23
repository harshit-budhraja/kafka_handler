from kafka_handler import Handler

k = Handler(verbose=True)

producer = k.Producer({'bootstrap.servers': "localhost:9092"})


def startManualTest():
    while True:
        m = str(input("Message to Produce => "))
        k.produce(producer, "test", m)
        k.flush(producer)

startManualTest()
