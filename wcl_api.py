import requests
import os

def get_wcl_token():
    auth = (os.getenv("WCL_CLIENT_ID"), os.getenv("WCL_CLIENT_SECRET"))
    resp = requests.post("https://www.warcraftlogs.com/oauth/token", data={"grant_type": "client_credentials"}, auth=auth)
    return resp.json().get("access_token")

# Logic to verify code on profile would go here