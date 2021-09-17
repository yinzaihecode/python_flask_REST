from flask import Flask, request
from flask_restful import Api, Resource, reqparse
from flask_jwtlogin import *

from security import authenticate, identity

# 인증은 post로
# api 콜했을때 토큰이 리턴됨.

app = Flask(__name__)
api = Api(app)
app.secret_key = 'jose'
items = []


# jwt = JWTLogin(app, authenticate, identity)
# 맨위에 배열선언,
# 딕셔너리 만들어서 어펜드 국룰


class Item(Resource):

    def get(self, name):
        item = next(filter(lambda x: x['name'] == name, items), None)
        return {'item': item}, 200 if item else 404

        # for item in items:
        #     if item['name'] == name:
        #         return item
        #     return {'item': None}, 404

    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items), None) is not None:
            return {'msg': "An item with name '{}' already exists.".format(name)}, 400

        data = request.get_json()  # silent=True,force=True

        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201

    def delete(self, name):
        global items
        items = list(filter(lambda x: x['name'] != name, items))
        return {'message': 'Item deleted'}

    def put(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument('price', type=float, required=True, help="this field cannot be left blank!")

        data = parser.parse_args()
        print(data['another'])

        item = next(filter(lambda x: x['name'] == name, items), None)
        if item is None:
            item = {'name': name, 'price': data['price']}
            items.append(item)
        else:
            item.update(data)

        return item


class ItemList(Resource):
    def get(self):
        return {'items': items}


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

app.run(port=5000, debug=True)
