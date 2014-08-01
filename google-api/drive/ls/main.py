# -*- coding: utf-8 -*-

from client import GoogleDriveClient
from apiclient.http import MediaFileUpload

drive_client = GoogleDriveClient()
drive = drive_client.createService()

folders = drive.files().list().execute()

for folder in folders["items"]:
    print(folder["title"])




