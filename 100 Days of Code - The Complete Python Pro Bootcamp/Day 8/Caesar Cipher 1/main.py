alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
original_text = input("Type your message:\n").lower()
shift_amount = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.

def encrypt(original_text, shift_amount):
    output_list = []
    for letter in original_text:
        if letter in alphabet:
            i = alphabet.index(letter)
            output_list.append(alphabet[i+shift_amount % 26])
        else:
            output_list.append(letter)
    encoded_string = "".join(output_list)
    print(f"Your encoded message is: {encoded_string}.")


encrypt(original_text = original_text, shift_amount= shift_amount)

