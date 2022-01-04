# producer
# admin panel http://localhost:15672
from kombu import Connection

connection = Connection("amqp://localhost:5672")
queue = connection.SimpleQueue("test_queue")
queue.put({"data": "hello world"})
connection.close()