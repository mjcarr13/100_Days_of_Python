# Exception Handling

try:
    file = open("a_file.txt")                # Attempt to open an existing file named "a_file.txt"
    a_dictionary = {"key": "value"}          # Create a simple dictionary with one key/value pair
    print(a_dictionary["key"])               # Try to access the value at key "key"
except FileNotFoundError:                    # This block runs if opening the file fails because it doesn't exist
    file = open("a_file.txt", "w")           # Create the file instead (write mode)
    file.write("Something")                  # Write placeholder text into the new file
except KeyError as error_message:            # This block runs if the dictionary lookup fails (missing key)
    print(f"The key {error_message} does not exist.")  # Report the missing key using the caught error
else:
    content = file.read()                    # Runs only if no exceptions occurred in the try block
    print(content)                           # Print the file contents
finally:
    raise TypeError("This is an error that I made up.")  # Always runs; deliberately raises a custom error


#BMI Example

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human Height should not be over 3 meters.")

bmi = weight / height ** 2
print(bmi)














