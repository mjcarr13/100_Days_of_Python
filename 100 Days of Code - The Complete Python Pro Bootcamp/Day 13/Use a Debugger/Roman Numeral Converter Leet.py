#Roman Numeral to Integer Converter

def rom_to_int(roman_numeral):
    numerals_dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }
    answer = 0
    for index, numeral in enumerate(roman_numeral):
        if index == 0:
            answer += numerals_dict[numeral]
        else:
            if numerals_dict[numeral] > numerals_dict[roman_numeral[index-1]]:
                answer += numerals_dict[numeral] - 2 * numerals_dict[roman_numeral[index-1]]
            else:
                answer += numerals_dict[numeral]
    return answer

print(rom_to_int("MCMXCIV"))

