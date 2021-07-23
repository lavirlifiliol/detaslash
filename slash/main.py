from pathlib import Path
import os

from flask import Flask
from deta import App
from upload_commands import build_commands
app = App(Flask(__name__))


@app.route("/", methods=["GET"])
def hello_world():
    return "hello, world"

@app.lib.run(action='test')
def test(ev):
    try:
        return build_commands(guild=ev.json['id'])
    except KeyError:
        return build_commands(guild=os.environ['TEST_GUILD'])
    
@app.lib.run(action='global')
def run(ev):
    return build_commands()
