# -*- coding: utf-8 -*-

from client import GoogleDriveClient
from apiclient.http import MediaFileUpload

drive_client = GoogleDriveClient()
drive = drive_client.createService()

body = {
    "title": "My Folder",
    "description": "This is test folder.",
    "mimeType": "application/vnd.google-apps.folder"
}
folder = drive.files().insert(body=body).execute()

parent = folder["id"]




