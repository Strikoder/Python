# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

letters = []

with open("Input/Letters/starting_letter.txt", mode="r") as file:
    letter = file.read()

with open("Input/Names/invited_names.txt", mode="r") as file:
    names = file.read()
    invited_names = names.split()

for name in invited_names:
    letters.append(letter.replace("[name]", f"{name}"))

results = ''.join(map(str, letters)).split("\n\n\n")

results.pop()

for index, message in enumerate(results):
    with open(f"Output/ReadyToSend/ready_to_send_to{invited_names[index]}", mode='w') as file:
        file.write(str(message))


