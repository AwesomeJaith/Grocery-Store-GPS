import requests
url = 'https://storeapi2.pythonanywhere.com/api/calculate-optimal-path'

data = { "groceries": ["spaghetti noodles", "alfredo sauce", "olives"] }

headers = {"Content-Type": "application/json"}

response = requests.post(url, json=data, headers=headers)

if response.status_code == 200:
    response_data = response.json()
    print(response_data)
else:
    print(f"Request failed with status code {response.status_code}")