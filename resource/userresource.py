from flask_restful import Api, Resource, reqparse
from db.userdbmanager import UserDbManager

class UserResource(Resource):
    TABLE_NAME = 'Users'

    parser = reqparse.RequestParser()
    parser.add_argument(name = 'username', 
    type=str, 
    required=True, 
    help="Username cannot be blank"
    )

    parser.add_argument(name = 'password', 
    type=str, 
    required=True, 
    help="Password cannot be blank"
    )

    parser.add_argument(name = 'email', 
    type=str, 
    required=True, 
    help="Email cannot be blank"
    )

    def post(self):
        data = UserResource.parser.parse_args()

        user = UserDbManager.get_user_by_email(data['email'])

        if user:
            return {'message': 'User with name: {name}, password: {password} and email: {email} already exists'.
            format(name=data['username'], password=data['password'], email=data['email'])}, 400
        else:
            UserDbManager.insert_user(data['username'], data['password'], data['email'])
            return {'message': 'User created succesfully'}, 201
