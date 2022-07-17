import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
NATO_phonetic_dict = {row["letter"]: row["code"] for (index, row) in data.iterrows()}
print(NATO_phonetic_dict)


def generate():
    word = input("Enter a word: ").upper()
    try:
        output_list = [NATO_phonetic_dict[letter] for letter in word]
    except KeyError as error_msg:
        print(f"Haha, you have entered a valid value, did you parents called you{error_msg} in your childhood?")
        generate()
    else:
        print(output_list)


generate()
