import logging
import queue
from typing import List
from time import sleep
from entities.message import Message
import paho.mqtt.client as mqtt
from multiprocessing import Queue
from threading import Thread

from entities.message import Message


class MQTTClient(mqtt.Client):
    def __init__(self, input_queue: Queue, output_queue: Queue, topics: List[str] = None, sleep: float = 0.01):
        super().__init__()
        self._topics = topics or []
        self._input_queue = input_queue
        self._output_queue = output_queue
        self.on_connect = self.on_connect_handler
        self.on_message = self.on_message_handler
        self._sleep_time = sleep
        Thread(target=self._run, daemon=True).start()

    def on_connect_handler(self, client, userdata, flags, rc):
        for topic in self._topics:
            self.subscribe(topic=topic)
            logging.info(f'Subscribed to topic: {topic}')
        logging.info("Connected with result code " + str(rc))

    def on_message_handler(self, client, userdata, msg):
        self._input_queue.put(Message(topic=msg.topic, payload=msg.payload))
        logging.info(f'Topic: {msg.topic} | Message: {msg.payload.decode()}')

    def _run(self):
        while True:
            if not self._output_queue.empty():
                try:
                    message = self._output_queue.get_nowait()
                except queue.Empty:
                    break

                if message:
                    self.publish(topic=message.topic, payload=message.payload)

            sleep(self._sleep_time)
