# Script to train machine learning model.

# Add the necessary imports for the starter code.

from sklearn.model_selection import train_test_split
import pandas as pd
from ml.data import process_data
from ml.model import train_model, inference, compute_model_metrics

import joblib

# Add code to load in the data.
data = pd.read_csv("./data/census_clean.csv")


# Optional enhancement, use K-fold cross validation instead of a train-test split.
train, test = train_test_split(data, test_size=0.20)

cat_features = [
    "workclass",
    "education",
    "marital-status",
    "occupation",
    "relationship",
    "race",
    "sex",
    "native-country",
]
X_train, y_train, encoder, lb = process_data(
    train, categorical_features=cat_features, label="salary", training=True
)

joblib.dump(encoder, './model/encoder.pkl')

# Proces the test data with the process_data function.
X_test, y_test, encoder, lb = process_data(
    test, categorical_features=cat_features, label="salary", training=False, encoder=encoder, lb=lb
)

# Train and save a model.
model = train_model(X_train, y_train)
joblib.dump(model, './model/census_model.pkl')

y_preds = inference(model, X_test)
precision, recall, fbeta = compute_model_metrics(y_test, y_preds)



with open('./model/slice_output.txt', "a") as f:
    # f.write("precision, recall, fbeta\n")
    for cat_feat in cat_features:

        uniq_val_list = data[cat_feat].unique()

        for val in uniq_val_list:
            f.write(f'For {val}:  \n\n')
            new_data = data[data[cat_feat] == val]

            X, y, _, _ = process_data(
                new_data, categorical_features=cat_features, label="salary", training=False, encoder=encoder, lb=lb
            )

            predict_values = inference(model, X)
            precision, recall, fbeta = compute_model_metrics(y, predict_values)
            f.write("precision, recall, fbeta\n")

            f.write(f'{precision}, {recall}, {fbeta}\n')
