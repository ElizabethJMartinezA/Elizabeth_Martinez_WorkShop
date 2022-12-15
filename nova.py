from flask import Flask 
from flask import request
import requests
import keystone


app = Flask('My_API')
env_url = 'https://api-uat-001.ormuco.com'
headers={'X-Auth-Token':keystone.login()}

novaPort = '8774/v2.1'


#3. List Flavours GET

def flavoursList():
    flavors = requests.get(url=f"{env_url}:{novaPort}/flavors", headers=headers)
    flavors = flavors.json().get('flavors')
    return flavors

#4. List Keypairs GET

def keypairsList():
    keyPairs = requests.get(url=f"{env_url}:{novaPort}/os-keypairs", headers=headers)
    keyPairs = keyPairs.json().get('keypairs')
    return keyPairs


#5. Security Group GET

def securityGroups():
    securityGroup = requests.get(url=f"{env_url}:{novaPort}/os-security-groups", headers=headers)
    securityGroup = securityGroup.json().get('security_groups')
    return securityGroup

#6. Create Server POST

def serverCreate(server_to_create):
    server_on_cloud = requests.post(url=f"{env_url}:{novaPort}/servers", json=server_to_create, headers=headers)
    return server_on_cloud
    

#print(server_on_cloud.reason)
#print(server_on_cloud.text)