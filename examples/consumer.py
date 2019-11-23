from kafka_handler import Handler

def test(message):
    print(message)

k = Handler(verbose=True)

consumer = k.Consumer({
    'bootstrap.servers': "localhost:9092",
    'group.id': "test",
    'auto.offset.reset': 'latest',
    'enable.auto.commit': True
})

k.subscribe(consumer, ["test"])
k.consume(consumer, test)
