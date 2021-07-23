from pathlib import Path
import os

from flask import Flask, request, jsonify
from deta import App, Deta
from upload_commands import build_commands
from discord_interactions import verify_key_decorator, InteractionType, InteractionResponseType

app = App(Flask(__name__))

deta = Deta(os.environ['PROJECT_KEY'])
number = deta.Base("number")


def up():
    number.put(number.get('number')['value'] + 1, 'number')
    return str(number.get('number')['value'])


def down():
    number.put(number.get('number')['value'] - 1, 'number')
    return str(number.get('number')['value'])


@app.route("/", methods=["POST"])
@verify_key_decorator(os.environ['CLIENT_PUBLIC'])
def interact():
    if request.json['type'] == InteractionType.APPLICATION_COMMAND:

        data = request.json['data']
        return jsonify({
            'type': InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE,
            'data': {
                'content': up() if data['options'][0]['name'] == 'up' else down()
            }
        })

@app.lib.run(action='test')
def test(ev):
    try:
        return build_commands(guild=ev.json['id'])
    except KeyError:
        return build_commands(guild=os.environ['TEST_GUILD'])
    
@app.lib.run(action='global')
def run(ev):
    return build_commands()


@app.lib.run(action='reset')
def run(ev):
    v = ev.json.get('v', 0)
    number.put(v, 'number')
    return number.get('number')['value']