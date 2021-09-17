from flask import Flask, jsonify, request, render_template
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

@app.route('/')
def home():
    return render_template('index.html')


# POST - used to receive data
# GET - used to send data back only
# POST /store data: {name: }


# POST /store data: {name:}
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],  #Json
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)


# GET /store<string:name>
@app.route('/store/<string:name>', methods=['GET']) # 'http://localhost:5000/store/some_name'
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message': 'store not found!'})


    # # Iterate over stores.
    # if the store name matches, return it
    # if none match, return an error message.not

# GET /store
@app.route('/store', methods=['GET'])
def get_stores():
    return jsonify({'stores': stores})


#1. 이터레이터
#2. match 검사
#3. 변수선언,  save, append.
#4. return


# POST /store/<string:name>/item {name:, price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'meesage': 'store not found.'})


# GET /store/<string:name>/item
@app.route('/store/<string:name>/item', methods=['GET'])
def get_items_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store['items': store['items']])



#run

app.run(port=5000)