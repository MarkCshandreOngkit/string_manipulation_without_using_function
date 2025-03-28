#input a string(words, statements, etc.)
string = input("Input: ")

#iterate through each character in the string
for character in string:
    #check if the character is a space character
    if character == " ":
        #replace space with "" and save if true
        string = string.removeprefix(" ")
    #check if the character is false
    else:
        #stop looping
        break
#print output
print(string)
        