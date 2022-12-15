from flask import Flask 
from flask import request
import requests
import keystone

app = Flask('My_API')
env_url = 'https://api-uat-001.ormuco.com'
headers={'X-Auth-Token':keystone.login()}

neutronPort = '9696'

# List Networks


def networksList():
    networks = requests.get(url=f"{env_url}:{neutronPort}/v2.0/networks", headers=headers)
    networks = networks.json().get('networks')
    return networks

