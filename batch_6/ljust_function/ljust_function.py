#input string
string = input("Input: ")
#input length of string to be returned(length_returned)
length_returned = int(input("Max Length of String: "))

#get length of string
string_length = len(string)

#fill beginning of string with "0"
string = string.zfill(length_returned)
#replace "0" with " "
string = string.replace("0", " ", length_returned - string_length)

#print string
print(f"Output:\n>{string}")