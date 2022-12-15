# replace text in google doc
import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials

CREDENTIALS_FILE = 'key.json'  # имя файла с закрытым ключом
# google_docs_id = "1KVeXRlieG-cZoUjeh2aV9JSq84WGnzag"
google_docs_id = "1hoP4acNyQxKpllDrogAo9SzERKxo5KSysxs3UiLqB1U"

credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE,
                                                               ['https://www.googleapis.com/auth/documents', 'https://www.googleapis.com/auth/drive', 'https://www.googleapis.com/auth/drive.file', 'https://www.googleapis.com/auth/drive.readonly', 'https://www.googleapis.com/auth/documents.readonly',])
httpAuth = credentials.authorize(httplib2.Http())
service = apiclient.discovery.build('docs', 'v1', http=httpAuth)


# doc = service.documents().get(documentId=google_docs_id).execute()
# doc_content = doc.get('body').get('content')

# print(doc)

# print(service.documents().create(body={}).execute())


service.documents().batchUpdate(documentId=google_docs_id, body={
    "requests": [
        {
            "replaceAllText": {
                "containsText": {
                    "text": "Лоґлайн: «Відьма з картини полює на душу молодого водія Богдана, у сім'ї якого очікується поповнення»",
                    "matchCase": True
                },
                "replaceText": 'Ти там скоро, Альош? «Плейбой» мій надибав, чи що?\nAre you there soon, Alyosha? "Playboy" is my dick, or what?'
            }
        }
    ]
}).execute()
