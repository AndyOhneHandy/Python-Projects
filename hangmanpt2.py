import random


def pruefung(word, letter, rletters, fletters, nhang):
    if letter in word and letter not in rletters:
        print (f"'{letter}' ist ein richtiger Buchstabe." )
        rletters += letter
        wort(letter)
        hangfkt(nhang)
    elif letter in rletters or letter in fletters:
        print (f"Du hast den Buchstaben '{letter}' schon eingegeben, versuche es erneut")
        hangfkt(nhang)
    else:
        nhang = nhang + 1
        print(f"'{letter}' ist ein falscher Buchstabe!")
        fletters += letter
        hangfkt(nhang)
    return nhang

def wort(letter):
    for i,c in enumerate(wordlist):
        if c == letter:
            wordlistminus[i] = letter
            print(f"Du hast einen Buchstaben an Position {i + 1} gefunden")
            print(wordlistminus)

nhang = 0
hangman = list("hangman")
hangmanminus = list("_______")
finalhang =  " ".join(hangman[0:nhang] + hangmanminus[0:-nhang])
rletters = []
fletters = []
words = ["kuh", "hund", "katze", "pferd", "auerhahn"]
word = random.choice(words)
wordlist = list(word)
wordlistminus = list(len(wordlist)*"_")
print(wordlistminus)

def hangfkt(nhang):
    hangman = list("hangman")
    hangmanminus = list("_______")
    finalhang =  " ".join(hangman[0:nhang] + hangmanminus[0:-nhang])
    print(finalhang,)
    return finalhang

while wordlist != wordlistminus and finalhang != " ".join(hangman):
    letter =  input("Gib bitte einen Buchstaben ein:     ").lower()
    print(letter)
    nhang = pruefung(word, letter, rletters, fletters, nhang)



