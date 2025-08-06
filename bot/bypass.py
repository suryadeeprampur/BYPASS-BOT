import requests

def bypass_url(url):
    session = requests.Session()
    response = session.head(url, allow_redirects=True, timeout=10)
    return response.url
