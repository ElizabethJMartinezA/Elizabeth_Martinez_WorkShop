from flask import Flask 
from flask import request
import requests
import keystone

app = Flask('My_API')
env_url = 'https://api-uat-001.ormuco.com'
headers={'X-Auth-Token':keystone.login()}

glance_port = '9292'
    
# list Images GET

#@app.route("/listImages", methods=['GET'])
def listImages():

    images = requests.get(url=f"{env_url}:{glance_port}/v2/images", headers=headers)
    images = images.json().get('images')
    return images
