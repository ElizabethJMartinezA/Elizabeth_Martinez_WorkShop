           
from flask import Flask 
from flask import request
import requests
from keystone import login
from glance import listImages
from nova import flavoursList, keypairsList ,securityGroups
from nova import serverCreate
from neutron import networksList

app = Flask('My_API')           
           
# keyStone

# glance
@app.route("/listImages", methods=['GET'])
def listarImagenes():
    imagenes=listImages()
    return imagenes 

# nova
    #GET
@app.route("/flavoursList", methods=['GET'])
def listarFlavours():
    flavours=flavoursList()
    return flavours

@app.route("/keypairsList", methods=['GET'])
def listarKeypairs():
    keyPair=keypairsList()
    return keyPair

@app.route("/securityGroups", methods=['GET'])
def listSecurityGroups():
    secureGroups = securityGroups()
    return secureGroups
# nova
    #POST
@app.route("/getJson", methods=['POST'])
def jsonData():
    serverData=request.get_json()
    serverCreate(serverData)
    
# neutron
@app.route("/networksList", methods=['GET'])
def listNetworks():
    netWorks = networksList()
    return netWorks
