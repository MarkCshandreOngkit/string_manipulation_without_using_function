#input string
string = input("Input: ")
#initialize
new_string = ""
#iterate through each character
for character in string:
    #check if character is the first
    if character == string[0]:
        #convert to upper
        character = character.upper()
        #add to new string
        new_string += character
    #else
    else:
        #convert to lower
        character = character.lower()
        #add to new string
        new_string += character
#print output
print(f"Output: {new_string}")