```text

# rabbitMQ fundamentals:

producer -> exchange -> queue -> consumer

Producer

The application that publishes a message.

Eventually:

Flask API = producer
Exchange

Receives published messages and decides where they should go.

Queue

Stores messages until a consumer receives them.

Consumer

The process that receives and processes messages.

```
