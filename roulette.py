import random
import time

balance = 100.00

def roll():
    winnumber = random.randrange(0,14,1)
    return winnumber

def balcheck(balance,bet):
    return balance < bet or bet < 0
  
def multipl(num):
    if num == "NULL":
        multiplikator = 14
    else:
        multiplikator = 2
    return multiplikator

def betting(nummerart, balance):
    multiplikator = multipl(nummerart)
    while True:
        bet0 = input(f"Gib deine Wette für {nummerart} ab (x{multiplikator})! (Verfügbare Balance: '{balance}')")
        time.sleep(1)
        try:
            bet0 = float(bet0)
        except ValueError:
            print(f"'{bet0}' ist eine invalide Eingabe: Bitte gib eine Nummer im Format EEE.cc ein!")
            continue
        if balcheck(balance, bet0):
            print(f"Deine Wette von '{bet0}' übersteigt deine verfügbare Balance von '{balance}' oder ist negativ! Versuche es bitte erneut:" )
            continue
        balance = balance - bet0
        time.sleep(1)
        print(f"'{bet0}' wurde erfolgreich auf {nummerart} gesetzt!")
        break
    return bet0, balance

betN, balance = betting("NULL", balance)
time.sleep(1)
betE, balance = betting("GERADE", balance)
time.sleep(1)
betO, balance = betting("UNGERADE", balance)
time.sleep(1)


number = roll()
print(number)
time.sleep(1)

if (number%2) == 0 and number != 0:
    print(f"{number} ist gerade!")
    time.sleep(1)
    win = betE * 2
    print(f"Du hast {win} gewonnen!")
    time.sleep(1)
    balance = balance + win
    print(f"Deine neue Balance beträgt nun {balance}!")
    time.sleep(1)

elif (number%2) != 0 and number != 0:
    print(f"{number} ist ungerade!")
    time.sleep(1)
    win = betO * 2
    print(f"Du hast {win} gewonnen!")
    time.sleep(1)
    balance = balance + win
    print(f"Deine neue Balance beträgt nun {balance}!")
    time.sleep(1)

else:
    print("Die Nummer ist 0!")
    time.sleep(1)
    win = betN * 14
    print(f"Du hast {win} gewonnen!")
    time.sleep(1)
    balance = balance + win
    print(f"Deine neue Balance beträgt nun {balance}!")
    time.sleep(1)