
This tool is used to find domains that resemble the one you target, using certstream to wait for new TLS certificates being issued.
It can be used to protect your domain name against typo squatting, and uses the AbuseIPDB API to check each domain's reputation.

# Installing

```
python -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt
```

# Usage

Firstly edit the main.py file and update the "TRUSTED_DOMAIN" variable with your domain name

```
echo $YOUR_ABUSEIPDB_API_KEY > key.txt
source ./venv/bin/activate
python main.py
```
