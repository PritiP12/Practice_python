def is_valid(pin):
    return True if(len(pin)in[4,6] and pin.isdigit()) else False
#pin=int(input("Enter Pin:"))
print(is_valid('789123'))