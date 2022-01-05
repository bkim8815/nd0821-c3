# Put the code for your API here.



from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union
from starter.ml.model import inference
import pandas as pd
import numpy as np

import joblib
from starter.ml.data import process_data


app = FastAPI()


# Declare the data object with its components and their type.
class Person(BaseModel):
    age: int
    workclass: str
    fnlgt: int
    education: str
    education_num: int
    marital_status: str
    occupation: str
    relationship: str
    race: str
    sex: str
    capital_gain: int
    capital_loss: int
    hours_per_week: int
    native_country: str



@app.get("/")
async def welcome():
    return {"message":"Hello"}



# This allows sending of data (our TaggedItem) via POST to the API.
@app.post("/salary")
async def calculate(person: Person):
    # model = csv("./model/census_model.pkl")
    model = joblib.load("./model/census_model.pkl")
    encoder = joblib.load("./model/encoder.pkl")


    df = pd.DataFrame.from_dict({
        "age": [person.age],
        "workclass": [person.workclass],
        "fnlgt": [person.fnlgt],
        "education": [person.education],
        "education_num": [person.education_num],
        "marital-status": [person.marital_status],
        "occupation": [person.occupation],
        "relationship": [person.relationship],
        "race": [person.race],
        "sex": [person.sex],
        "capital-gain": [person.capital_gain],
        "capital-loss": [person.capital_loss],
        "hours-per-week": [person.hours_per_week],
        "native-country": [person.native_country]

        }
    )

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


    X, _, _, _ = process_data(df, cat_features, label=None, training=False, encoder=encoder)

    prediction = inference(model, X)
    print(prediction)
    return np.array(prediction).tolist()[0] == 1
