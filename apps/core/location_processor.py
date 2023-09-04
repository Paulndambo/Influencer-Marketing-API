import requests

headersList = {
    "Accept": "*/*",
    "User-Agent": "Thunder Client (https://www.thunderclient.com)" 
    }

payload = ""

def get_customer_location_details(reqUrl):
    response = requests.request("GET", reqUrl, data=payload,  headers=headersList)
    return response.json()
