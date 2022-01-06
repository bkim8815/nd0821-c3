import requests
import json

url = 'https://bk-faskapi.herokuapp.com/salary'
data={
"age": 31,
"workclass": "Private",
"fnlgt": 45781,
"education": "Masters",
"education_num": 14,
"marital_status": "Never-married",
"occupation": "Prof-specialty",
"relationship": "Not-in-family",
"race": "White",
"sex": "Female",
"capital_gain": 14084,
"capital_loss": 0,
"hours_per_week": 50,
"native_country": "United-States"
}

x = requests.post(url, data = json.dumps(data))

print("status:")
print(x.status_code)
print("result:")
print(x.text)
