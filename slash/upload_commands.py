import os
import requests

SCOPE = "applications.commands.update applications.commands"
API_ENDPOINT = 'https://discord.com/api/v8'

def get_token():
    data = {
        'grant_type': 'client_credentials',
        'scope': SCOPE
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    r = requests.post(f'{API_ENDPOINT}/oauth2/token', data=data, headers=headers, auth=(os.environ['APP_ID'], os.environ['APP_SECRET']))
    r.raise_for_status()
    return r.json()['access_token']


def build_commands(*, guild=None):
    path = f'{API_ENDPOINT}/applications/{os.environ["APP_ID"]}'
    if guild:
        path += f'/guilds/{guild}'
    path += '/commands'
    data = {
        "name": "num",
        "description": "change the number",
        "options": [
            {
                "name": "up",
                "description": "make the number 1 greater",
                "type": 1,
            },
            {
                "name": "down",
                "description": "make the number 1 smaller",
                "type": 1,
            }
        ]
    }
    headers = {
        'Authorization': f'Bearer {get_token()}'
    }
    r = requests.post(path, headers=headers, json=data)
    r.raise_for_status()
    return r.json()
