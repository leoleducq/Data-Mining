# Import du model
import pickle
filename = 'wine_quality_t0_l1.sav'
loaded_model = pickle.load(open(filename, 'rb'))
col_keep = ['fixed acidity','volatile acidity','citric acid','residual sugar',
 'chlorides','free sulfur dioxide','total sulfur dioxide','density','pH',
 'sulphates','alcohol','red','white']

from sklearn import preprocessing
import pandas as pd

from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/predict_wine", methods=['POST'])
def predict_wine_quality(col_keep = col_keep, model = loaded_model) -> dict:
    """
    Predict the wine quality based on inputs
    """
    if request.method == 'POST':
        wine_input = {
            'fixed acidity': request.get_json()["fixed acidity"],
            'volatile acidity': request.get_json()["volatile acidity"],
            'citric acid': request.get_json()["citric acid"],
            'residual sugar': request.get_json()["residual sugar"],
            'chlorides': request.get_json()["chlorides"],
            'free sulfur dioxide': request.get_json()["free sulfur dioxide"],
            'total sulfur dioxide': request.get_json()["total sulfur dioxide"],
            'density': request.get_json()["density"],
            'pH': request.get_json()["pH"],
            'sulphates': request.get_json()["sulphates"],
            'alcohol': request.get_json()["alcohol"],
            'type wine' : request.get_json()["type wine"]
        }

        wine_red = [1 if item == 'red' else 0 for item in wine_input['type wine']]
        wine_white = [1 if item == 'white' else 0 for item in wine_input['type wine']]
        data_df_raw = pd.DataFrame.from_dict(wine_input)
        data_df_raw['red'] = wine_red
        data_df_raw['white'] = wine_white
        
        data_df_filter = data_df_raw.loc[::, [col_name for col_name in list(data_df_raw.columns) if col_name in col_keep]]
        data_array_l1 = preprocessing.normalize(data_df_filter, norm='l1')
        data_df_l1 = pd.DataFrame(data_array_l1, columns = col_keep)

        # Run prediction
        quality_prediction = {"quality" : [str(item) for item in list(model.predict(data_df_l1))]}

    return jsonify(quality_prediction)