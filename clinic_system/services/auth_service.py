
class AuthService:
    def __init__(self, storage):
        self.storage = storage
        self.users = self.storage.load()

    def login(self, username, password):
        for user in self.users:
            if user["username"] == username and user["password"] == password:
                return user
        return None