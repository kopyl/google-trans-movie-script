from googletrans import Translator

import os
import six
from google.cloud import translate_v2 as translate

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


def translate_text(text):
    credential_path = "key.json"
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

    translate_client = translate.Client()

    if isinstance(text, six.binary_type):
        text = text.decode("utf-8")

    result = translate_client.translate(
        text, target_language='en', format_="text")
    return result


print("start")

text = getText()
# righttoowntranslations.insert_many(translations)

# print(len(text))


# print(list(righttoowntranslations.find()))

# print(json.dumps(translations, indent=4, ensure_ascii=False))
# print(json.dumps(translations, indent=4, ensure_ascii=False))

# for x in righttoowntranslations.find({}, {"_id": 0}):
#     print(json.dumps(x, indent=4, ensure_ascii=False))


chunked_list = list()
chunk_size = 10
for i in range(0, len(text), chunk_size):
    chunked_list.append(text[i:i+chunk_size])

print("chunked")

count = 0
for chunk in chunked_list:
    translations = translate_text(chunk)
    righttoowntranslations.insert_many(translations)
    count += 1
    print(count)

# for translation in righttoowntranslations.find({}, {"_id": 0}):
#     print(json.dumps(translation, indent=4, ensure_ascii=False))


print("end")
