class User:
    users = []

    def __init__(self, id, name, email, password):
        self.id = id
        self.name = name
        self.email = email
        self.password = password

    def __dict__(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "password": self.password,
        }


def get_user_by_id(user_id):
    return next((user for user in User.users if user.id == user_id), None)


def add_user(user):
    new_user = User(**user.dict())
    User.users.append(new_user)
    return new_user


def update_user(user_id, updated_user):
    user = get_user_by_id(user_id)
    user.name = updated_user.name
    user.email = updated_user.email
    user.password = updated_user.password
    return user


def delete_user(user_id):
    user = get_user_by_id(user_id)
    User.users = [u for u in User.users if u.id != user_id]
    return user
