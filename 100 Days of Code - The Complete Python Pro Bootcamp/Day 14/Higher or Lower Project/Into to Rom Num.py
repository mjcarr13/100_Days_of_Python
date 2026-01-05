"""Seven different symbols represent Roman numerals with the following values:

Symbol	Value
I	1
V	5
X	10
L	50
C	100
D	500
M	1000
Roman numerals are formed by appending the conversions of decimal place values from highest to lowest.

Converting a decimal place value into a Roman numeral has the following rules:

If the value does not start with 4 or 9, select the symbol of the maximal value that can be subtracted from the input,
append that symbol to the result, subtract its value, and convert the remainder to a Roman numeral.

If the value starts with 4 or 9 use the subtractive form representing one symbol subtracted from the following symbol,
for example, 4 is 1 (I) less than 5 (V): IV and 9 is 1 (I) less than 10 (X): IX.
Only the following subtractive forms are used: 4 (IV), 9 (IX), 40 (XL), 90 (XC), 400 (CD) and 900 (CM).

Only powers of 10 (I, X, C, M) can be appended consecutively at most 3 times to represent multiples of 10.
You cannot append 5 (V), 50 (L), or 500 (D) multiple times. If you need to append a symbol 4 times use the subtractive form.
Given an integer, convert it to a Roman numeral.

#so we'd want a for loop which reads from right to left and generates a list which we can then use to convert to our numerals. 

-1 = number * 1
-2 = number * 10
-3 = number * 100
-4 = number * 1000

so let's say the number is 1994

indexing our numbers are 
-1 = 4
-2 = 9
-3 = 9
-4 = 1

and using he above formula we'd get

-1 = 4
-2 = 90
-3 = 900
-4 = 1000

we'd then want to add those to a list, adding each one to the front of the list one by one

[1000, 900, 90, 4)

we then need to convert these numbers into the roman numerals. We could just throw together a comprehensive dictionary

into_to_num_dict = {
    1: "I", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI", 7: "VII", 8: "VIII", 9: "IX", 10: "X", 20: "XX", 30: "XXX",
    40: "XL", 50: "L", 60: "LX", 70: "LXX", 80: "LXX", 90: "XC", 100: "C", 200: "CC", 300: "CCC", 400: "CD", 500: "D",
    600: "DC", 700: "DCC", 800: "DCCC", 900: "CM", 1000: "M", 2000: "MM", 3000: "MMM",
}

[1000, 900, 90, 4)
should thus become

year = [into_to_num_dict[1000]+into_to_num_dict[900]+into_to_num_dict[90]+into_to_num_dict[4]]
print(year)
#cool, proof of concept above seems to work, let's get coding.

#so we'd want a for loop which reads from right to left and generates a list which we can then use to convert to our numerals.
"""


def integer_to_dec_values(number):
    iterable_num = list(map(int, str(number)))
    for index, element in enumerate(iterable_num):
        index = index - len(iterable_num)
        if index == -2:
            iterable_num[-2] = element * 10
        elif index == -3:
            iterable_num[-3] = element* 100
        elif index == -4:
            iterable_num[-4] = element * 1000
    return iterable_num


into_to_num_dict = {
        1: "I", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI", 7: "VII", 8: "VIII", 9: "IX", 10: "X", 20: "XX", 30: "XXX",
        40: "XL", 50: "L", 60: "LX", 70: "LXX", 80: "LXX", 90: "XC", 100: "C", 200: "CC", 300: "CCC", 400: "CD", 500: "D",
        600: "DC", 700: "DCC", 800: "DCCC", 900: "CM", 1000: "M", 2000: "MM", 3000: "MMM",
    }

def int_to_rom(number_to_convert):
    list_to_convert = integer_to_dec_values(number_to_convert)
    year = ""
    for i in list_to_convert:
        if i != 0:
            year += str(into_to_num_dict[i])
    return year


print(int_to_rom(2005))
