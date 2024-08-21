# transaction.py

from datetime import datetime

class Transaction:
    def __init__(self, description, amount, category, date=None):
        self.description = description
        self.amount = amount
        self.category = category
        self.date = date if date else datetime.now().strftime("%Y-%m-%d")

    def __repr__(self):
        return f"{self.date} - {self.category}: {self.description} (${self.amount})"
