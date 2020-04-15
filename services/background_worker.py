import abc
import queue
import logging
from time import sleep
from entities.message import Message
from multiprocessing import Process, Queue


class BackgroundWorker(abc.ABC):
    def __init__(self,
                 input_queue: Queue = None,
                 output_queue: Queue = None,
                 sleep_time: float = 0.01):
        self._input_queue = input_queue
        self._output_queue = output_queue
        self._sleep_time = sleep_time

    @abc.abstractmethod
    def _target(self, message: Message):
        pass

    def start(self):
        Process(target=self._target_wrapper, daemon=True).start()

    def _target_wrapper(self):
        while True:
            if not self._input_queue.empty():
                try:
                    message = self._input_queue.get_nowait()
                except queue.Empty:
                    break

                if message:
                    logging.info(f'Worker: {self.__class__.__name__} | message: {message.to_dict()}')
                    self._target(message=message)

            sleep(self._sleep_time)
