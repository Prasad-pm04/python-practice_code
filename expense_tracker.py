expenses = {}

def add_expense(date, amount, category):
    if date not in expenses:
        expenses[date] = []
    expenses[date].append({'amount': amount, 'category': category})
    print(f"Added ₹{amount} to {category} on {date}")

def show_expenses():
    for date, records in expenses.items():
        print(f"\n📅 Date: {date}")
        for record in records:
            print(f"   ₹{record['amount']} - {record['category']}")

def total_spent():
    total = sum(record['amount'] for records in expenses.values() for record in records)
    print(f"\n💰 Total Spent: ₹{total}")

# Sample usage
add_expense("2025-07-15", 200, "Groceries")
add_expense("2025-07-15", 50, "Snacks")
add_expense("2025-07-14", 500, "Travel")

show_expenses()
total_spent()
