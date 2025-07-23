from confluent_kafka import Consumer
import threading
from app.segmentation import segment_pdf

def listen():
    consumer = Consumer({
        'bootstrap.servers': 'localhost:9092',
        'group.id': 'edip-ml-group',
        'auto.offset.reset': 'earliest'
    })
    consumer.subscribe(['document.uploaded'])

    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            print("Kafka error: {}".format(msg.error()))
            continue
        doc_id = msg.value().decode('utf-8')
        print(f"[Kafka] Received document ID: {doc_id}")
        segment_pdf(doc_id)

def start_kafka_listener():
    thread = threading.Thread(target=listen, daemon=True)
    thread.start()
