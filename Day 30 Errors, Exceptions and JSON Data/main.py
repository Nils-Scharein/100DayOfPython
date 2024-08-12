import pandas
nato = pandas.read_csv("nato_phonetic_alphabet.csv")

#defines
dic = {row["letter"]:row["code"] for (index, row) in nato.iterrows()}


a = True
def generate_phonetic():
    try:
        user_input = input("Please insert a Word for the Nato Alphabet\n")
        result = [dic[letter] for letter in user_input.upper()]
        a = False
    except KeyError:
        print("Pls insert only letters")
        generate_phonetic()
    else:
        print(result)

generate_phonetic()
