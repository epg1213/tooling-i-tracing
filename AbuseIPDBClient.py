# AbuseIPDBClient.py
import requests
import socket

class AbuseIPDBClient:
    def __init__(self, api_key: str):
        self.api_key=api_key

    def check_reputation(self, ip: str): # using a BaseClient class to make one get request seemed overkill
        response = requests.get("https://api.abuseipdb.com/api/v2/check?ipAddress={}".format(ip),
             headers={"Key": self.api_key, "Accept": "application/json"}).json()
        return int(response["data"]["abuseConfidenceScore"])

def get_score(domain):
    try:
        with open("key.txt", "r") as file:
            key=file.read()
    except:
        print("Please put your AbuseIPDB API key in a 'key.txt' file.")
        exit(1)
    try:
        client = AbuseIPDBClient(key.strip())
        ip = socket.gethostbyname(domain)
        return client.check_reputation(ip)
    except:
        return 0 # if the dns can't be solved or there is no entry in abuseIPDB for example

