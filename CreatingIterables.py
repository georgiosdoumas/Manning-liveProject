class Count:
    def __init__(self, max_element):
        self.limit = max_element
    def __getitem__(self, index):
        if index < self.limit:
            return index
        else:
            raise IndexError

class Fibonacci:
    def __init__(self, maxfib):
        # set the maximum number of Fibonacci numbers
        self.limit = maxfib
        self.previous = 1
        self.current = 1
        
    def __getitem__(self, index):
      if index < self.limit:
          if index == 0:
              return self.previous
          elif index == 1:
              return self.current
          else:
              temp = self.previous + self.current
              self.previous = self.current
              self.current = temp
              return self.current
      else:
          raise IndexError

counter01 = Count(5)
print("At any point in the program:", counter01[0])
for i in counter01 :
    print(i)

try:
    print("At any point in the program:", counter01[6])  # produces the IndexError
except IndexError:
    print("You went too far!")

fib_iterable = Fibonacci(8)
for number in fib_iterable:
    print(number)
