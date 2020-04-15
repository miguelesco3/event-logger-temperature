import logging
from multiprocessing import Queue

from models.record import Record
from entities.message import Message
from services.database_service import DataBaseService
from services.background_worker import BackgroundWorker


class DatabaseWorker(BackgroundWorker):
    def __init__(self,
                 db_service: DataBaseService,
                 input_queue: Queue = None,
                 output_queue: Queue = None,
                 sleep_time: float = 0.01):
        super().__init__(input_queue, output_queue, sleep_time)
        self._db_service = db_service

    def _target(self, message: Message):
        try:
            record = Record(topic=message.topic, payload=message.payload)
            session = self._db_service.get_session()
            session.add(record)
            session.commit()
            logging.info(f'Record stored!')
        except Exception as e:
            logging.error(e)
