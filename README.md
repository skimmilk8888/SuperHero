## Dependencies

You need to install flask, flask_restful, six, scipy, numpy, sklearn first

## Start server

```
python server.py
```
This will also create a local SQLite database training.db

## Post articles

First unzip data.zip. Then "cd" to the unzipped folder, for example "~/Downloads/data". Then type command:
```
find ./dc -exec curl http://localhost:5000/article -X POST -H "Content-Type: text/xml" --data-binary "@{}" -H "label: dc" \;
find ./marvel -exec curl http://localhost:5000/article -X POST -H "Content-Type: text/xml" --data-binary "@{}" -H "label: marvel" \;
```

## Train

```
curl http://localhost:5000/train
```

## Predict
For example:
```
curl http://localhost:5000/predict -X POST --data-binary "@./dc/711.txt"
```