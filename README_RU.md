# Пример сервера на Flask.

server.py  
Позволяет провести сложение и деление чисел  
используя GET и POST запросы,  
как показано в request_server.py

### Операция сложения в server.py.
Принимает только GET запросы.  
пример: 
```shell
curl -X GET "http://127.0.0.1:5000/path/summa?sugarmoon=200&sugar=100"
```

### Операция деления в server.py.
Принимает только POST запросы.
пример:
```shell
curl --request POST 'http://127.0.0.1:5000/division' --header 'Content-type: application/json' -d '{"a":100,"b":2}'
```

## request_server.py
Передает GET запрос на сложение  
и POST запрос на деление чисел.


