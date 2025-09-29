# Link to Github repo: https://github.com/Kiktur/ee250-labs

"""EE 250L Lab 04 Starter Code
Run vm_pub.py in a separate terminal on your VM."""

import paho.mqtt.client as mqtt
import time

"""This function (or "callback") will be executed when this client receives 
a connection acknowledgement packet response from the server. """

def on_connect(client, userdata, flags, rc):
    """Once our client has successfully connected, it makes sense to subscribe to
    all the topics of interest. Also, subscribing in on_connect() means that, 
    if we lose the connection and the library reconnects for us, this callback
    will be called again thus renewing the subscriptions"""

    print("Connected to server (i.e., broker) with result code "+str(rc))
    #replace user with your USC username in all subscriptions
    client.subscribe("vagutier/ping")
   
    
    #Add the custom callbacks by indicating the topic and the name of the callback handle
    client.message_callback_add("vagutier/pong", on_message_from_ping)


"""This object (functions are objects!) serves as the default callback for 
messages received when another node publishes a message this client is 
subscribed to. By "default,"" we mean that this callback is called if a custom 
callback has not been registered using paho-mqtt's message_callback_add()."""
def on_message(client, userdata, msg):
    # print("Custom callback  - topic: "+msg.payload.decode())
    print("Default callback - topic: " + msg.topic + "   msg: " + str(msg.payload, "utf-8"))
    converted_msg = int(msg.payload.decode())
    print("Custom callback  - Ping Message: "+msg.payload.decode())
    num = converted_msg + 1
    client.publish("vagutier/pong", str(num))
    time.sleep(1)


#Custom message callback.
def on_message_from_ping(client, userdata, message):
   converted_msg = int(message.payload.decode())
   print("Custom callback  - Ping Message: "+message.payload.decode())
   num = converted_msg + 1
   client.publish("vagutier/pong", str(num))
   time.sleep(1)


if __name__ == '__main__':
    
    #create a client object
    client = mqtt.Client()
    #attach a default callback which we defined above for incoming mqtt messages
    client.on_message = on_message
    #attach the on_connect() callback function defined above to the mqtt client
    client.on_connect = on_connect

    client.connect(host="10.94.188.246", port=1883, keepalive=60)

    client.loop_forever()
    time.sleep(1)
