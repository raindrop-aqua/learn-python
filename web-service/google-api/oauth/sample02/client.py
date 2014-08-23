# -*- coding: utf-8 -*-

import httplib2

from apiclient.discovery import build
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import run

CLIENT_SECRETS_LOCATION = "client_secrets.json"
CREDENTIALS_LOCATION = "credentials.json"
REDIRECT_URI = "urn:ietf:wg:oauth:2.0:oob"
SCOPES = ["https://www.googleapis.com/auth/drive.file",
          "https://www.googleapis.com/auth/userinfo.email",
          "https://www.googleapis.com/auth/userinfo.profile"
]


class GoogleDriveClient(object):
    def createService(self):
        flow = flow_from_clientsecrets(
            CLIENT_SECRETS_LOCATION,
            scope=" ".join(SCOPES),
            redirect_uri=REDIRECT_URI
        )

        storage = Storage(CREDENTIALS_LOCATION)
        credentials = storage.get()
        if credentials is None or credentials.invalid == True:
            credentials = run(flow, storage)

        http = httplib2.Http()
        http = credentials.authorize(http)

        drive_service = build("drive", "v2", http)
        return drive_service
