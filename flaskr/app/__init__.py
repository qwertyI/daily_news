from flask import Flask

app = Flask(__name__)

server_url = 'http://127.0.0.1:5001'

from app import view