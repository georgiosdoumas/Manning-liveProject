class CountIterator:
  def __init__(self, limit):
      self.limit = limit
      self.count = 0  
  def __next__(self):
      if self.count < self.limit:
          value = self.count
          self.count += 1
          return value
      else:
          raise StopIteration
  def __iter__(self):
      return self

class FibonaciIterator:
    def __init__(self, maxfib):
        self.limit = maxfib
        self.previous = 1
        self.current = 1
        self.count = 0
    def __next__(self):
      if self.count < self.limit:
          if self.count == 0:
              self.count += 1
              return self.previous
          elif self.count == 1:
              self.count += 1
              return self.current
          else:
              temp = self.previous + self.current
              self.previous = self.current
              self.current = temp
              self.count += 1
              return self.current
      else:
          raise StopIteration
    def __iter__(self):
        return self

def count_generator(limit):
    count = 0
    while count < limit:
        yield count
        count += 1

def FibonaciGenerator(maxfib):
    previous = 0
    current = 1
    while current < maxfib:
        if previous == 0:
            yield current
            previous += 1
        else:
            yield current
            temp = current
            current = temp + previous
            previous = temp

            
countiter01 = CountIterator(10)
for c in countiter01:
    print(c)

countiter02 = CountIterator(5)
listc = [c for c in countiter02]
print(listc)       # [0, 1, 2, 3, 4] 

countiter03 = CountIterator(3)
print(countiter03)
print(next(countiter03))  # 0
print(next(countiter03))  # 1
print(next(countiter03))  # 2
try:
    print(next(countiter03))
except StopIteration:
    print("You went too far")

fib_iterator01 = FibonaciIterator(7)
for number in fib_iterator01:
    print(number)
fib_iterator02 = FibonaciIterator(8)
fib_list = [f for f in fib_iterator02 ]
print(fib_list)                 # [1, 1, 2, 3, 5, 8, 13, 21]

print("\n Generator:")
for x in count_generator(5):
    print(x)
print("\n Fibonaci Generator function:")
for f in FibonaciGenerator(11):  
    print(f)                # prints the fib numbers smaller than 11 : 1,1,2,3,5,8
