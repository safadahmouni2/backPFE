
# Import the Flask module that has been installed.
import joblib
from flask import Flask, jsonify
from data import influencedist,persondist,topfrequentwords,accuracy,topicmodeling,comparaison,datadist
from flask_cors import CORS
from flask import request
from keras.models import model_from_json
from keras.preprocessing.sequence import pad_sequences
import pickle


# Creating a new "app" by using the Flask constructor. Passes __name__ as a parameter.
app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})
@app.route("/")
def index():
    return jsonify({})

@app.route("/data-distribution")
def datadistribution():
    return jsonify(datadist)
@app.route("/top-frequent-words")
def topwors():
    return jsonify(topfrequentwords)
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
    if(algorithm != "lstm"):
        result = predict(text,model)
    elif(algorithm == "lstm"):
        result = predictdl(text,model)
    else:
        result = {"politician_name" :"error", "influence":"error"}
    return jsonify({"result":result})


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

# load the ML models from disk
def get_model(algorithm):
    if algorithm=="nb":
        loaded_model= joblib.load("modelnb.sav")
    elif algorithm=="svm":
         loaded_model= joblib.load("modelsvm.sav")
    elif algorithm=="lr":
         loaded_model= joblib.load("modelLogisticRegression.sav")
    elif algorithm=="rf":
         loaded_model= joblib.load("modelRandomForest.sav")
    elif algorithm=="lstm":
        json_file = open('model.json', 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        loaded_model = model_from_json(loaded_model_json)
        # load weights into new model
        loaded_model.load_weights("modelw.h5")
    else:
        loaded_model = None
    return loaded_model

# load the Dl(LSTM) models from disk
def predictdl(text,model):
    with open('tokenizer.pickle', 'rb') as handle:
        loaded_tokenizer = pickle.load(handle)
    seq= loaded_tokenizer.texts_to_sequences([text])
    padded = pad_sequences(seq, maxlen=2000)
    pred = model.predict(padded)

    return {"politician_name" :
    str(get_politician(pred[0].argmax(axis=-1)+1)), "influence":str(pred[0].argmax(axis=-1)+1)}
def predict(text,model):
    #loaded_model= joblib.load("modelnb.sav")
    tfidfvect = joblib.load("tfidfvect.sav")  
    a = []
    a.append(text)
    ap = tfidfvect.transform(a)
    result =model.predict(ap)
    politician_name = get_politician(int(result[0]))
    return {"politician_name" :str(politician_name), "influence":str(result[0])}

if __name__ == "__main__":
    app.config['JSON_AS_ASCII'] = False
    app.run(debug=True)