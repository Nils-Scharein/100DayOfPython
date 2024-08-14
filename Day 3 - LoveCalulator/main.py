name1 = "Angela Yu"
name2 = "Jack Bauer"
word1 = "Love"
word2 = "True"

def loveCalculator(name, word1, word2):
    array1 = list(word1)
    array2 = list(word2)
    counter1 = 0
    counter2 = 0

    for letter in name:
        if letter in array1:
            counter1 += 1
        if letter in array2:
            counter2 += 1

    erg = counter1 + counter2
    return erg

def checker(count):
    if count < 10 or count > 90:
        print(f"Your score is {count}, you go together like coke and mentos.")
    elif count > 40 and count < 50:
        print(f"Your score is {count}, you are alright together.")
    else:
        print(f"Your score is {count}")

score1 = loveCalculator(name1, word1, word2)
score2 = loveCalculator(name2, word1, word2)

combined_score = int(f"{score1}{score2}")

checker(combined_score)