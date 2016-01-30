import optparse

class CLI(object):
    def __init__(self):
        parser = optparse.OptionParser(usage = "%prog [options]", version = "%prog 0.1")

        # Roomba host option
        parser.add_option("-r", "--roomba-host", type="str", dest="roomba_host", default="roombots.riesd.com",
                          help="The host of the simulator, or ip of the roomba.")
        # Channel option
        parser.add_option("-c", "--channel", type="str", dest="channel", default="roomba",
                          help="The name of the channel you're using. Only change this if you're using the simulator.")

        (options, args) = parser.parse_args()
        self.host = options.roomba_host
        self.channel = options.channel
