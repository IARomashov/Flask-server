import requests


response = requests.get("http://127.0.0.1:5000/summa?x=200&y=100")
print(int(response.text))

response = requests.post('http://127.0.0.1:5000/division', json={'a': 100, 'b': 2})
print(int(response.text))
