from flask_restful import Api, Resource, reqparse
from flask_jwt import jwt_required
from db.itemdbmanager import ItemDbManager
from db.item import Item

class ItemResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(name = 'price', 
    type=float, 
    required=True, 
    help="Price cannot be blank"
    )

    @jwt_required()
    def get(self, name):
        item = ItemDbManager.get_item_by_name(name)
        if item:
            result = {'name': name, 'price': item.price}
            return {'item': result}
        return {"message": "{} not found".format(name)}, 404


    @jwt_required()
    def post(self, name):
        item = ItemDbManager.get_item_by_name(name)
        if item:
             return {'message': '{} already exists'.format(name)}, 400
        
        data = ItemResource.parser.parse_args()
        
        ItemDbManager.insert_item(name, data['price'])
        item = {'name': name, 'price': data['price']}
        return {"item": item}, 201

    @jwt_required()
    def put(self, name):
        data = ItemResource.parser.parse_args()
        price = data['price']

        items = ItemDbManager.get_all_items()

        for item in items:
            if item.name == name:
                item.price = price
                ItemDbManager.update_item(item)
                return {'name': name, 'price': price}, 200

        item = {'name': name, 'price': price}
        ItemDbManager.insert_item(name, price)
        return {'name': name, 'price': price}, 201
    
    @jwt_required()
    def delete(self, name):
        items = ItemDbManager.get_all_items()
        for item in items:
            if item.name == name:
                ItemDbManager.delete_item(name)
                return {'message': '{} deleted'.format(name)}, 200
        return {'message': '{} not found'.format(name)}, 400


class ItemsResource(Resource):
    @jwt_required()
    def get(self):
        all_item = ItemDbManager.get_all_items()
        items = []

        for item in all_item:
            items.append({'name': item.name, 'price': item.price})

        return {'items': items}, 200