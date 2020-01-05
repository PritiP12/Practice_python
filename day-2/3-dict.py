'''Create a function that determines whether a shopping order is eligible for free shipping.
 An order is eligible for free shipping if the total cost of items purchased exceeds $50.00.
'''
def free_shipping(order):
    if (sum(order.values())>=50):
        print("sorry...!! shopping order is eligible for free shipping")
    else:
        print("shopping order is not eligible for free shipping")
free_shipping({ "Shampoo": 5.99, "Rubber Ducks": 15.99 })