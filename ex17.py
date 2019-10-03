# Below are two versions of the same script. 
# One shorter than the other. 
# The longer has been commented out.


from sys import argv
from os.path import exists

script, from_file, to_file = argv

# print(f"Copying from {from_file} to {to_file}")

# # In two-line
# in_file = open(from_file)
# indata = in_file.read()

# In one line
indata = open(from_file).read()
#in_file = open(from_file).read()

print(f"The input file is {len(indata)} bytes long")

out_file = open(to_file, 'w').write(indata)
# out_file.write(indata)


print(f"Does the output file exist? {exists(to_file)}")
# print("Ready, hit RETURN to continue, CTRL-C to abort.")
# input()


print("Alright, all done.")

# out_file.close()
# # in_file.close()
