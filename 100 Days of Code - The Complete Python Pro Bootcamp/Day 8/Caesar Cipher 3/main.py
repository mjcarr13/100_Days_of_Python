import art
print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(original_text, shift_amount, encode_or_decode):
    if encode_or_decode == decode



def caesar(original_text, shift_amount, encode_or_decode):
    if encode_or_decode == "decode":
        output_list = []
        for letter in original_text:
            if letter in alphabet:
                i = alphabet.index(letter)
                output_list.append(alphabet[(i + shift_amount) % 26])
            else:
                output_list.append(letter)
        encoded_string = "".join(output_list)
        print(f"Your encoded message is: {encoded_string}.")
        use_again = input("Type 'yes' if you want to go again. Otherwise, type 'no'.").lower()
        if use_again == "yes":
            direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
            text = input("Type your message:\n").lower()
            shift = int(input("Type the shift number:\n"))
            caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
        else:
            print("So long then!")
    elif encode_or_decode == "decode":
        decrypted_list = []
        for letter in original_text:
            if letter in alphabet:
                i = alphabet.index(letter)
                decrypted_list.append(alphabet[(i - shift_amount) % 26])
            else:
                decrypted_list.append(letter)
        decrypted_string = "".join(decrypted_list)
        print(f"Your decoded message is: {decrypted_string}.")
        use_again = input("Type 'yes' if you want to go again. Otherwise, type 'no'.").lower()
        if use_again == "yes":
            direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
            text = input("Type your message:\n").lower()
            shift = int(input("Type the shift number:\n"))
            caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
        else:
            print("So long then!")


caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

