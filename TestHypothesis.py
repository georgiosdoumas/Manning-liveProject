# I used the id() in the previous solution, so here I am testing something more
element01 = [3,2]
element02 = ['c', 'b']
list01 = [element01, element02]
list02 = list01
print(f" list01 has id {id(list01)} and value {list01}")
print(f" list02 has id {id(list02)} and value {list02}")
element01[0] = 30
print(f" list01 has id {id(list01)} and value {list01}")
print(f" list02 has id {id(list02)} and value {list02}")
