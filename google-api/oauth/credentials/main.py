# -*- coding: utf-8 -*-

import logging
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError

CLIENT_SECRETS_LOCATION = "client_secrets.json"
CREDENTIALS_LOCATION = "credentials.json"
REDIRECT_URI = "urn:ietf:wg:oauth:2.0:oob"
SCOPES = ["https://www.googleapis.com/auth/drive",
          "https://www.googleapis.com/auth/userinfo.email",
          "https://www.googleapis.com/auth/userinfo.profile"
]

def store_credentials(credentials):
    try:
        f = open(CREDENTIALS_LOCATION, 'wb')
        f.write(credentials.to_json())
        f.close()
    except IOError:
        pass

def exchange_code(authorization_code):
    flow = flow_from_clientsecrets(CLIENT_SECRETS_LOCATION, " ".join(SCOPES))
    flow.redirect_uri = REDIRECT_URI
    try:
        credentials = flow.step2_exchange(authorization_code)
        return credentials
    except FlowExchangeError, e:
        logging.error("An error occurred: %s", e)


code = "4/fXU4C4_CLJVYlfHw3HQZ9Z1tKtcm.wljqGBnBpmYYgrKXntQAax2K_BioeAI"
credentials = exchange_code(code)
store_credentials(credentials)