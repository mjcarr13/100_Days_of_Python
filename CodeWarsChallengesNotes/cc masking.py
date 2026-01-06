# return masked string





# my instinct is to take the string, convert it to a list, use splicing to replace the characters up to the
# fourth from last caracter with #, then convert back to a string and return this string

# or we could take the length of the string, create a string of string length-4, then add the last four characters

cc = "263582736582736528"
print (cc[-4:])

num = len(cc) - 4
output_string = ""
for char in range(0, num):
    output_string += "#"
returnable_string = output_string + cc[-4:]
print(returnable_string)
