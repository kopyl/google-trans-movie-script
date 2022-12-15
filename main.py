from googletrans import Translator

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
translator = Translator()
CORS(app, resources={r"*": {"origins": "*"}})


@app.route('/', methods=['POST'])
def hello_world():
    text = request.json.get('text')
    result = translator.translate(text or "Помилка", src="uk", dest="en")
    return jsonify({
        "translation": result.text,
    })


if __name__ == '__main__':
    app.run(host='', port=5009)
