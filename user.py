class User:
    def __init__(self, email, user, password, key = None):
        self.key = key
        self.email = email
        self.user = user
        self.password = password

