import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
NATO_phonetic_dict = {row["letter"]: row["code"] for (index, row) in data.iterrows()}
print(NATO_phonetic_dict)


word = input("Enter a word: ").upper()
output_list = [NATO_phonetic_dict[letter] for letter in word]
print(output_list)
