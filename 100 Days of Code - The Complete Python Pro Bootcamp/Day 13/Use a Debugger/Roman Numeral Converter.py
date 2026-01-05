#Roman Numeral to Integer Converter

def rom_to_int(roman_numeral):
    numeral_dict = {
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
            answer += numeral_dict[numeral]
        else:
            if numeral == "I":
                answer += numeral_dict["I"]
            elif numeral == "V":
                if roman_numeral[index -1] == "I":
                    print(roman_numeral[index -1])
                    answer += numeral_dict["V"] - 2 * numeral_dict["I"]
                else:
                    answer += numeral_dict["V"]
            elif numeral == "X":
                if roman_numeral[index -1] == "I":
                    answer += numeral_dict["X"] - 2 * numeral_dict["I"]
                else:
                    answer += numeral_dict["X"]
            elif numeral == "L":
                if roman_numeral[index -1] == "X":
                    answer += numeral_dict["L"] - 2 * numeral_dict["X"]
                else:
                    answer += numeral_dict["L"]
            elif numeral == "C":
                if roman_numeral[index -1] == "X":
                    answer += numeral_dict["C"] - 2 * numeral_dict["X"]
                else:
                    answer += numeral_dict["C"]
            elif numeral == "D":
                if roman_numeral[index -1] == "C":
                    answer += numeral_dict["D"] - 2 * numeral_dict["C"]
                else:
                    answer += numeral_dict["D"]
            elif numeral == "M":
                if roman_numeral[index -1] == "C":
                    answer += numeral_dict["M"] - 2 * numeral_dict["C"]
                else:
                    answer += numeral_dict["M"]
    return answer

print(rom_to_int("DCCLXXVII"))