import os

PG_HOST = os.getenv('PG_HOST', '0.0.0.0')
PG_PORT = os.getenv('PG_PORT', 5432)
PG_USERNAME = os.getenv('PG_USERNAME', 'vcamargo')
PG_PASSWORD = os.getenv('PG_PASSWORD', 'maxwell')
DATABASE = os.getenv('DATABASE', 'sda_device')

MQTT_HOST = os.getenv('MQTT_HOST', '192.168.43.155')
MQTT_PORT = os.getenv('MQTT_PORT', 1883)
