from asyncio import sleep

import websocket
import yaml
import socket

config = yaml.safe_load(open('config/config.yml', 'rb'))
HOST = config['HOST']
PORT = config['PORT']
NICK = config['NICK']
PASS = config['PASS']


class PubSub(object):
    def __init__(self, channel, n_msg_per_sec=100):
        # super(Bot, self).__init__()
        self._nickname = NICK
        self.channel = channel
        self.connect(channel)
        print("{} {}\n{}".format(NICK, channel,
                                 '-' * (len(NICK + channel) + 1)))

        self._msg_count = 0
        self.n_msg_per_sec = n_msg_per_sec

    def connect(self, channel):
        self._socket = websocket.WebSocket()
        self._socket.connect("wss://pubsub-edge.twitch.tv")
        # self._socket.send("PASS {}\r\n".format(PASS).encode("utf-8"))
        self._socket.send('{"type": "PING"}')
        response = self._socket.recv()
        print(f"Received: {response}")
        self._socket.send('{"type": "LISTEN", "data": {"topics": ["channel-subscribe-events-v1.55933037"],"auth_token": "gmmoh5co6nj81uqjk1ys3v94wptpnd"}}')

    def _get_response(self):
        try:
            response = self._socket.recv()
        except UnicodeDecodeError as e:
            print('\n\n%s\n\n' % e)
            return False
        return response

    def action(self, msg):
        print(msg)

    def run(self):
        while True:
            response = self._get_response()
            if response:
                self.action(response)
            sleep(1 / float(self.n_msg_per_sec))


pubsub = PubSub(channel='ilmasseo')
pubsub.run()
