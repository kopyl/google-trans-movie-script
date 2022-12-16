# coding=utf8

import json
import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials

import pymongo

from process_text import getText

import json


client = pymongo.MongoClient(
    f"mongodb://"
    f"kopyl:oleg66@"
    f"localhost"
)

db = client["moviescripts"]
righttoowntranslations = db["righttoowntranslations"]

CREDENTIALS_FILE = 'key.json'
google_docs_id = "1hoP4acNyQxKpllDrogAo9SzERKxo5KSysxs3UiLqB1U"

permissions = [
    'https://www.googleapis.com/auth/documents']
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    CREDENTIALS_FILE, permissions
)
httpAuth = credentials.authorize(httplib2.Http())
service = apiclient.discovery.build('docs', 'v1', http=httpAuth)


def update_google_doc(request: list):
    service.documents().batchUpdate(documentId=google_docs_id, body={
        "requests": request
    }).execute()


def transform_to_replaceAllText(translations: list):
    return list(map(lambda x: {
        "replaceAllText": {
            "containsText": {
                "text": x["input"],
                "matchCase": True
            },
            "replaceText": f'{x["input"]}\n-------\n{x["translatedText"]}'
        }
    }, translations))


# update_google_doc(transform_to_replaceAllText(example_translations))


replacements = transform_to_replaceAllText(
    righttoowntranslations.find({}, {"_id": 0}))

chunked_list = list()
chunk_size = 10
for i in range(0, len(replacements), chunk_size):
    chunked_list.append(replacements[i:i+chunk_size])

count = 0
for n, chunk in enumerate(chunked_list[74:]):
    # if count < 40:
    #     continue
    # for x in chunk:
    #     if x["replaceAllText"]["containsText"]["text"] == "Коли я дозволю.":
    #         print(x, count, n)
    update_google_doc(chunk)
    # print(chunk)


# count = 0
# for translation in transform_to_replaceAllText(
#     righttoowntranslations.find({}, {"_id": 0})
# ):
#     print(json.dumps(translation, indent=4, ensure_ascii=False))
#     count += 1
#     if count == 1:
#         break
