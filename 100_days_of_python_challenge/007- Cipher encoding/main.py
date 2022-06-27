from art import logo
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(input_text, shift_amount, encoding_type):
    output = ""
    if encoding_type == "decode":
        shift_amount *= -1
    elif encoding_type != "decode" and encoding_type !="encode":
        print("You have entered an invalid type of encoding")
        return

    for char in input_text:
        if char in alphabets:
            position = alphabets.index(char)
            new_position = position + shift_amount
            output += alphabets[new_position]
        else:
            output += char

    print(f"Here's the {encoding_type}d result: {output}")


print(logo)
finished = False
while not finished:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    caesar(input_text=text, shift_amount=shift, encoding_type=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        finished = True
        print("Cya")



