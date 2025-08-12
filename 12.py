import paho.mqtt.client as mqtt
import time
import random

BROKER = "test.mosquitto.org"  # Public MQTT broker
PORT = 1883
TOPIC = "demo/mqtt/example"

# Callback when a message is received
def on_message(client, userdata, msg):
    print(f"[Subscriber] Received: {msg.payload.decode()} from topic: {msg.topic}")

# Create MQTT client
client = mqtt.Client()

# Attach the message handler
client.on_message = on_message

# Connect to broker
print("[System] Connecting to broker...")
client.connect(BROKER, PORT, keepalive=60)

# Subscribe to the topic
client.subscribe(TOPIC)
print(f"[Subscriber] Subscribed to topic: {TOPIC}")

# Start network loop in the background
client.loop_start()

try:
    while True:
        # Create random temperature data
        temperature = round(random.uniform(20.0, 30.0), 2)
        message = f"Temperature: {temperature} °C"

        # Publish message
        client.publish(TOPIC, message)
        print(f"[Publisher] Sent: {message}")

        time.sleep(2)

except KeyboardInterrupt:
    print("\n[System] Disconnecting...")
    client.loop_stop()
    client.disconnect()
    print("[System] Disconnected.")
