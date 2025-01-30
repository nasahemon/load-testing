# load-testing
try load testing

```sh
pip install locust
```

```sh
pip install flask
```

## To run the api service
```sh
python3 app.py
```

## To run the locust

```sh
locust -f locustfile.py
```

### curl for face detect

```sh
curl -X 'GET' \
  'http://172.16.7.82:4102/face/detect?filePath=/mnt/012_19922617289000218_P.jpg&location=true&compare=true' \
  -H 'accept: application/json'
```


```sh
curl -X 'POST' \
  'http://172.16.7.82:4102/face/detect/v2' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@/home/hasan/Downloads/test1.jpg;type=image/jpeg'
```