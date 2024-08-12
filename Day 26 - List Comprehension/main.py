import pandas
nato = pandas.read_csv("nato_phonetic_alphabet.csv")

dic = {row["letter"]:row["code"] for (index, row) in nato.iterrows()}
user_input = input("Please insert a Word for the Nato Alphabet")
result = [dic[letter] for letter in user_input.upper()]

print(result)

