from flask import Flask, request
# import pickle

app = Flask(__name__)

# model = pickle.load(open('model.pkl', 'rb'))

# @app.route('/predict', methods=['POST'])
# def predict():
#     data = request.get_json()
#     prediction = model.predict([data['measurements']])
#     return prediction[0]


@app.route('/', methods=['GET'])
def check():

    response = {"API is up"}

    return response