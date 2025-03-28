#input string
string = input("Input: ")
#split string into words
words = string.split()

#initialize
first = True
new_string = ""

#iterate through each words
for word in words:
    #iterate through each characters
    for character in word:
        #check if first letter
        if character.isalpha() and first:
            #convert to upper if true
            character = character.upper()
            #add to new string
            new_string += character
            first = False

        #else
        else:
            #convert to lower 
            character = character.lower()
            #add to new string
            new_string += character
    #add space to new string
    new_string += " "
    first = True

#print new string
print(f"Output: {new_string}")
