from flask import Flask, request, jsonify
from flask_jwt import JWT, current_identity, jwt_required
from flask_restful import Api, Resource, reqparse

from resource.userresource import UserResource
from resource.itemresource import ItemResource, ItemsResource

from security import authenticate, identity

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['JWT_AUTH_USERNAME_KEY'] = 'email'
app.secret_key = "biodun"
api = Api(app)

jwt = JWT(app, authenticate, identity)

@jwt.jwt_error_handler
def customized_error_handler(error):
    return jsonify({
                       'message': error.description,
                       'code': error.status_code
                   }), error.status_code
        
        
api.add_resource(ItemResource, '/item/<string:name>')
api.add_resource(ItemsResource, '/items')
api.add_resource(UserResource, '/user')

app.run(port=5000)
