# -*- coding: utf-8 -*-


import logging
import httplib2, urllib2
from apiclient.discovery import build
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import Credentials
from oauth2client.client import FlowExchangeError


CLIENT_SECRETS_LOCATION = "client_secrets.json"
CREDENTIALS_LOCATION = "credentials.json"
REDIRECT_URI = "urn:ietf:wg:oauth:2.0:oob"
SCOPES = ["https://www.googleapis.com/auth/drive.file",
          "https://www.googleapis.com/auth/userinfo.email",
          "https://www.googleapis.com/auth/userinfo.profile"
]

class GetCredentialsException(Exception):
    def __init__(self, authorization_url):
        self.authorization_url = authorization_url


class CodeExchangeException(GetCredentialsException):
    """
    """


class NoRefreshTokenException(GetCredentialsException):
    """
    """


class NoUserIdException(Exception):
    """
    """


def get_stored_credentials(user_id):
    credentials = None
    try:
        f = open(CREDENTIALS_LOCATION, 'r')
        content = f.read()
        f.close()
    except IOError:
        return credentials

    try:
        credentials = Credentials.new_from_json(content)
    except ValueError:
        pass

    return credentials


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
        raise CodeExchangeException(None)


def get_user_info(credentials):
    user_info_service = build(
        "oauth2", "v2",
        http=credentials.authorize(httplib2.Http()))
    user_info = None

    try:
        user_info = user_info_service.userinfo().get().execute()
    except urllib2.HTTPError, e:
        logging.error("An error occurred: %s", e)
    if user_info and user_info.get("id"):
        return user_info
    else:
        raise NoUserIdException


def get_authorization_url(user_id):
    """
    アプリケーション認証URLを作成します。
    """
    flow = flow_from_clientsecrets(CLIENT_SECRETS_LOCATION, " ".join(SCOPES))
    flow.params["access_type"] = "offline"
    flow.params["approval_prompt"] = "force"
    flow.params["user_id"] = user_id
    return flow.step1_get_authorize_url(REDIRECT_URI)


def get_credentials(authorization_code):
    email_address = ""
    user_id = ""

    try:
        credentials = exchange_code(authorization_code)
        user_info = get_user_info(credentials)
        email_address = user_info.get("email")
        user_id = user_info.get("id")
        if credentials.refresh_token is not None:
            store_credentials(credentials)
            return credentials
        else:
            credentials = get_stored_credentials(user_id)
            if credentials and credentials.refresh_token is not None:
                user_info = get_user_info(credentials)
                email_address = user_info.get("email")
                user_id = user_info.get("id")
                return credentials
    except CodeExchangeException, e:
        logging.error("An error occurred: %s", e)
        e.authorization_url = get_authorization_url(user_id)
        raise e
    except NoUserIdException:
        logging.error("No User ID could be retrieved.")

#user_id = ""
#print get_authorization_url(user_id, None)

code = ""
get_credentials(code)