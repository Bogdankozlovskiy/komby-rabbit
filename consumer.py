# consumer
# admin panel http://localhost:15672   (guest|guest)
from kombu import Connection, Exchange, Queue, Consumer
from kombu.exceptions import TimeoutError
from contextlib import suppress


connection = Connection('amqp://localhost:5672')
channel = connection.channel()

exchange_1 = Exchange('dick_pro_1', type='topic', channel=channel)
exchange_1.declare()
exchange_2 = Exchange('dick_pro_2', type='fanout', channel=channel)
exchange_2.declare()
exchange_3 = Exchange('dick_pro_3', type='direct', channel=channel)
exchange_3.declare()

queue_1 = Queue(name="vagina_1", channel=channel)
queue_1.declare()
queue_2 = Queue(name="vagina_2", channel=channel)
queue_2.declare()
queue_3 = Queue(name="vagina_3", channel=channel)
queue_3.declare()
queue_4 = Queue(name="vagina_4", channel=channel)
queue_4.declare()

queue_1.bind_to(exchange=exchange_1, routing_key="#.stock.#", channel=channel)
queue_2.bind_to(exchange=exchange_1, routing_key="*.stock.#", channel=channel)
queue_3.bind_to(exchange=exchange_1, routing_key="#.stock.*", channel=channel)
queue_4.bind_to(exchange=exchange_2, routing_key="bla.bla.bla", channel=channel)
queue_3.bind_to(exchange=exchange_3, routing_key="direct.routing.key", channel=channel)

consumer = Consumer(
    channel=channel,
    queues=[queue_1, queue_2, queue_3, queue_4],
    accept=['json', "yaml", "pickle"],
    on_message=lambda message: (print(message.headers, message.payload), message.ack())
)

with (consumer, suppress(TimeoutError)):
    connection.drain_events(timeout=2)

connection.release()