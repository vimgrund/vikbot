import pysftp
import requests
import os


def download_pic(url):
    filename = "../tmp/" + url.split('/')[-1]
    res = requests.get(url)
    with open(filename, "wb") as f:
        f.write(res.content)
    return filename


def ftp_upload(file, prefix=""):
    # credentials of targeted sftp server
    host = os.environ['VB_FTP_HOST']
    username = os.environ['VB_FTP_USER']
    password = os.environ['VB_FTP_PW']
    url = os.environ['VB_URL']
    result = "¯\_ (ツ)_/¯"
    try:
        with pysftp.Connection(host=host,
                               username=username, password=password) as conn:
            print("connection established successfully")
            # file path of local file and targeted location
            filename = file.split('/')[-1]
            target_location = f'/httpdocs/{prefix}{filename}'
            # call conn.put() method to upload file to server
            conn.put(file, target_location)
            conn.close()
            result = f"{url}{prefix}{filename}"
    except:
        result = 'failed to establish connection to targeted server'
    return result