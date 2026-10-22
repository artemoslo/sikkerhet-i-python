import requests

url = "http://localhost:8080"
for i in range(1000):
    response = requests.get(url)
    print(f"Request {i} status: {response.status_code}")