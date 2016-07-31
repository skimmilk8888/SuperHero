from flask import Flask, request
from flask_restful import Resource, Api, abort
from train import MachineLearning
from db import init_db, add_record, read_record, delete_record, update_record, list_records

app = Flask(__name__)
api = Api(app)
init_db()
ml = MachineLearning()

class Article(Resource):
    def get(self, id):
        data, label = read_record(id)
        if data is None:
            abort(404, message='Article {} doesn\'t exist'.format(id))
        return {"id": id, "data": data, "label": label}

    def delete(self, id):
        if not delete_record(id):
            abort(404, message='Article {} doesn\'t exist'.format(id))
        return '', 204

    def put(self, id):
        data = request.get_data()
        label = request.headers.get('label')
        update_record(id, data, label)
        return data, 201

# shows a list of all articles, and lets you POST to add new articles
class ArticleList(Resource):
    def get(self):
        ids = list_records()
        return [{'id': id} for id in ids]

    def post(self):
        data = request.get_data()
        label = request.headers.get('label')
        add_record(data, label)
        return '', 201

class Train(Resource):
    def get(self):
        ml.init_training()
        # Fetch training data
        ids = list_records()
        for id in ids:
            data, label = read_record(id)
            ml.add_training_data(data, 0 if label == 'dc' else 1)
        ml.train()
        return '', 201

class Predict(Resource):
    def post(self):
        data = request.get_data()
        result = 'dc' if ml.predict(data) == 0 else 'marvel'
        return result, 201

api.add_resource(ArticleList, '/article')
api.add_resource(Article, '/article/<int:id>')
api.add_resource(Train, '/train')
api.add_resource(Predict, '/predict')

if __name__ == '__main__':
    app.run()