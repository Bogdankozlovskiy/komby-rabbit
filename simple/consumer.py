# consumer
# admin panel http://localhost:15672
from kombu import Connection
from contextlib import suppress

connection = Connection("amqp://localhost:5672")
queue = connection.SimpleQueue("test_queue")

with suppress(queue.Empty):
    messsage = queue.get(block=True, timeout=2)
    print(messsage.payload)
    messsage.ack()

queue.close()
connection.close()