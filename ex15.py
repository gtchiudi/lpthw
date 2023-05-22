# import argv from sys module
from sys import argv

# unpack argv into script and filename
script, filename = argv
# open the file given from argv
txt = open(filename)

# print filename
print(f"Here's your file {filename}:")
# print contents of file given from read() function
print(txt.read())
txt.close()

# prompt for filename and read input
print("Type the filename again:")
file_again = input("> ")

# open new fd on given filename and print contents
txt_again = open(file_again)
print(txt_again.read())
txt_again.close()
