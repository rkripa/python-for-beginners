# Save this file as eof.py
# Run from Cmd or terminal window as:
# python eof.py
# 

print("** Input EOFError demo **")

string = input("Enter numbers or string: ")
print("Input Entered:", string)

print("** When input() read ctrl-z or ctrl-d, it raises EOFError **")
eof = input("Enter ctrl-z or ctrl-d: ")
