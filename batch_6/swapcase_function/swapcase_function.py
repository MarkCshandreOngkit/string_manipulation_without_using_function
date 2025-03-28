#input string
string = input("Input: ")
#initialize
new_string = ""
#iterate through each character
for character in string:
    #check if lower
    if character.islower():
        #convert to upper if true
        character = character.upper()
        #add to new string
        new_string += character
    #if upper
    elif character.isupper():
        #convert to lower if true
        character = character.lower()
        #add to new string
        new_string += character
    #else
    else:
        #add to new string
        new_string += character
#print new string
print(f"Output: {new_string}")