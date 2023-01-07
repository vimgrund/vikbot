import requests

def download_pic(url):
    filename = url.split('/')[-1]
    res = requests.get(url)
    with open(filename, "wb") as f:
        f.write(res.content)
    return filename