# main.py
import AbuseIPDBClient
import Levenshtein
import Logger
import certstream

LOGGER = Logger.Logger() # overload with True to print logs
TRUSTED_DOMAIN = "pepito.com" # change here and put your DN

def acknowledge(domain, authority):
    levenshtein_score = Levenshtein.distance(domain, TRUSTED_DOMAIN)
    if levenshtein_score > 4:
        return
    abuseipdb_score = AbuseIPDBClient.get_score(domain)
    trust_score = 0
    if not "letsencrypt" in authority: # we don't trust let's Encrypt
        trust_score += 20
    # the more operations needed to transform into our domain,
    # the more trusted the domain gets
    trust_score += levenshtein_score * 10
    # trusted domains with low abuseIPDB score get high trust score
    trust_score += 100 - abuseipdb_score 
    if trust_score<30:
        LOGGER.high(domain, authority)
    elif trust_score<50:
        LOGGER.medium(domain, authority)
    else:
        LOGGER.low(domain, authority)

def callback(message, context):
    if message['message_type'] != "certificate_update":
        return
    all_domains = message['data']['leaf_cert']['all_domains']
    authority = message['data']['leaf_cert']["extensions"]["authorityInfoAccess"]
    for domain in all_domains:
        acknowledge(domain, authority)

def main():
    certstream_url="wss://certstream.calidog.io/"
    certstream.listen_for_events(callback, url=certstream_url)

if __name__ == "__main__":
    main()


