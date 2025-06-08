# main.py
import AbuseIPDBClient
import stringdiff
import Logger
import certstream

logger = Logger.Logger()
trusted_domain = "pepito.com"

def acknowledge(domain, authority):
    stringdiff_score = stringdiff.get_score(domain, trusted_domain)
    if stringdiff_score > 4:
        return
    abuseipdb_score = AbuseIPDBClient.get_score(domain)
    trust_score = 0
    if not "letsencrypt" in authority:
        trust_score += 20
    trust_score += stringdiff_score * 10
    trust_score += 100 - abuseipdb_score
    if trust_score<30:
        logger.high(domain, authority)
    elif trust_score<50:
        logger.medium(domain, authority)
    else:
        logger.low(domain, authority)

def callback(message, context):
    if message['message_type'] != "certificate_update":
        return
    all_domains = message['data']['leaf_cert']['all_domains']
    authority = message['data']['leaf_cert']["extensions"]["authorityInfoAccess"]
    for domain in all_domains:
        acknowledge(domain, authority)

def main():
    certstream_url="wss://certstream.calidog.io/"
    #certstream.listen_for_events(callback, url=certstream_url)
    for domain in ["pepito.org", "forza.fr", "pepite.com"]:
        acknowledge(domain, "letsencrypt")

if __name__ == "__main__":
    main()


