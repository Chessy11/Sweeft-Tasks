import hashlib
import requests


def shorten(link: str):
    # ! The algorithm used in this function must be checked out for
    # ! the probability of URL collision when hash calculation for two
    # ! different strings gives the same result 
    encoded_url = hashlib.sha256(link.encode()).hexdigest()[:8]
    return encoded_url

def check_url(url: str):
    # checks if URL is valid
    try:
        r = requests.get(url)
        r.raise_for_status()
    except:
        return False
    return True
    