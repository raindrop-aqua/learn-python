# -*- coding: utf-8 -*-

from client import GoogleDriveClient
from apiclient.http import MediaFileUpload

drive_client = GoogleDriveClient()
drive_service = drive_client.createService()

FILENAME = "test document.txt"
media_body = MediaFileUpload(FILENAME, mimetype="text/plain", resumable=True)
body = {
    "title": "My Document",
    "description": "A test document",
    "mimeType": "text/plain"
}

file = drive_service.files().insert(body=body, media_body=media_body).execute()
