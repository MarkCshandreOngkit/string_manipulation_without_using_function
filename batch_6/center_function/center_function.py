#import math
import math
#input string
string = input("Input: ")
#input length of string to be returned(max_length)
max_length = int(input("Max Length of String: "))

#get length of string
string_length = len(string)
#get space filler(max_length - string_length)
filler = max_length - string_length
#get half of filler(ceiling)
half_filler = math.ceil(filler / 2)

#fill beginning of string with " "
beginning_filler = " " * half_filler
string = beginning_filler + string

#fill end of string with " "
end_filler = " " * (filler - half_filler)
string = string + end_filler

#print string
print(string)