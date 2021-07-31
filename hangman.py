import random

def pruefung(word, letter, rletters, fletters, hangman):
    if letter in word and letter not in rletters:
        print (f"'{letter}' ist ein richtiger Buchstabe. Hangman: {hangman}" )
        rletters += letter
    elif letter in rletters or letter in fletters:
        print (f"Du hast den Buchstaben '{letter}' schon eingegeben, versuche es erneut")
    else:
        hangman = hangman + 1
        print(f"'{letter}' ist ein falscher Buchstabe! +1 Hangman: {hangman}")
        fletters += letter
    return hangman, 12

def main():
    print("Hello World")
    hangman = 0
    words = ["kuh", "hund", "katze", "pferd"]
    word = random.choice(words)
    wordarr = list(word)
    print(wordarr)
    rlets = len(word)
    rletters = []
    fletters = []

    while rlets > len(rletters):
        letter =  input("Gib bitte einen Buchstaben ein:     ").lower()
        print(letter)
        hangman, i = pruefung(word, letter, rletters, fletters, hangman)


    print(f"Du hast alle Buchstaben richtig erraten! Dein Wort war '{word}'! Du hast insgesamt {hangman} Fehler gemacht")

if __name__ == "__main__":
    main()
