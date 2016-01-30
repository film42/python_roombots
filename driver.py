import json
import websocket
import thread
import time

# Disable verbose socket output. It's not that useful.
# websocket.enableTrace(True)

class Driver(object):
    def __init__(self, host, channel, uses_heartbeat=True):
        self.host = host
        self.channel = channel
        self.uses_heartbeat = uses_heartbeat
        self.socket = websocket.WebSocketApp("ws://%s/socket/websocket?vsn=1.0.0" % self.host,
                                             on_message = self.on_raw_message,
                                             on_open = self.on_open)

        # Now we will only listen to updates from the websocket!
        self.socket.run_forever()

    def drive(self, message):
        drive_message = {
            "topic" : self.channel,
            "event" : "drive",
            "ref" : 15,
            "payload" : message,
        }

        self.send(drive_message)

    def setup_heartbeat(self):
        while True:
            heartbeat_message = {
                "topic" : "phoenix",
                "event" : "heartbeat",
                "payload": {},
                "ref": 10,
            }

            time.sleep(1)
            self.send(heartbeat_message)


    def on_open(self, _socket):
        join_message = {
            "topic" : self.channel,
            "event" : "phx_join",
            "payload" : {},
            "ref" : 1,
        }

        self.send(join_message)

    def on_message(self):
        raise Exception("self.on_message needs to be implemented by you!")

    def on_raw_message(self, _socket, json_message):
        message = json.loads(json_message)

        print "Received message:", message

        if message["event"] == "phx_reply" and message["ref"] == 1:
            print "Channel has been joined, you can now send drive commands!"

            if self.uses_heartbeat:
                print "Setting up a heartbeat"
                thread.start_new_thread(self.setup_heartbeat, ())

            self.on_start()
        else:
            self.on_message(message)

    def on_start(self):
        raise Exception("self.on_start needs to be implemented by you!")

    def on_sensor_update(self, sensor_update):
        raise Exception("self.on_sensor_update needs to be implemented by you!")

    def send(self, message):
        print "Sending message:", message
        self.socket.send(json.dumps(message))
