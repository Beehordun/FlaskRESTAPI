from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt import JWT, current_identity, jwt_required

from resource.userresource import UserResource
from resource.itemresource import ItemResource, ItemsResource

from application.security import authenticate, identity



api = Api()
api.add_resource(ItemResource, '/item/<string:name>')
api.add_resource(ItemsResource, '/items')
api.add_resource(UserResource, '/user')

def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')
    jwt = JWT(app= app, authentication_handler= authenticate, identity_handler= identity)

    @jwt.jwt_error_handler
    def customized_error_handler(error):
        return jsonify({
                       'message': error.description,
                       'code': error.status_code
                   }), error.status_code
                    
    with app.app_context():
        api.init_app(app)
        return app