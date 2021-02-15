from textblob import TextBlob
from flask import Flask, request, jsonify 
from flask_cors import CORS

app = Flask(__name__) 
CORS(app)

@app.route("/testHealth") 
def hello():
    return "Hello World!"

@app.route("/analyse/sentiment", methods=['POST']) 
def analyse_sentiment():
    sentence = request.get_json()['sentence']
    polarity = TextBlob(sentence).sentences[0].polarity 
    return jsonify(
        sentence=sentence,
        polarity=polarity 
    )

if __name__ == '__main__': 
    app.run(host='0.0.0.0', port=5000)