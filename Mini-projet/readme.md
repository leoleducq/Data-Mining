### Requêter l'API
- Exécuter le fichier predict_quality_wine.py avec `flask --app predict_quality_api run --host=0.0.0.0`
- Via POSTMAN, envoyer une requête POST à l'adresse http://localhost:5000/predict avec en paramètre un json contenant les caractéristiques du vin à prédire
- Exemple de json à envoyer : 
```json
{
    "fixed acidity": [7,3,9,10,5],
    "volatile acidity": [0.7,0.2,0.1,0.3,0.4],
    "citric acid": [0,0,1,0.1,0.3],
    "residual sugar": [2,3,4,5,1],
    "chlorides": [0.1,0.2,0.3,0.4,0.5],
    "free sulfur dioxide": [13,32,45,5,8],
    "total sulfur dioxide": [40,50,10,23,36],
    "density": [0.99,0.65,0.34,0.88,0.9],
    "pH": [3.5,4.2,3.6,4.1,1.2],
    "sulphates": [0.6,0.8,0.2,0.6,0.4],
    "alcohol": [9.5,20,21,3,4],
    "type wine" : ["red","white","red","red","white"]
}
```