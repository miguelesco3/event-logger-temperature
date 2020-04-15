import logging
import settings

from multiprocessing import Queue
from services.mqtt_client import MQTTClient
from services.ChangeUnitsWorker import ChangeUnitsWorker

input_event_queue = Queue()
output_event_queue = Queue()


client = MQTTClient(
    input_queue=input_event_queue,
    output_queue=output_event_queue,
    topics=['esp32/temperatura', 'esp32/humedad'])
client.connect(host=settings.MQTT_HOST,
               port=settings.MQTT_PORT)


transform = ChangeUnitsWorker(
    input_queue=input_event_queue,
    output_queue=output_event_queue
)


if __name__ == "__main__":
    logging_mode = logging.INFO
    logging.basicConfig(format='%(asctime)s.%(msecs)s:%(name)s:%(thread)d:%(levelname)s:%(process)d:%(message)s',
                        level=logging_mode)
    transform.start()
    client.loop_forever()
