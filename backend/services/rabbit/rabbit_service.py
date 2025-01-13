import json
import uuid

import pika

from backend.services.rabbit.constants import DEFAULT_EXCHANGE


class RabbitMQService(object):
    @staticmethod
    def manual_close_connection(instance):
        if instance is not None and instance.connection.is_closed is False:
            instance.connection.close()

    @staticmethod
    def basic_publish(self, body, routing_key, properties_headers=None):
        properties = pika.BasicProperties(
            correlation_id=self.corr_id,
        )
        if properties_headers:
            properties = pika.BasicProperties(
                correlation_id=self.corr_id, headers=properties_headers
            )
        self.channel.basic_publish(
            exchange=DEFAULT_EXCHANGE,
            routing_key=routing_key,
            properties=properties,
            body=json.dumps(body),
        )
        print('sended')
        self.connection.close()
        return {
            "status": 9000,
            "statusMessage": "Request is published to queue: " + routing_key,
        }

    @staticmethod
    def basic_request(self, body, routing_key, time_limit=None):
        msg = body.copy()

        self.corr_id = str(uuid.uuid4())

        self.channel.basic_publish(
            exchange=DEFAULT_EXCHANGE,
            routing_key=routing_key,
            properties=pika.BasicProperties(
                correlation_id=self.corr_id,
                reply_to=self.reply_queue.method.queue,
            ),
            body=json.dumps(body),
        )
        self.connection.process_data_events(time_limit=time_limit or 100)

        self.connection.close()
        return self.response
