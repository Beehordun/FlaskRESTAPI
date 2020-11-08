from werkzeug.security import safe_str_cmp

from db.user import User
from db.userdbmanager import UserDbManager

def authenticate(email, password):
    user = UserDbManager.get_user_by_email(email)
    if user and safe_str_cmp(user.password, password):
        return user

def identity(payload):
    user_id = payload['identity']
    return UserDbManager.get_user_by_id(user_id)
