import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials

CREDENTIALS_FILE = 'key.json'
google_docs_id = "1hoP4acNyQxKpllDrogAo9SzERKxo5KSysxs3UiLqB1U"

permissions = [
    'https://www.googleapis.com/auth/documents']
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    CREDENTIALS_FILE, permissions
)
httpAuth = credentials.authorize(httplib2.Http())
service = apiclient.discovery.build('docs', 'v1', http=httpAuth)

service.documents().batchUpdate(documentId=google_docs_id, body={
    "requests": [
        {
            "replaceAllText": {
                "containsText": {
                    "text": "Лоґлайн: «Відьма з картини полює на душу молодого водія Богдана, у сім'ї якого очікується поповнення»",
                    "matchCase": True
                },
                "replaceText": 'Hey, I am gay!'
            }
        }
    ]
}).execute()
