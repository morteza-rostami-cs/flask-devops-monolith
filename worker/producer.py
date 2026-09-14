# import pika

from shared.rabbitmq import get_connection

# rabbitmq connection
connection = get_connection()
# what is a channel?
channel = connection.channel()

# create a message queue
channel.queue_declare(queue="devops_test")

channel.basic_publish(
    exchange="",
    routing_key="devops_test",
    body="hello rabbitmq",
)

print("Message published")

connection.close()
