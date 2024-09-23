import logging
import json
from datetime import datetime

logger = logging.getLogger(__name__)

class DataManager:
    def __init__(self):
        self.users_file = "users.json"
        self.users = self.load_users()

    def load_users(self):
        try:
            with open(self.users_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def save_users(self):
        with open(self.users_file, 'w') as f:
            json.dump(self.users, f)

    def get_user_profile(self, user_id):
        return self.users.get(str(user_id), {})

    def update_user_profile(self, user_id, data):
        if str(user_id) not in self.users:
            self.users[str(user_id)] = {}
        self.users[str(user_id)].update(data)
        self.users[str(user_id)]['last_updated'] = datetime.now().isoformat()
        self.save_users()

    def delete_user_data(self, user_id):
        if str(user_id) in self.users:
            del self.users[str(user_id)]
            self.save_users()

    def anonymize_data(self, data):
        # Implement data anonymization logic here
        # This is a placeholder implementation
        anonymized_data = data.copy()
        if 'name' in anonymized_data:
            anonymized_data['name'] = 'Anonymous'
        if 'phone' in anonymized_data:
            anonymized_data['phone'] = 'XXXXXXXXXX'
        return anonymized_data
