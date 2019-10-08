# import the argv module
from sys import argv

# store argv values in variables: script and input_file
script, input_file = argv

# define a function called print_all that takes in
# an argument 'f'. Inside the function read and print value
# passed in parameter 'f'
def print_all(f):
  print(f.read())

# define a function named rewind that takes in an 
# argument 'f'. Inside rewind function start reading from first character.
def rewind(f):
  f.seek(0)

# define function named print_a_line that takes in
# two arguments 'line_count' and 'f'
# print values passed in as parameters.
def print_a_line(line_count, f):
  print(line_count, f.readline())

# open and store input_file passed in through argv
# and store it in a variable called current_file.
current_file = open(input_file)

# print 'First let's print the whole file:' to the console.
print("First lets print the whole file:\n")
# call in function print_all and pass in the value
# in the variable created above, current_file.
print_all(current_file)

# print 'Now let's rewind, kind of like a tape.'
print("Now let's rewind, kind of like a tape.")
# call in function rewind with current_file as argument.
rewind(current_file)
# print 'let's print three line:' to the console.
print("Let's print three lines:")
# create variable current_line and store 1
current_line = 1
# call in function print_a_line and pass in two arguments:
# current_line and current_file.
# should print: 'current_line value ' + 'current_line in file value' e.g. 1 This is line 1
print_a_line(current_line, current_file)

# Call in print_a_line two more times
# update the value of current_line
current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
