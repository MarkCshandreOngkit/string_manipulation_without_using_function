#input string
string = input("Input: ")
#input end_string
end_string = input("Check if ending in: ")
#find end_string in string
position = string.rfind(end_string)
print(position)
#if endstring not in string
    #print False
#if endstring in string but not in end
    #print False
#if endstring in string in end position
    #print True