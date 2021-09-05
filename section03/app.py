from flask import Flask, jsonify
# package import Class

app = Flask(__name__)

stores = [
    {
        'name': 'My Wonderful Store',
        'items': [
            {
                'name': 'My Item',
                'price': 15.99
            }
        ]
    }
]


# POST - used to receive data
# GET - used to send data back only
# POST /store data: {name: }


# POST /store data: {name:}
@app.route('/store', methods=['POST'])
def create_store():
    pass


# GET /store<string:name>
@app.route('/store/<string:name>') #'http://localhost:5000/store/some_name'
def get_store(name):
    pass


# GET /store
@app.route('/store')
def get_stores():
    return jsonify


# POST /store/<string:name>/item {name:, price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    pass


# GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    pass

#run

app.run(port=5000)