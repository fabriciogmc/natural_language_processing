from flask import Flask, jsonify, request
from flask_cors import CORS
from bot_model import preprocess, representation, classify

app = Flask(__name__)
CORS(app)

# Basic api route
@app.route('/bot_service')
def bot_service():
    ## Here we shall insert the PLN preprocessing, representation and classification code
    user_input = request.args.get('user_input') 
    preprocessed = preprocess(user_input)
    text_representation = representation(preprocessed)
    response_class = classify(text_representation)
    data = {"response": response_class}
    return jsonify(data)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)