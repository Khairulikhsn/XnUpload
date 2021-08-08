import json
import os

import click

CONFIG_FILE = os.path.expanduser('~/.config/xnup.json')
SESSION_FILE = os.path.expanduser('~/.config/xnup')


def default_config():
    if os.path.lexists(CONFIG_FILE):
        return CONFIG_FILE
    os.makedirs(os.path.dirname(CONFIG_FILE), exist_ok=True)
    click.echo('Go to https://my.telegram.org and create a App in API development tools')
    api_id = click.prompt('Please Enter api_id', type=int)
    api_hash = click.prompt('Now enter api_hash')
    with open(CONFIG_FILE, 'w') as f:
        json.dump({'api_id': api_id, 'api_hash': api_hash}, f)
    return CONFIG_FILE
