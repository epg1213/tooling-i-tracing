# AbuseIPDBClient.py
import requests
import socket

class AbuseIPDBClient:
    def __init__(self, api_key: str):
        self.api_key=api_key

    def check_reputation(self, ip: str):
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
    client = AbuseIPDBClient(key.strip())
    ip = socket.gethostbyname(domain)
    return client.check_reputation(ip)


