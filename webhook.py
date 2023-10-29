import json
import os
import time
from http.server import BaseHTTPRequestHandler

from telebot import types

from main import bot


class handler(BaseHTTPRequestHandler):
    server_version = 'WebhookHandler/1.0'

    def do_GET(self):
        time.sleep(1.5)
        bot.set_webhook('https://' + os.environ['VERCEL_URL'])
        self.send_response(200)
        self.end_headers()

    def do_POST(self):
        cl = int(self.headers['Content-Length'])
        post_data = self.rfile.read(cl)
        body = json.loads(post_data.decode())

        bot.process_new_updates([types.Update.de_json(body)])

        self.send_response(204)
        self.end_headers()
