# coding=utf8

import json
import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials


import json


CREDENTIALS_FILE = 'key.json'
google_docs_id = "1HyTRstURZU4QDugHk0f1_NEYy2ytDBE6vtUfnvzRhjQ"
# google_docs_id = "18UOaPL6dpwPpDTS1C7o_D3QKrzBWz5npyXH9MuuI0qg"

permissions = [
    'https://www.googleapis.com/auth/documents']
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    CREDENTIALS_FILE, permissions
)
httpAuth = credentials.authorize(httplib2.Http())
service = apiclient.discovery.build('docs', 'v1', http=httpAuth)

doc = service.documents().get(documentId=google_docs_id).execute()

for paragraph in doc["body"]["content"]:
    text = paragraph.get("paragraph", {}).get("elements", [{}])[
        0].get("textRun", {}).get("content", "")
    if not text:
        continue
    print(text)
