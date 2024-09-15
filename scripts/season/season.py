# sesoes disponiveis para analize:
import http.client
import requests


def season(key):

    conn = http.client.HTTPSConnection("v1.formula-1.api-sports.io")

    headers = {
        'x-rapidapi-host': "v1.formula-1.api-sports.io",
        'x-rapidapi-key': key
        }

    conn.request("GET", "/seasons", headers=headers)

    res = conn.getresponse()
    data = res.read()

    return data.decode("utf-8")
