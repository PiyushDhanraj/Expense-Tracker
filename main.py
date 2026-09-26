import csv

expenses = []

try:
    with open("data\\expenses.csv", "r") as file:
        reader = csv.reader(file)

        for row in reader:
            expense = {
                "date": row[0],
                "description": row[1],
                "category": row[2],
                "amount": float(row[3])
            }

            expenses.append(expense)

except FileNotFoundError:
    pass

while True:
    print("\n==============================")
    print("   PERSONAL EXPENSE TRACKER")
    print("==============================")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Calculate Total")
    print("4. Delete Expense")
    print("5. Category Summary")
    print("6. Exit")
    print("==============================")

    choice = input("Enter your choice: ")

    if choice == "1":
        date = input("Enter date: ")
        description = input("Enter description: ")
        category = input("Enter category: ")

        while True:
            try:
                amount = float(input("Enter amount: "))

                if amount < 0:
                    print("Amount cannot be negative.")
                else:
                    break

            except ValueError:
                print("Please enter a valid number.")


        expense = { 
            "date": date,
            "description": description,
            "category": category,
            "amount": amount
        }

        expenses.append(expense)

        with open("data\\expenses.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([
                date,
                description,
                category,
                amount
            ])
        print("Expense added successfully")

    elif choice == "2":
        if len(expenses)==0:
            print("No expenses found.")
        else:
            print("\n===== ALL EXPENSES =====") 

            i = 1

            for expense in expenses:
                print(f"\nExpense {i}")
                print("Date:", expense["date"])
                print("Description:", expense["description"])
                print("Category:", expense["category"])
                print("Amount: ₹", expense["amount"])

                i += 1   

    elif choice == "3": 
        total = 0

        for expense in expenses:
            total = total + expense["amount"]

        print(f"Total Expenses: ₹{total}")
       

    elif choice == "4":
        if len(expenses)==0:
            print("No expenses found.")
        else:
            i=1

            for expense in expenses:
            
                print(f'{i}. {expense["description"]} ₹{expense["amount"]}')
                i+=1

            try:

                number = int(input("Enter expense number to delete: "))

                if number >=1 and number <= len(expenses):
                    expenses.pop(number - 1)

                    with open("data\\expenses.csv", "w", newline="") as file:
                        writer = csv.writer(file)

                        for expense in expenses:
                            writer.writerow([
                                expense["date"],
                                expense["description"],
                                expense["category"],
                                expense["amount"]
                            ])

                    print("Expense deleted successfully.")
                
                else:
                    print("Invalid expense number entered. Please try again.")
            except ValueError:
                print("Please enter a valid number.")

    elif choice == "5":
        if len(expenses) == 0:
            print("No expenses found.")
        else:
            categories = {}

            for expense in expenses:
                category = expense["category"]
                amount = expense["amount"]

                if category in categories:
                    categories[category] += amount
                else:
                    categories[category] = amount

            print("\n===== CATEGORY SUMMARY =====")

            for category in categories:
                print(category, ":", "₹", categories[category])

    elif choice == "6":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice. Please try again.")
