import requests

JORDIN_BASE_URL = "https://jord.in"


def jordin_get(endpoint):
    return requests.get(JORDIN_BASE_URL + endpoint).text
