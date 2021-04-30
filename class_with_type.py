class Price:
    def __init__(self, input_part_number, input_price):
        self.price = input_price
        self.part_number = input_part_number
    def get_price(self):
        return  self.price

def function__init__(me, input_part_number, input_price):
    me.part_number = input_part_number
    me.price = input_price

def function_get_price(me):
    return me.price

namespace = {"__init__": function__init__, "get_price": function_get_price}

Price2 = type('fromTypePrice', (), namespace)

bicycle_price = Price('AF3456', 300.00)
print(f"The price of bicycle {bicycle_price.part_number} is {bicycle_price.get_price()} $")

car_price = Price2('BMW', 30000.00)
print(f"The price of car {car_price.part_number} is {car_price.get_price()} $")
