
# Import the Flask module that has been installed.
from flask import Flask, jsonify
from data import data_distribution,influencedist,persondist,accuracy,topicmodeling,comparaison
import sys
from flask_cors import CORS

# Creating a new "app" by using the Flask constructor. Passes __name__ as a parameter.
app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})
@app.route("/")
def index():
    return jsonify({})

@app.route("/data-distribution")
def datadistribution():
    return jsonify(data_distribution)

@app.route("/influence-distribution")
def influencedistribution():
    return jsonify(influencedist)

@app.route("/person-distribution")
def persondistribution():
    return jsonify(persondist)

@app.route("/accuracy")
def faccuracy():
    return jsonify(accuracy)

@app.route("/comparaison")
def fcomparaison():
    return jsonify(comparaison)

@app.route("/topic-modeling")
def ftopicmodeling():
    return jsonify(topicmodeling)

@app.route("/application")
def appl():
    return jsonify({"result":"result of prediction"})

if __name__ == "__main__":
    app.config['JSON_AS_ASCII'] = False
    app.run(debug=True)