# -*- coding: utf-8 -*-

import httplib2

from apiclient.discovery import build
from oauth2client.file import Storage

CREDENTIALS_LOCATION = "credentials.json"

class GoogleDriveClient(object):
    def createService(self):
        storage = Storage(CREDENTIALS_LOCATION)
        credentials = storage.get()
        if credentials is None or credentials.invalid == True:
            return None

        http = httplib2.Http()
        http = credentials.authorize(http)

        drive_service = build("drive", "v2", http)
        return drive_service
