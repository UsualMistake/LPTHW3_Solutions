# import neccesary modules
from sys import argv

#create two variables that take in argv
script, filename = argv

# pass-in the file in filename and store 
# it in variable txt
txt = open(filename)

#print  the message below
print(f"Here is your file {filename}:")
# read the file stored in txt
print(txt.read())

# prompt user for filename and store
# the value in variable file_again
print("Type the filename again:")
file_again = input("> ")

# store the value passed in file_again into txt_again
txt_again = open(file_again)

# read and print value in txt_again
print(txt_again.read())

