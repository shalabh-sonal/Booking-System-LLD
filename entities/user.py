class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.is_authenticated = False

    def login(self):
        self.is_authenticated = True

    def logout(self):
        self.is_authenticated = False
