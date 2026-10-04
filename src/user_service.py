class UserService:

    def __init__(self):
        self.users = []

    def create_user(self, name, email):
        user = {
            "name": name,
            "email": email
        }

        self.users.append(user)
        return user

    def get_users(self):
        return self.users