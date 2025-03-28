#import math
import math
#input string
string = input("Input: ")
#input length of string to be returned(max_length)
max_length = input("Max Length of String: ")

#get length of string
string_length = len(string)
#get space filler(max_length - string_length)
filler = max_length - string_length
#get half of filler(ceiling)
half_filler = math.ceil(filler / 2)

#fill beginning of string with zero
#fill end of string with zero
#print string