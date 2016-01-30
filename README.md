PythonRoombots
==============

This is a little library that can act as a programmatic client for connecting to and driving [a roombot](http://roombots.riesd.com/).

To connect to the roombot simulator you would clone this repository and run a command like:

```
python roombots.py --roomba-host roombots.riesd.com --channel YOUR_UNIQUE_CHANNEL
```

To connect to a physical roombot you can use the default channel and just point to the IP address of the roombot:

```
python roombots.py --roomba-host 192.168.0.0.2
```

You will see a lot of output about the messages received and sent by this client so you can decide how to customize it.


## Getting Started

Make sure you install the dependencies found in the `requirements.txt` file found in the root of this project.

```
pip install -r requirements.txt
```


## Customizing

To customize, open up `roombots.py` and begin coding the Roomba around the maze.


## Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/film42/python_roombots. This project is intended to be a safe, welcoming space for collaboration, and contributors are expected to adhere to the [Contributor Covenant](contributor-covenant.org) code of conduct.


## License

The gem is available as open source under the terms of the [MIT License](http://opensource.org/licenses/MIT).
