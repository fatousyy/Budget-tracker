# tracker.py

from transaction import Transaction

class Tracker:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, description, amount, category, date=None):
        transaction = Transaction(description, amount, category, date)
        self.transactions.append(transaction)

    def get_summary_by_category(self):
        summary = {}
        for transaction in self.transactions:
            if transaction.category in summary:
                summary[transaction.category] += transaction.amount
            else:
                summary[transaction.category] = transaction.amount
        return summary

    def get_total_expense(self):
        return sum(t.amount for t in self.transactions)
