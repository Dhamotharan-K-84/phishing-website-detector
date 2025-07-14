import re
import whois
from urllib.parse import urlparse
from datetime import datetime

def extract_features(url):
    features = []

    features.append(len(url))                             # URL length
    features.append(url.count('@'))                       # '@' symbol
    features.append(url.count('https'))                   # Count of 'https'
    features.append(url.count('//'))                      # Count of '//'
    features.append(1 if '-' in url else 0)               # '-' presence
    features.append(1 if 'https' in url else 0)           # SSL in URL
    features.append(1 if re.match(r"\d+\.\d+\.\d+\.\d+", url) else 0)  # IP address

    # WHOIS features
    try:
        domain = urlparse(url).netloc
        w = whois.whois(domain)

        creation_date = w.creation_date
        if isinstance(creation_date, list):
            creation_date = creation_date[0]
        age = (datetime.now() - creation_date).days if creation_date else 0
        features.append(age)
        features.append(1 if w.registrar else 0)
    except:
        features.extend([0, 0])  # WHOIS failed

    return features
