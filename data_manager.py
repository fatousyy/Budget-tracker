# data_manager.py

import json

class DataManager:
    def __init__(self, filename='transactions.json'):
        self.filename = filename

    def save_data(self, data):
        with open(self.filename, 'w') as file:
            json.dump([t.__dict__ for t in data], file)

    def load_data(self):
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []
