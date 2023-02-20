import FoodClass as fc

# this dictionary represents transactions. The key of the dictionary is the transaction identifier.
# The Value of the dictionary is a list. The elements in each list are -
# ['Date', 'Name of item', 'Cost', 'customerid' ]

dict = {
    "trans1": ["2/15/2023", "The Lone Patty", 17, 569],
    "trans2": ["2/15/2023", "The Octobreakfast", 18, 569],
    "trans3": ["2/15/2023", "The Octoveg", 16, 570],
    "trans4": ["2/15/2023", "The Octoburger", 20, 570],
}

order_total = 0
member_discount = 0.2


# Customer 1
customerid = 570
name = "Danni Sellyar"
address = "87 Mitchell Way Hewitt Texas 76712"
phone = "254-555-9362"
email = "dsellyarft@gmpg.org"
member_status = False


# Customer 2
customerid = 569
name = "Aubree Himsworth"
address = "1172 Moulton Hill Waco Texas 76710"
phone = "254-555-2273"
email = "ahimsworthfs@list-manage.com"
member_status = True


# Program
customer = fc.Customer(customerid, name, address, email, phone, member_status)

print(f"Customer Name: {customer.get_name()}")
print(f"Phone: {customer.get_phone()}")

for transaction in dict:
    if dict[transaction][3] == customerid:
        print(
            f"Order Item: {dict[transaction][1]}  Price: ${format(dict[transaction][2], '.2f')}"
        )
        itemcost = float(dict[transaction][2])
        order_total += itemcost

print(f"Total Cost: ${format(order_total, '.2f')}")

if customer.get_member_status() == True:
    discount = order_total * member_discount
    order_total -= discount
    print(f"Member Discount: ${format(discount, '.2f')}")
    print(f"Total Cost after discount: ${format(order_total, '.2f')}")
