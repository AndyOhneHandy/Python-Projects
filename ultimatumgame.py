from dataclasses import dataclass
import random
import time
import numpy

@dataclass
class AIPlayer():
    PLbeht: str
    PLinct: str
    PLinc: int
    PLsplit: int
    PLaccept: float

behaviourtype = ["homooec", "fair", "unfair", "selfish", "altruistic"]
iR = ["rich"]
iA = ["average"]*5
iP = ["poor"]*3
incometype = iR + iA + iP




def avginccheck(input):
    return input <= 0

def splitamountcheck(input, endowment):
    return input <= 0 or input > endowment

def playerinputcheck(input):
    return input != "ja" and input != "nein"

def gamemodeinputcheck(input):
    return input != "split" and input != "accept"

def checkoutcome(splitvalue, acceptvalue):
    if splitvalue >= acceptvalue:
        return 1
    if splitvalue < acceptvalue:
        return 0


def incomecalc(inctype, avginc):
    if inctype == "rich":
        return 2*avginc + abs(round(numpy.random.normal(0, 0.5*avginc),0))
    elif inctype == "average":
        return abs(round(numpy.random.normal(avginc, 0.1*avginc),0))
    else:
        return abs(round(numpy.random.normal(0.5*avginc, 0.05*avginc),0))
1
def thresholdcalc(inc, behtype, endowment, avginc):
    if behtype == "homooec":
        return 0
    elif behtype == "altruistic":
        return min([0.1*inc, 0.2*endowment, 0.1*avginc])
    elif behtype == "fair" or behtype == "unfair":
        return min([0.2*inc, 0.4*endowment, 0.4*avginc])
    elif behtype == "selfish":
        return min([0.4*inc, 0.7*endowment, 0.8*avginc])
    else:
        return 0.5*endowment

def splitcalc(inc, behtype, endowment):
    if behtype == "homooec":
        return 0.4*endowment
    elif behtype == "fair":
        return min([0.5*endowment, 0.3*inc])
    elif behtype == "unfair":
        return min([0.3*endowment, 0.2*inc])
    elif behtype == "selfish":
        return 0.1*endowment
    elif behtype == "altruistic":
        return min([0.7*endowment, 0.5*inc])
    else:
        return 0.5*endowment

print(f"An einem Ultimatum-Spiel nehmen zwei Spieler teil. Ein Spieler wird mit einem gewissen Budget ausgestattet.")
time.sleep(0.5)
print(f"Dieser Spieler kann nun entscheiden wie viel er von seiner Ausstattung an den zweiten Spieler abtreten möchte.")
time.sleep(0.5)
print(f"Der zweite Spieler kann dieses Angebot entweder akzeptieren, wobei er den angebotenen Betrag und sein Mitspieler den Rest als Auszahlung erhalten...")
time.sleep(0.5)
print(f"...oder das Angebot ablehnen, wobei keiner der beiden Spieler eine Auszahlung erhält.") 
time.sleep(0.5)
print(f"Als Referenz für den AI-Mitspieler muss im folgenden ein Durchschnittseinkommen angegeben werden.")



while True:
    time.sleep(0.5)
    avginc = input("Bitte gib ein Durchschnittseinkommen an (positive, ganze Zahl):   ")
    time.sleep(0.5)
    try:
        avginc = int(avginc)
    except ValueError:
        print(f"{avginc} ist eine invalide Eingabe - bitte gib eine ganze Zahl an...")
        continue
    if avginccheck(avginc):
        print(f"Deine Eingabe ({avginc}) ist invalide, weil sie negativ ist. Versuche es bitte erneut...")
        continue
    print(f"{avginc} wurde erfolgreich als Durchschnittseinkommen festgelegt.")
    break

endowment = abs(round(numpy.random.normal(0.3*avginc, 0.05*avginc),0))
AIopponent = AIPlayer(random.choice(behaviourtype), random.choice(incometype), 0, 0, 0)
AIopponent.PLinc = incomecalc(AIopponent.PLinct, avginc)
AIopponent.PLaccept = thresholdcalc(AIopponent.PLinc, AIopponent.PLbeht, endowment, avginc)
AIopponent.PLsplit = splitcalc(AIopponent.PLinc, AIopponent.PLbeht, endowment)


