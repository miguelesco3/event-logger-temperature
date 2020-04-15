from json import loads
import datetime as dt


class Message:
    def __init__(self, topic: str, payload: bytes, json: bool = False):
        self._created_at = dt.datetime.now().strftime("%m-%d-%Y %H:%M:%S")
        self._topic = topic
        self._payload = loads(payload.decode()) if json else payload.decode()

    @property
    def topic(self):
        return self._topic

    @property
    def payload(self):
        return self._payload

    def to_dict(self):
        return {
            'topic': self._topic,
            'payload': self._payload,
            'created_at': self._created_at,
        }
