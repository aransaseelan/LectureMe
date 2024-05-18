from werkzeug.security import generate_password_hash, check_password_hash

class User: 
    ''' This is a class that represents a user. It has a username and a password. '''
    def __init__(self, username, password):
        self.username = username
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)