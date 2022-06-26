import paho.mqtt.client as mqtt
from time import sleep

# Set the IP address and port number of the MQTT broker
broker_ip = "192.168.1.152"
broker_port = 1883
device_id = "fan01"

# setup the topics
topic = "home/bathroom/" + device_id
status_topic = topic + "/state"

def status_callback(client, userdata, message):
    """ This function is called when a message is received on the status topic. """
    status_message = ""
    print(f'message: {str(message.payload.decode("utf-8"))}, userdata: {userdata}, message.topic: {message.topic}')

    # Split the topic string up into a list of strings
    topics = message.topic.split("/")

    # Check if the topic is the status topic
    last_topic = topics[-1]
    if last_topic == "state":

        # Return a status message
        status_message = f"{device_id} is Happy and Ok"
        client.publish(topic, status_message)

    print("status_message: " + status_message)
    return status_message

# create a node
fan = mqtt.Client()
fan.connect(broker_ip, broker_port)
fan.on_message = status_callback

# Start the loop and subscribe
fan.loop_start()
fan.subscribe(status_topic)

# Send birthing message
fan.publish(topic + "/birthing_message", f"{device_id} Ready")

print("press CTRL + C to quit")
while True or KeyboardInterrupt:
    # Do nothing, and let the loop run
    sleep(0.5)