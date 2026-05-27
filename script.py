from exercise1 import *

print(user_data["expenses"][1]["amount"])

def create_expense(amount, **kwargs):
    expense = {"amount":amount}
    expense.update(kwargs)
    return expense

final_data= create_expense(150, id=4, category="utilities")
print(final_data)...