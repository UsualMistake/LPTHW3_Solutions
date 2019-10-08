# Create a function named cheese_and_crackers that takes in two parameters: cheese_count and boxes_of_crackers.
def cheese_and_crackers(cheese_count, boxes_of_crackers):
  # Inside cheese_and_crackers print out the values passed in as arguments to the console.
  print(f"You have {cheese_count} cheeses!")
  print(f"You have {boxes_of_crackers} boxes of crackers!")
  # print out other messages
  print("Man that's enough for a party!")
  print("get a blanket.\n")

# print an intro message before calling the function
print("We can just give the function numbers directly:")
# call the function cheese_and_crackers and pass in two numbers: 20, 30
cheese_and_crackers(20, 30)


# print out an intro message before calling the function
print("OR, we can use variables from our script:")
# create two variables and give each a value
amount_of_cheese = 10
amount_of_crackers = 50

# call in function cheese_and_crackers and pass in the the two variables created.
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# print out an intro message before calling the function
print("We can even do math inside too:")
# Call in the function cheese_and_crackers and pass in two math operations
cheese_and_crackers(10 + 20, 5 + 6) # 30, 11

# print out an intro message before calling the function
print("And we can combine the two, variables and math:")
# Call in the function cheese_and_crackers and pass in two math operations using the variables created above with a literal number.
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000) # 110, 1050


#### STUDY DRILL 3 #####
## CREATE YOUR OWN FUNCTION AND CALL IT 10 TIMES

def bucket_list_plan(countries, age, name):
  print(f"Hello {name},")
  print(f"You're {age} years old")
  print(f"and you would like to visit {countries[0]}, {countries[1]}, and {countries[2]}")

countries = ['Australia', 'Germany', 'Russia']

#call 1:
# bucket_list_plan(countries, 28, 'Nelson')
#call 2:
# bucket_list_plan(countries, 20 + 9, 'Nelson')
#call 3:
# age = 30
# bucket_list_plan(countries, age, 'Nelson')
#call 4:
# name = "Nelson"
# bucket_list_plan(countries, 31, name)
#call 5:
# age = 32
# name = "Nelson"
# bucket_list_plan(countries, age, name)
#call 6:
# age = 33
# name = "Nelson"
# bucket_list_plan(countries, age + 1, name)
#call 7:
# countries[0] = "England"
# countries[1] = "Ireland"
# countries[2] = "Greece"
# age = 34
# name = "Nelson"
# bucket_list_plan(countries, age, name)
#call 8:
# age = 35
# name = "Nelson"
# bucket_list_plan(countries, age, name + " Alexander")
#call 9:
# age = 36
# name = "Nelson"
# bucket_list_plan(countries, age + 1, name + " Alexander")
#call 10:
countries[2] = "any country in Africa"
age = 37
name = "Nelson"
bucket_list_plan(countries, age, name)
