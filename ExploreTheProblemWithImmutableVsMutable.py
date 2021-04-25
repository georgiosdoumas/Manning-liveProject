int01 = 10
int02 = int01
print("We just declared:")
print(f" int01 with assigned value {int01} and it has  id {id(int01)}")
print(f" int02 = int01 and int02 has value {int02} and id {id(int02)}")
# id is the same for both variables
int02 = 20
print(f"After doing int02 = 20 we have:")
print(f"id(int01) = {id(int01)} and value int01 = {int01}")
print(f"id(int02) = {id(int02)} and value int02 = {int02}")
str01 = 'c'
str02 = str01
print("Similar with strings")
print(f"str01 has id {id(str01)} and value {str01}")
print(f"str02 has id {id(str02)} and value {str02}")
str02 = 'g'
print(f"After doing : str02 = 'g' ")
print(f"str01 has id {id(str01)} and value {str01}")
print(f"str02 has id {id(str02)} and value {str02}")

list01 = [1, 'f', 20]
list02 = list01
print(f" list01 has id {id(list01)} and value {list01}")
print(f" list02 has id {id(list02)} and value {list02}")
list02[2] = 2
print(f" list01 has id {id(list01)} and value {list01}")
print(f" list02 has id {id(list02)} and value {list02}")
list01[1] = 'gg'
print(f" list01 has id {id(list01)} and value {list01}")
print(f" list02 has id {id(list02)} and value {list02}")
list01 = ['new', 'list']
print(f" list01 has id {id(list01)} and value {list01}")
print(f" list02 has id {id(list02)} and value {list02} still!")
list01 = [1, 'gg', 2]  # this is the value that currently list02 has
print(f" list01 has id {id(list01)} and value {list01}") 
print(f" list02 has id {id(list02)} and value {list02}")
list03 = [3,2,1]
list04 = [3,2,1]  # this way it will get a different id from list03
print(f" list03 has id {id(list03)} and value {list03}") 
print(f" list04 has id {id(list04)} and value {list04}")
# And if I change list03[1] then the value of list04 will of course not be affected.
list03[1] = 10
print(f" list03 has id {id(list03)} and value {list03}") 
print(f" list04 has id {id(list04)} and value {list04}")

dict01 = {1:'a', 2:'b'}
dict02 = dict01
print(f" dict01 has id {id(dict01)} and value {dict01}")
print(f" dict02 has id {id(dict02)} and value {dict02}")
dict02[3] = ['c', 'd']
print(f" dict01 has id {id(dict01)} and value {dict01}")
print(f" dict02 has id {id(dict02)} and value {dict02}")
dict01[3][1] = 'D'
print(f" dict01 has id {id(dict01)} and value {dict01}")
print(f" dict02 has id {id(dict02)} and value {dict02}")

nestedlist01 = [[1,2], ['a', 'b', 'c']]
nestedlist02 = nestedlist01
print(f" nestedlist01 has id {id(nestedlist01)} and value {nestedlist01}") 
print(f" nestedlist02 has id {id(nestedlist02)} and value {nestedlist02}")
nestedlist02[1][2] = 'C'
print(f" nestedlist01 has id {id(nestedlist01)} and value {nestedlist01}") 
print(f" nestedlist02 has id {id(nestedlist02)} and value {nestedlist02}")
nestedlist01[0] = [10, 20]
print(f" nestedlist01 has id {id(nestedlist01)} and value {nestedlist01}") 
print(f" nestedlist02 has id {id(nestedlist02)} and value {nestedlist02}")
