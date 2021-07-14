# Example Flask server.

server.py
Allows you to add and divide numbers
using GET and POST requests,
as shown in request_server.py

### Addition operation in server.py.
Only accepts GET requests.
example:
```shell
curl -X GET "http://127.0.0.1:5000/path/summa?sugarmoon=200&sugar=100"
```

### Division operation in server.py.
Only accepts POST requests.
example:
```shell
curl --request POST 'http://127.0.0.1:5000/division' --header 'Content-type: application / json' -d '{"a": 100, "b": 2}'
```

## request_server.py
Sends a GET request for addition
and a POST request to divide numbers.


