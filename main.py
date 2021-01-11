import pandas

file = pandas.read_csv("nato_phonetic_alphabet.csv")
file_dic = pandas.DataFrame(file)
file_dic2 = {row.letter: row.code for (index, row) in file_dic.iterrows()}

while True:
    inp = input("Enter a word: ")
    try:
        for letter in inp:
            print(f"{letter} for {file_dic2[letter.upper()]}")
        break
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
