# producer
# admin panel http://localhost:15672
from kombu import Connection, Exchange, Queue, Producer
from datetime import datetime, timedelta


connection = Connection('amqp://localhost:5672')
channel = connection.channel()

exchange = Exchange('dick_pro_3', type='direct')
producer = Producer(
    channel=channel,
    exchange=exchange,
    serializer='pickle',
    routing_key="direct.routing.key"
)
producer.publish(
    {'hello': 'world2', "date": datetime.now(), "delta": timedelta(hours=5)},
    headers={"Pidor": True}
)

connection.release()