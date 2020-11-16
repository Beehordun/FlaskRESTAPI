class User(object):
    def __init__(self, id, username, password, email):
        self.id = id
        self.username = username
        self.email = email
        self.password = password
    
    def json(self):
        return {'id': self.id, 'username': self.username, 'email': self.email, 'password': self.password}

