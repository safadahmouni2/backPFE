
# Import the Flask module that has been installed.
import joblib
from flask import Flask, jsonify
from data import data_distribution,influencedist,persondist,accuracy,topicmodeling,comparaison
import sys
from flask_cors import CORS
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn import svm
from flask import request

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
    text = request.args.get("textinput")
    algorithm = request.args.get("algorithm")
    model = get_model(algorithm)
    result = predict(text,model)
    return jsonify({"result":result})


# load the model from disk
# load the model from disk

def get_politician(index):
    politicians = [
        "",
        "قيس سعيد",
        "عبير موسي",
        "هشام المشيشي",
        "الصافي سعيد",
        "راشد الغنوشي",
        "محمد عبو",
        "سيف الدين مخلوف",
        "يوسف الشاهد",
        "ياسين العياري",
        "فيصل التبيني"
    ]
    return politicians[index]

def get_model(algorithm):
    if algorithm=="nb":
        loaded_model= joblib.load("modelnb.sav")
    elif algorithm=="svm":
         loaded_model= joblib.load("modelsvm.sav")
    elif algorithm=="lr":
         loaded_model= joblib.load("modelLogisticRegression.sav")
    elif algorithm=="rf":
         loaded_model= joblib.load("modelRandomForest.sav")
    else:
        loaded_model= joblib.load("modelnb.sav")
    return loaded_model

def predict(text,model):
    #loaded_model= joblib.load("modelnb.sav")
    tfidfvect = joblib.load("tfidfvect.sav")  
    #text = "الارادة السياسية كانت السبب في إنتهاء الارهاب في تونس بفضل تعاون راشد الغنوشي و يوسف الشاهد"

    a = []
    a.append(text)
    ap = tfidfvect.transform(a)
    result =model.predict(ap)
    politician_name = get_politician(int(result[0]))
    return {"politician_name" :str(politician_name), "influence":str(result[0])}

if __name__ == "__main__":
    app.config['JSON_AS_ASCII'] = False
    app.run(debug=True)