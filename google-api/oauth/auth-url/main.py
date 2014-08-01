# -*- coding: utf-8 -*-


from oauth2client.client import flow_from_clientsecrets


CLIENT_SECRETS_LOCATION = "client_secrets.json"
REDIRECT_URI = "urn:ietf:wg:oauth:2.0:oob"
SCOPES = ["https://www.googleapis.com/auth/drive",
          "https://www.googleapis.com/auth/userinfo.email",
          "https://www.googleapis.com/auth/userinfo.profile"
]

def get_authorization_url(user_id):
    """
    アプリケーション認証URLを作成します。
    """
    flow = flow_from_clientsecrets(CLIENT_SECRETS_LOCATION, " ".join(SCOPES))
    flow.params["access_type"] = "offline"
    flow.params["approval_prompt"] = "force"
    flow.params["user_id"] = user_id
    return flow.step1_get_authorize_url(REDIRECT_URI)

print(get_authorization_url("mododeveloper@gmail.com"))
