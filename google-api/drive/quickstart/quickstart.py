# -*- coding: utf-8 -*-

import httplib2
import pprint

from apiclient.discovery import build
from apiclient.http import MediaFileUpload
from oauth2client.client import flow_from_clientsecrets

CLIENT_SECRETS_LOCATION = "client_secrets.json"
OAUTH_SCOPE = "https://www.googleapis.com/auth/drive"
REDIRECT_URI = "urn:ietf:wg:oauth:2.0:oob"

flow = flow_from_clientsecrets(CLIENT_SECRETS_LOCATION, OAUTH_SCOPE, REDIRECT_URI)
authorize_url = flow.step1_get_authorize_url()
print "Go to the following link in your browser: " + authorize_url

code = raw_input("input authorize code:")
credentials = flow.step2_exchange(code)

http = httplib2.Http()
http = credentials.authorize(http)

drive_service = build("drive", "v2", http=http)

FILENAME = "test document.txt"
media_body = MediaFileUpload(FILENAME, mimetype="text/plain", resumable=True)
body = {
    "title": "My Document",
    "description": "A test document",
    "mimeType": "text/plain"
}

file = drive_service.files().insert(body=body, media_body=media_body).execute()
pprint.pprint(file)