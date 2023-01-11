import logging
import pysftp
import requests
import os


def download_pic(url):
    filename = "../tmp/" + url.split('/')[-1]
    res = requests.get(url)
    with open(filename, "wb") as f:
        f.write(res.content)
    return filename


def ftp_1_upload(file, prefix=""):
    # credentials of targeted sftp server
    host = os.environ['VB_FTP_1_HOST']
    username = os.environ['VB_FTP_1_USER']
    password = os.environ['VB_FTP_1_PW']
    url = os.environ['VB_URL_1']
    return ftp_upload(file, prefix, host, username, password, url)


def ftp_2_upload(file, prefix=""):
    # credentials of targeted sftp server
    host = os.environ['VB_FTP_2_HOST']
    username = os.environ['VB_FTP_2_USER']
    password = os.environ['VB_FTP_2_PW']
    url = os.environ['VB_URL_2']
    return ftp_upload(file, prefix, host, username, password, url)


def ftp_upload(file, prefix, host, username, password, url):
    result = "¯\_ (ツ)_/¯"
    try:
        with pysftp.Connection(host=host,
                               username=username, password=password) as conn:
            # logging.info("connection established successfully")
            # file path of local file and targeted location
            filename = file.split('/')[-1]
            target_location = f'/httpdocs/{prefix}{filename}'
            # call conn.put() method to upload file to server
            conn.put(file, target_location)
            conn.close()
            result = f"{url}{prefix}{filename}"
            # logging.info(f"file stored at {result}")
    except:
        # logging.info(f"failed to establish connection to targeted {host}")
        result = 'failed to establish connection to targeted server'
    return result
