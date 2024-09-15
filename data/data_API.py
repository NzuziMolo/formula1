# Obtencao dos dados por meio de uma API
import os
import requests
import json
import pandas as pd


chave = '4fa03c5d1fb45efde700cd4e48af9971'


import http.client

conn = http.client.HTTPSConnection("v1.formula-1.api-sports.io")

headers = {
    'x-rapidapi-host': "v1.formula-1.api-sports.io",
    'x-rapidapi-key': chave
    }

conn.request("GET", "/seasons", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))




