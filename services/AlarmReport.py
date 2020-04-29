import logging
import json
from collections import defaultdict
from services.background_worker import BackgroundWorker
from multiprocessing import Queue
from entities.message import Message


class AlarmReport(BackgroundWorker):
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
                payload['temperature'] = self.alarmCheck(input_payload['temperature'])
            if len(payload.keys()):
                self._output_queue.put(
                    Message(topic='Output', payload=json.dumps(payload).encode()))

        except Exception as e:
            logging.error(e)

    @staticmethod
    def alarmCheck(celsius: float = 0) -> float:
        if celsius > 30:
            return "ALERTA: Temperatura muy elevada"
        else:
            return "Temperatura normal"

