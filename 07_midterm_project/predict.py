import pickle
import pandas as pd
import xgboost as xgb
from flask import Flask, request, jsonify

# Load the model and DictVectorizer (dv)
model_file = 'XGBoost_model.bin'

with open(model_file, 'rb') as f_in:
    dv, model = pickle.load(f_in)

app = Flask('Fraud')

def predict_transaction_fraud(test_record, fraud_threshold=0.5):
    # Get the feature names used during training
    train_feature_names = model.feature_names

    # Transform the test record into the format used for prediction
    X_test = dv.transform([test_record])

    # Ensure the transformed test data has the same feature names as the training data
    X_test = pd.DataFrame(X_test, columns=train_feature_names)

    # Convert the DataFrame to a DMatrix
    X_test_dmatrix = xgb.DMatrix(X_test)

    # Get the prediction (probability of being fraudulent)
    y_preds = model.predict(X_test_dmatrix)

    # Classify the transaction based on the fraud threshold
    transaction_type = "Not Fraud" if y_preds[0] >= fraud_threshold else "Fraud"

    return transaction_type

@app.route('/predict', methods=['POST'])
def predict():
    transaction = request.get_json()

    # Call the prediction function with the received transaction
    transaction_status = predict_transaction_fraud(transaction)

    result = {
        'transaction_status': transaction_status
    }

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)
