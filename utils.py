import requests # type: ignore

def test_logo_url(url):
    try:
        r = requests.head(url, allow_redirects=True, timeout=2)
        if r.status_code == 200 and r.headers.get('content-type', '').startswith('image'):
            return True
        else:
            return False
    except Exception as e:
        return False