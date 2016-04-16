# IRL Alerts
Are your viewers looking for some excitement in your stream?

Looking for a way to reward them for their generous contributions by having real world consequences happen upon receiving a donation or a subscription?

Well, you're in the right place.

## Installation
### Virtual Environment
I would recommend running this in a virtual environment to keep your dependencies in check. If you'd like to do that, run:

```shell
sudo pip install virtualenv
```

Followed by:

```shell
virtualenv venv
```

This will create an empty virtualenv in your project directory in a folder called "venv." To enable it, run:

```shell
source venv/bin/activate
```

and your console window will be in that virtualenv state. To deactivate, run:

```shell
deactivate
```

### Dependencies
To install all dependencies locally (preferably inside your activated virtualenv), run:

```shell
pip install -r requirements.txt
```

### Further Steps
- Make a copy of the example config file:

```shell
cp config_example.py config.py
```

- Follow the instructions on the [Particle Documentation](https://docs.particle.io/guide/getting-started/start/photon/) to get your device hooked up to the Internet.
- Take the code from `irlalerts.ino` and place it in the [Particle Build](https://build.particle.io/build/new) area, then flash it to your device. You can get the `access_token` for `config.py` from this area in the `settings` tab.

## Interacting with the Thing
Start the server by running:

```shell
python server.py
```

Then, head to [http://127.0.0.1:5000/donation/](http://127.0.0.1:5000/donation/) or [http://127.0.0.1:5000/subscription/](http://127.0.0.1:5000/subscription/) to activate the server logic.

You can monitor incoming requests on the [Particle User Logs](https://dashboard.particle.io/user/logs) screen.
