print("How old are you?", end=" ")
age = input()
print("How tall are you?", end=" ")
height = input()
print("How much do you weight?", end= " ")
weight = input()

print(f"So You're {age} years old, {height} inches tall and {weight} lbs heavy.")

print(f"everything combined totals = {int(age) + int(height) + int(weight)}")
