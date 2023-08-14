# events_handing_task

The Event emitter service --> listens to incoming events using amqp connection and sends the request to the Event Handler service.

The Event Handler service --> listens to the event emitter service using api's and process the request and saves in to DB
