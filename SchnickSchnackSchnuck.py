from dataclasses import dataclass
import random
import time

@dataclass
class Figur():
    name: str
    id: int
    win: list
    loss: list
    def nameid(self):
        return f"{self.name} oder {self.id}"

schere = Figur("schere", 0, [2,3], [1,4])
stein = Figur("stein", 1, [0,3], [2,4])
papier = Figur("papier", 2, [1,4], [0,3])
echse = Figur("echse", 3, [2,4], [0,1])
spock = Figur("spock", 4, [0,1], [2,3])

figlist = [schere, stein, papier, echse, spock]
# figlist = [
#     Figur(),
#     Figur()
# ]

# namelist = list(map(lambda f: f.figname, figlist))
namelist = [f.name for f in figlist]
idlist = [f.id for f in figlist]



def inputcheck(figplayer, figlist):
    return figplayer not in [f.name for f in figlist] and figplayer not in [str(f.id) for f in figlist]

def roundcheck(rounds):
    return isinstance(rounds)

def wincheck(fig, gegnerplay):
    return fig.id in gegnerplay.loss

def tiecheck(fig, gegnerplay):
    return fig.id == gegnerplay.id

def round():   
    gegnerplay = random.choice(figlist)

    while True:
        figplayer = input(f"Gib deine Figur ein: { '; '.join((f.nameid() for f in figlist))}:       ")
        if inputcheck(figplayer, figlist):
            print (f"Deine Eingabe ('{figplayer}') ist leider nicht valide. Versuche es erneut... ")
            continue
        fig = next((f for f in figlist if figplayer == f.name or figplayer == str(f.id)), None)
        print(f"Du hast erfolgreich {fig.name} eingeloggt!")    
        break

    time.sleep(0.5)
    print("Schere...")
    time.sleep(0.5)
    print("     Stein...")
    time.sleep(0.5)
    print("         Papier...")
    time.sleep(0.5)
    print("             Echse...")
    time.sleep(0.5)
    print("                 Spock...")
    time.sleep(1)
    print(f"Dein Gegner hat {gegnerplay.name} gespielt.")

    time.sleep(1)

    if wincheck(fig, gegnerplay):
        print(f"Wow, was für ein Kampf: {fig.name} besiegt {gegnerplay.name}! Du hast diese Runde gewonnen!")
        return 2
    else:
        if tiecheck(fig, gegnerplay):
            print(f"Das gibt es doch nicht: {fig.name} und {gegnerplay.name} trennen sich unentschieden!")
            return 1
        else:
            print(f"Och Menno: {gegnerplay.name} besiegt {fig.name}! Du hast diese Runde leider verloren... yIkEs")
            return 0


while True:
    rounds = input(f"Gib die Anzahl an Rundensiegen ein, die für den Gesamtsieg benötigt werden:    ")
    try:
        rounds = abs(int(rounds))
    except ValueError:
        print(f"'{rounds}' ist eine invalide Eingabe: Bitte gib eine positive Ganze Zahl an!")
        continue 
    time.sleep(0.5)
    print(f"Du hast erfolgreich {rounds} Rundensiege bis zum Gesamtsieg eingestellt!")
    break

winplayer = 0
wingegner = 0
ties = 0
runde = 0

time.sleep(0.5)
print("")
while winplayer < rounds and wingegner < rounds:
    runde = runde + 1
    print(f"Starte Runde {runde} :")
    time.sleep(1)
    output = round()
    time.sleep(1)
    if output == 2:
        winplayer = winplayer + 1
        print(f"Damit erhältst Du einen Punkt und der neue Punktestand entspricht: {winplayer}:{wingegner} (Du:Gegner) [Unentschieden: {ties} ]")
    elif output == 1:
        ties = ties + 1
        print(f"Damit bleibt es bei einem Punktestand von {winplayer}:{wingegner} (Du:Gegner) [--> +1 Unentschieden: {ties} ]")
    else:
        wingegner = wingegner + 1
        print(f"Damit erhält dein Gegner einen Punkt und der neue Punktestand entspricht: {winplayer}:{wingegner} (Du:Gegner) [Unentschieden: {ties} ]")
    time.sleep(2)
    print("")

if winplayer == rounds:
    print(f"Gut gemacht, du hast deinen Gegner mit einem Endstand von {winplayer}:{wingegner} nach {runde} Runden besiegt.")
else:    
    print(f"Schade: Leider konntest du deinen Gegner nicht besiegen. Der Endstand nach {runde} Runden ist {winplayer}:{wingegner} . ")
