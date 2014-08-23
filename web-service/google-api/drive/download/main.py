# -*- coding: utf-8 -*-

from client import GoogleDriveClient

def store_file(file_name, content):
    f = open(file_name, 'wb')
    f.write(content)
    f.close()

drive_client = GoogleDriveClient()
drive = drive_client.createService()

id = ""
file = drive.files().get(fileId=id).execute()

download_url = file["downloadUrl"]

if download_url:
    response, content = drive._http.request(download_url)
    if response["status"] == "200":
        store_file(file["title"], content)
