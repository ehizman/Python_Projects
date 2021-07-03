import time

option = input("""
Type 1 to continue 
Press 2 to continue """)

list_of_transaction = list()
while option == "1":
    name: str = input("Enter the customer name: ").upper()
    quantity: int = int(input("Enter the quantity of products: "))
    price: int = int(input("Enter the price: "))
    total: int = quantity * price

    transaction_tuple = (name, quantity, price, total, time.ctime().upper())
    list_of_transaction.append(transaction_tuple)
    print(f"Transaction saved -----> {transaction_tuple}")
    option = input("""
Type 1 to continue 
Press 2 to continue """)

print("%-25s%-25s%-25s%-25s%-25s" % ("name", "quantity", "price", "total", "time of transaction"))
for i in list_of_transaction:
    print("%-25s%-25s%-25s%-25s%-25s" % i)
print("Exiting application")

