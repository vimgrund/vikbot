from flask import Flask
from threading import Thread
from waitress import serve

app = Flask(__name__)

@app.get('/')
def hello():
    return "Discord Bot up and running"

def run():
    ip = "0.0.0.0"
    port = 80
    print(f"starting heartbeat-server at {ip}:{port}")
    serve(app, host=ip, port=port)

def start_heartbeat():
    t = Thread(target=run)
    t.start()

