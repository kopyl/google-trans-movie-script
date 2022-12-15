from googletrans import Translator

from flask import Flask, request, jsonify
from flask_cors import CORS

import os
import six
from google.cloud import translate_v2 as translate

app = Flask(__name__)
translator = Translator()
CORS(app, resources={r"*": {"origins": "*"}})


def translate_text(text):
    credential_path = "/Users/olehkopyl/Dropbox/Development/JS/vue/App for Render.com/API/key.json"
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

    translate_client = translate.Client()

    if isinstance(text, six.binary_type):
        text = text.decode("utf-8")

    result = translate_client.translate(
        text, target_language='en', format_="text")
    return result["translatedText"]


@app.route('/', methods=['POST'])
def hello_world():
    input_text = request.json.get('text')
    translation = translate_text(input_text)
    print(translation)
    print(translation)
    return jsonify({
        "translation": translation
    })


# if __name__ == '__main__':
#     app.run(host='', port=5009)


text = translate_text("Ти там скоро, Альош? «Плейбой» мій надибав, чи що?")

print(text)
