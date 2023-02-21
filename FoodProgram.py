# Import the class
import FoodClass as fc

# this dictionary represents transactions. The key of the dictionary is the transaction identifier.
# The Value of the dictionary is a list. The elements in each list are -
# ['Date', 'Name of item', 'Cost', 'customerid' ]

# Initialize necessary variables
dict = {
    "trans1": ["2/15/2023", "The Lone Patty", 17, 569],
    "trans2": ["2/15/2023", "The Octobreakfast", 18, 569],
    "trans3": ["2/15/2023", "The Octoveg", 16, 570],
    "trans4": ["2/15/2023", "The Octoburger", 20, 570],
}

order_total = 0
member_discount = 0.2


# CUSTOMERS
# Customer 1
customerid = 570
name = "Danni Sellyar"
address = "87 Mitchell Way Hewitt Texas 76712"
email = "dsellyarft@gmpg.org"
phone = "254-555-9362"
member_status = False

# Customer 2
customerid = 569
name = "Aubree Himsworth"
address = "1172 Moulton Hill Waco Texas 76710"
email = "ahimsworthfs@list-manage.com"
phone = "254-555-2273"
member_status = True


# PROGRAM
# Initializing the customer
customer = fc.Customer(customerid, name, address, email, phone, member_status)


# Printing the customer name and phone number
print(f"Customer Name: {customer.get_name()}")
print(f"Phone: {customer.get_phone()}")


# Cycling through the dictionary to find relevant transactions
for transaction in dict:
    if dict[transaction][3] == customer.get_customerid():
        # Initializing the transaction
        transaction = fc.Transaction(
            dict[transaction][0],
            dict[transaction][1],
            dict[transaction][2],
            dict[transaction][3],
        )

        # Displaying the item name and cost
        print(
            f"Order Item: {transaction.get_item_name()}  Price: ${format(transaction.get_cost(), '.2f')}"
        )

        # Calculating the runnning total
        order_total += float(transaction.get_cost())


# Printing the total cost (running total)
print(f"Total Cost: ${format(order_total, '.2f')}")


# Displaying the member discount
if customer.get_member_status() == True:
    # Calculating the discount
    discount = order_total * member_discount

    # Calculating the total amount
    order_total -= discount

    # Printing the results
    print(f"Member Discount: ${format(discount, '.2f')}")
    print(f"Total Cost after discount: ${format(order_total, '.2f')}")
