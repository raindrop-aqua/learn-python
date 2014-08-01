# -*- coding: utf-8 -*-

from client import GoogleDriveClient

client = GoogleDriveClient()
service = client.createService()
print service
