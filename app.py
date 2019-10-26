from flask import Flask,request, jsonify, render_template
import os
import spacy
from flask_cors import CORS

#BASE_DIR = os.path.dirname(os.path.abspath(__file__))
#MODEL_DIR = os.path.join(BASE_DIR, 'model')
#input_dir = MODEL_DIR

app = Flask(__name__)
CORS(app)

nlp = spacy.load(model/)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    test_text = request.json["text"]
    try:
        doc = nlp(test_text)
        for ent in doc.ents:
            return jsonify(ent.label_, ent.text), 200
    except Exception as e:
        print(e)
        return jsonify({"result": "Model failed"})

@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
