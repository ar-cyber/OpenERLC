import requests
from utils.conf import main
def send_command(command: str):
    key = main['setup']['api_key']
    if not key:
        return {
            "code": 403,
            "message": "There was no key in the conf file or the key is invalid"
        }
    body = {
        "command": command
    }
    query = requests.post("https://api.policeroleplay.community/v1/server/command", body).json()
    if query.code and query.code in [2000, 2001]:
        return {
            "code": 403,
            "message": "There was a malformed code or the code was not sent"
        }
    else:
        return query
    