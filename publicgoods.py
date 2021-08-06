from dataclasses import dataclass
import random
import time


@dataclass
class AIPlayer():
    PLnumber: int
    PLwallet: float
    PLtype: str
    PLstrategy: float 



types = ["naive", "average", "selfish"]

def contributioncheck(contribution,endowment):
    return contribution < 0 or contribution > endowment

def payoutcalc(contribution):
    conTotal = sum(contribution)
    payout = (conTotal*2)/len(playerlist)
    return payout

def strategycalc(strategy,type,reference):
    if type == "naive":
        return (strategy + reference)/2
    elif type == "average":
        return reference
    else:
        return 0.8*reference


def round(endowment):      
    print(f"Du und deine Mitspieler wurden mit jeweils {endowment} Geldeinheiten ausgestattet.")
    time.sleep(0.5)
    while True:
        PLcontribution = input(f"Bitte gib' den Betrag an, den du von deiner Ausstattung dieser Runde zum öffentlichen Gut beitragen möchtest:  ")
        try:
            PLcontribution = float(PLcontribution)
        except ValueError:
            print(f"Invalide Eingabe, bitte gib' eine Dezimalzahl im Format 1.23 an.")
            continue
        if contributioncheck(PLcontribution,endowment):
            print(f"Deine Eingabe ist invalide, weil sie negativ ist, oder über deinem Rundeneinkommen liegt.")
            continue
        print(f"Du hast erfolgreich {PLcontribution} beigetragen!")
        realplayer.PLstrategy = PLcontribution
        break
    time.sleep(0.5)
    contributions = [f.PLstrategy for f in playerlist]
    avgcontri = sum(contributions)/len(contributions)
    print(f"Die Beiträge aller Spieler sind {contributions}.")
    time.sleep(0.5)
    payout = payoutcalc(contributions)
    print(f"Dadurch beträgt die Auszahlung {payout} Geldeinheiten pro Spieler.")
    
    time.sleep(0.5)
    realplayer.PLwallet += endowment - realplayer.PLstrategy + payout
    p2.PLwallet += endowment - p2.PLstrategy + payout
    p3.PLwallet += endowment - p3.PLstrategy + payout
    p4.PLwallet += endowment - p4.PLstrategy + payout
    print(f"Dein neuer Kontostand beträgt {realplayer.PLwallet}. Die deiner Mitspieler (p2,p3,p4) {p2.PLwallet}, {p3.PLwallet}, {p4.PLwallet}")

    time.sleep(0.5)
    p2.PLstrategy = strategycalc(p2.PLstrategy, p2.PLtype, avgcontri)
    p3.PLstrategy = strategycalc(p3.PLstrategy, p3.PLtype, avgcontri)
    p4.PLstrategy = strategycalc(p4.PLstrategy, p4.PLtype, avgcontri)
    return avgcontri

runde = 0
endowment = 10
avgcontri = endowment
realplayer = AIPlayer(1, 0, "", 0)
p2 = AIPlayer(2, 0, random.choice(types), random.uniform(endowment, 0.95*endowment))
p3 = AIPlayer(3, 0, random.choice(types), random.uniform(endowment, 0.95*endowment))
p4 = AIPlayer(4, 0, random.choice(types), random.uniform(endowment, 0.95*endowment))

playerlist = [realplayer, p2, p3, p4]

while avgcontri >= 0.45*endowment:
    runde += 1
    print(f"")
    time.sleep(0.5)
    print(f"Starte Runde {runde}...")
    time.sleep(0.5)
    avgcontri = round(endowment)

print("")
time.sleep(0.5)
print(f"Das Spiel wurde beendet, da die durchschnittlichen Beiträge in der letzten Runde {avgcontri} betrugen, was weniger als 45% des Einkommens ({0.45*endowment}GE) entspricht.")
time.sleep(0.5)
print(f"Dein Finaler Kontostand beträgt {realplayer.PLwallet}. Deine Mitspieler (p2,p3,p4) gehen mit {p2.PLwallet}, {p3.PLwallet}, {p4.PLwallet}, nach Hause.")


