# import argv to take in arguments
from sys import argv

# create three variables, two take in argv
# the store store '> ' 
script, user_name, age = argv
prompt = '> '

# print and prompt user three times
print(f"Hi {user_name}, I'm the {script} script")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("what kind of computer do you have?")
computer = input(prompt)

# finally, print a targetted massage based on the user's responses.
print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure what that is.
And you have a {computer} computer. Nice.
You are {age} years old.
""")
