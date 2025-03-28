#input string
string = input("Input: ")
#input end_string
end_string = input("Check if ending in: ")

#find end_string in string
position = string.rfind(end_string)

#check length of string and end_string(for checking if end string is in the end)
string_length = len(string)
end_string_length = len(end_string)


#check if end_string is in the end of string
if position + end_string_length == string_length:
    #print True
    print("Output: True")
#if not
else:
    #print False
    print("Output: False")