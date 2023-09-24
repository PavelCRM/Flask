class User:
    users = []

    def __init__(self, id, name, email, password):
        self.id = id
        self.name = name
        self.email = email
        self.password = password

    def validate(self):
        required_fields = ["id", "name", "email", "password"]

        for field in required_fields:
            if not hasattr(self, field):
                return False

        return True

    def save(self):
        User.users.append(self)

    def delete(self):
        User.users = [user for user in User.users if user.id != self.id]

    @classmethod
    def find_by_id(cls, user_id):
        return next((user for user in cls.users if user.id == user_id), None)

    @staticmethod
    def get_all():
        return User.users
