import logging
import json
from collections import defaultdict
from services.background_worker import BackgroundWorker
from multiprocessing import Queue
from entities.message import Message


class ChangeUnitsWorker(BackgroundWorker):
    def __init__(self,
                 input_queue: Queue = None,
                 output_queue: Queue = None,
                 sleep_time: float = 0.01):
        super().__init__(input_queue, output_queue, sleep_time)

    def _target(self, message: Message):
        try:
            input_payload = json.loads(message.payload)
            payload = defaultdict()
            if input_payload.get('temperature'):
                payload['temperature'] = self.to_fahrenheit(input_payload['temperature'])
            if len(payload.keys()):
                self._output_queue.put(
                    Message(topic='Output', payload=json.dumps(payload).encode()))

        except Exception as e:
            logging.error(e)

    @staticmethod
    def to_fahrenheit(celsius: float = 0) -> float:
        return celsius * 1.8 + 32

    @staticmethod
    def km_to_miles(kilometers: int) -> float:
        return kilometers * 0.62