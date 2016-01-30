from driver import Driver
from cli import CLI

#
# Helper class that will wrap a sensor update message.
#
class SensorUpdate(object):
    def __init__(self, payload):
        self.light_bumper_right_front = payload["light_bumper_right_front"]
        self.light_bumper_right_center = payload["light_bumper_right_center"]
        self.light_bumper_right = payload["light_bumper_right"]
        self.light_bumper_left_front = payload["light_bumper_left_front"]
        self.light_bumper_left_center = payload["light_bumper_left_center"]
        self.light_bumper_left = payload["light_bumper_left"]
        self.bumper_right = payload["bumper_right"]
        self.bumper_left = payload["bumper_left"]

#
# The Roombot Client
#
# This is where you will want to write your code to driver the roombot
# around the maze.
#
class Roombot(Driver):
    # This method is called when we join th channel, this is where
    # you can execute your first drive command!
    def on_start(self):
        # You can use the self.drive method to send a command.
        self.drive({ "velocity" : 100, "radius" : 0 })

    # This method is called with a Dict of messages coming over the
    # websocket. Most messages are not useful, but you can use this as
    # a place to route your messages, like to self.on_sensor_update.
    def on_message(self, message):
        if message["event"] == "sensor_update":
            sensor_update = SensorUpdate(message["payload"])
            self.on_sensor_update(sensor_update)

    # This method is called when we get a sensor update message.
    def on_sensor_update(self, sensor_update):
        print "Sensor update received!"

        if sensor_update.light_bumper_right_center == 1:
            self.drive({ "velocity" : 100, "radius" : 5 })


#
# Runner
#
if __name__ == "__main__":
    # This will parse out the host and channel options
    cli = CLI()

    # This will connect your Roombot to the simulator, or Roomba and
    # setup a heartbeat that checks-in with the host every second.
    # Once everything is connected, your Roombot's self.on_start method
    # will be called.
    roombot = Roombot(cli.host, cli.channel, uses_heartbeat=True)
