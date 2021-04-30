class Price:
    def __init__(me, input_part_number, input_price):
        me.price = input_price
        me.part_number = input_part_number
    def get_price(self):   ## it works even if I use self here and not me ! 
        return  self.price

def seperate_set_discount(some_item_price, some_percent_off):
    some_item_price.percent_off = some_percent_off

def seperate_get_discount_price(some_item_price):
    return some_item_price.get_price() * some_item_price.percent_off 

item_price = Price("123-AF", 123.5) 
print(f"The price of item {item_price.part_number} is {item_price.get_price()} $")
print("dir(Price):\n", dir(Price))
print("Price.__dict__:\n", Price.__dict__)
print("dir(item_price):\n", dir(item_price))
print("item_price.__dict__:\n", item_price.__dict__)
seperate_set_discount(item_price, 0.20)
print("\n We applied the seperate function for setting discount as an extra attribute")
print("The price for item will  have a discount of {:.2f} \n".format(seperate_get_discount_price(item_price)))

print("dir(Price):\n", dir(Price))            # this did not change
print("Price.__dict__:\n", Price.__dict__)    # this did not change
print("dir(item_price):\n", dir(item_price))             #this shows the new attribute 'percent_off'
print("item_price.__dict__:\n", item_price.__dict__)     #this shows the new attribute 'percent_off'
