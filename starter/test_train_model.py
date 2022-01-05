# Script to train machine learning model.

# Add the necessary imports for the starter code.

from sklearn.model_selection import train_test_split
import pandas as pd
from starter.ml.data import process_data
from starter.ml.model import train_model
import joblib
import pytest


@pytest.fixture(scope="session")
def data():
    return pd.read_csv("./data/test_census_clean.csv")




def test_train_model(data):
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
        data, categorical_features=cat_features, label="salary", training=True
    )
    model = train_model(X_train, y_train)
    assert model != None


def test_train_test_split(data):
    train, test = train_test_split(data, test_size=0.20)
    assert test.shape[0] > 0
