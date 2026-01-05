# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

import pandas
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

#need to read the csv and create a dataframa

alphabet_dataframe = pandas.read_csv("nato_phonetic_alphabet.csv")

for (index, row) in alphabet_dataframe.iterrows():
    nato_dict = {row.letter: row.code for (index, row) in alphabet_dataframe.iterrows()}


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

#so we'll make a function for this one using our dictionary

def words_to_phonetic(user_string, phonetic_dictionary):
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    user_string_clean_1 = user_string.upper().replace(" ", "")
    user_string_clean = [letter for letter in user_string_clean_1 if letter in alphabet]
    string_to_convert = [letter for letter in user_string_clean]
    phonetic_output = [phonetic_dictionary[i] for i in string_to_convert if phonetic_dictionary[i]  ]
    return phonetic_output


user_string = input("Type a word or sentence: ")
print(words_to_phonetic(user_string, nato_dict))

