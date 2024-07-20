from flask import Flask,render_template,request,jsonify

app=Flask(__name__)


items=[
    {
        'id':1,
        'name':'item1',
        'price':15.99,
        'quantity':1
    },
    {
        'id':2,
        'name':'item2',
        'price':25.99,
        'quantity':1
    }
]

@app.route('/')
def home():
    return "WELCOME TO THE API"

@app.route('/items',methods=['GET'])
def get_items():
    return jsonify(items)

@app.route('/items/<int:item_id>',methods=['GET'])
def get_item(item_id):
    item=next((item for item in items if item['id']==item_id),None)
    if item is None:
        return jsonify({'message':'Item not found'}),404
    return jsonify(item)


@app.route('/items',methods=['POST'])
def create_item():
    if not request.json or not 'name' in request.json:
        return jsonify({'message':'Bad request'}),400
    data=request.get_json()
    new_item={
        'id':items[-1]['id']+1,
        'name':data['name'],
        'price':data['price'],
        'quantity':data['quantity']
    }
    items.append(new_item)
    return jsonify(new_item),201

@app.route('/items/<int:item_id>',methods=['PUT'])
def update_item(item_id):
    item=next((item for item in items if item['id']==item_id),None)
    if item is None:
        return jsonify({'message':'Item not found'}),404
    item['name']=request.json.get('name',item['name'])
    item['price']=request.json.get('price',item['price'])
    item['quantity']=request.json.get('quantity',item['quantity'])
    return jsonify(item)

@app.route('/items/<int:item_id>',methods=['DELETE'])
def delete_item(item_id):
    item=next((item for item in items if item['id']==item_id),None)
    if item is None:
        return jsonify({'message':'Item not found'}),404
    items.remove(item)
    return jsonify({'message':'Item deleted'}),200



if __name__ == '__main__':
    app.run(debug=True)