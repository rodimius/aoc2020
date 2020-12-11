import lilParser

numbers = lilParser.parse("./1/input")

def findProduct2():
  for first in numbers:
    for second in numbers:
      if first + second == 2020:
        print(first)
        print(second)
        print(first * second)
        return

def findProduct3():
  for first in numbers:
    for second in numbers:
      for third in numbers:
        if first + second + third == 2020:
          print(first)
          print(second)
          print(third)
          print(first * second * third)
          return

findProduct2()
findProduct3()
