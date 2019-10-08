def add(a, b):
  print(f"ADDING {a} + {b}")
  return a + b

def substract(a, b):
  print(f"SUBSTRACTING {a} - {b}")
  return a - b

def multiply(a, b):
  print(f"MULTIPLYING {a} * {b}")
  return a * b

def divide(a, b):
  print(f"DIVIDING {a} / {b}")
  return a / b

print("Let's do some math with just functions!")

age = add(30, 5)
height = substract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Age: {age}, height: {height}, weight: {weight}, IQ: {iq}")


# A puzzle: print 'here is a puzzle'
print("He is a puzzle")

# What is the value of what?
# devide = 50/2 = 25
# multiply = 180 * 25 = 4500
# substract = 74 - 4500 = -4426
# addition = 35 + -4426 = -4391
# what should = -4391
what = add(age, substract(height, multiply(weight, divide(iq, 2))))

print("That becomes: ", what, "can you do it by hand?")