def PlayerAccept(endowment):
    while True:
        time.sleep(0.5)
        playerinput = input(f"Dein Mitspieler bietet dir an, {AIopponent.PLsplit} von seiner Austattung ({endowment}) abzugeben. Schreibe 'ja' um dieses Angebot zu akzeptieren oder 'nein' um es abzulehnen:   ")
        time.sleep(0.5)
        if playerinputcheck(playerinput.lower()):
            print(f"Deine Eingabe ({playerinput}) ist nicht 'ja' oder 'nein'. Versuche es bitte erneut.")         
            continue
        print(f"Du hast erfolgreich auf das Angebot von deinem Mitspieler ({AIopponent.PLsplit} von {endowment}) mit {playerinput} reagiert")
        break
    time.sleep(0.5)
    if playerinput.lower() == "ja":
        acceptamount = AIopponent.PLsplit - 1
    elif playerinput.lower() == "nein":
        acceptamount = AIopponent.PLsplit + 1
    p = checkoutcome(AIopponent.PLsplit, acceptamount)
    if p == 1:
        print(f"Du hast das Angebot deines Mitspielers akzeptiert.")
        playerPurse = AIopponent.PLsplit
        AIPurse = endowment - AIopponent.PLsplit
    else:
        print(f"Du hast das Angebot deines Mitspielers nicht akzeptiert.")
        playerPurse = 0
        AIPurse = 0    
    return playerPurse, AIPurse

def PlayerSplit(endowment):
    while True:
        time.sleep(0.5)
        splitamount = input(f"Du wurdest mit {endowment} ausgestattet. Gib den Betrag an, den du davon an deinen Mitspieler abtreten möchtest (positive, ganze Zahl):   ")
        time.sleep(0.5)
        try:
            splitamount = int(splitamount)
        except ValueError:
            print(f"{splitamount} ist eine invalide Eingabe - bitte gib eine ganze Zahl an...")
            continue
        if splitamountcheck(splitamount, endowment):
            print(f"Deine Eingabe ({splitamount}) ist negativ oder größer als deine Ausstattung - versuche es bitte erneut...")         
            continue
        print(f"Du hast erfolgreich das Angebot gemacht, {splitamount} von deiner Ausstattung von {endowment} an deinen Mitspieler abzutreten.")
        break
    time.sleep(0.5)    
    p = checkoutcome(splitamount, AIopponent.PLaccept)
    if p == 1:
        print(f"Dein Mitspieler hat dein Angebot akzeptiert.")
        playerPurse = endowment - splitamount
        AIPurse = splitamount
    else:
        print(f"Dein Mitspieler hat dein Angebot nicht akzeptiert.")
        playerPurse = 0
        AIPurse = 0
    return playerPurse, AIPurse

time.sleep(0.5)
print(f"In dieser Runde wird der Spieler, der das Angebot macht, mit {endowment} ausgestattet.")
time.sleep(0.5)
print("Wähle jetzt bitte aus, ob du in dieser Runde ein Split-Angebot machen möchtest, oder ein Angebot deines Mitspielers annehmen bzw. ablehnen möchtest.")
while True:
    time.sleep(0.5)
    playergamemode = input("Um ein Split-Angebot zu machen gib bitte 'split' ein, um über das Angebot deines Mitspielers zu entscheiden 'accept':   ")
    time.sleep(0.5)
    if gamemodeinputcheck(playergamemode.lower()):
        print(f"Deine Eingabe ({playergamemode}) ist nicht valide. Bitte versuche es erneut...")
        continue
    break
if playergamemode.lower() == "split":
    time.sleep(0.5)
    print(f"Starte Runde, in der du über den Betrag entscheidest, den du abtrittst...")
    PLoutcome, AIoutcome = PlayerSplit(endowment)
elif playergamemode.lower() == "accept":
    time.sleep(0.5)
    print(f"Starte Runde, in der du entscheidest, ob du das Angebot deines Mitspielers annimmst oder nicht...")
    PLoutcome, AIoutcome = PlayerAccept(endowment)
else:
    print("Fehler")
    PLoutcome = 0
    AIoutcome = 0

time.sleep(0.5)
print(f"Die Runde wurde beendet. Deine Auszahlung beträgt {PLoutcome}, während dein Mitspieler {AIoutcome} erhält.")
time.sleep(0.5)
print(f"Informationen über den AI-Mitspieler: {AIopponent}")