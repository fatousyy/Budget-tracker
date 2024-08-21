# main.py

from tracker import Tracker
from data_manager import DataManager
from transaction import Transaction

def main():
    tracker = Tracker()
    data_manager = DataManager()

    # Load existing transactions
    loaded_transactions = data_manager.load_data()
    tracker.transactions = [Transaction(**t) for t in loaded_transactions]

    while True:
        print("\nBudget Tracker Menu:")
        print("1. Add Transaction")
        print("2. View Summary by Category")
        print("3. View Total Expense")
        print("4. Save and Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            description = input("Enter description: ")
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            tracker.add_transaction(description, amount, category)
        elif choice == '2':
            summary = tracker.get_summary_by_category()
            for category, total in summary.items():
                print(f"{category}: ${total}")
        elif choice == '3':
            print(f"Total Expense: ${tracker.get_total_expense()}")
        elif choice == '4':
            data_manager.save_data(tracker.transactions)
            print("Data saved. Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
