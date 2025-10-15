import json
import os

from user_data import UserData


class UserManager:
    def __init__(self):
        self.json_path = 'user_data.json'
        self.users = self._create_dict()
        self.new_user_count = 0

    def add_user(self, user: UserData):
        if not self._user_exists(user.id) and user.username is not None:
            self.users[user.id] = user.to_dict()
            self.new_user_count += 1
            return True

        return False

    def create_user(self, user_id: int, username: str, firstname: str, lastname: str, phone_number: str) -> UserData:
        return UserData(user_id, username, firstname, lastname, phone_number)

    def save_users_to_json(self):
        if self.users:
            with open(self.json_path, 'w', encoding='utf-8') as f:
                json.dump(self.users, f, ensure_ascii=False, indent=2)

    def _load_from_json(self):
        if not os.path.exists(self.json_path):
            return None

        users = list()
        with open(self.json_path, 'r', encoding='utf-8') as f:
            try:
                users = json.load(f)
            except FileNotFoundError as e:
                print(e)
        return users  # dict

    def _user_exists(self, user_id):
        return str(user_id) in self.users

    def _create_dict(self):
        return self._load_from_json()

    def get_users_count(self):
        return len(self.users)
