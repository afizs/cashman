# cashman 

# 1. date 
# 2. Amount 
# 3. Name 
# 4. Type 

from datetime import datetime

transactions = [] 

while(True):
    print("1. Enter your transaction details") 
    print("2. Show All expenses")
    print("3. Show All income")
    print("4. Show the Balance")
    print("5. Show all transactions")

    choice = int(input())

    if choice ==1:
        amount = int(input("Enter the amount: "))
        name =  input("enter the descripton: ")
        type_of = input("Type of your transcation (Income/Expense)")
        date = datetime.now()
        transaction = {}
        transaction['amount'] = amount
        transaction['name'] = name
        transaction['type_of'] = type_of
        transaction['date'] = date

        transactions.append(transaction)
    elif choice ==2:
        pass
    elif choice ==3:
        pass
    elif  choice == 4:
        pass
    else:
        print(transactions)