#input string
string = input("Input: ")
#input prefix to be remove if in the beginning of string
prefix = input("Prefix to be remove: ")
#check if string starts with prefix
if string.startswith(prefix):
    #replace prefix with "" 1 time
    string = string.replace(prefix, "", 1)
#print string
print(string)