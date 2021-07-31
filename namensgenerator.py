import random

namesur = ["Glubbeldatsch", "Mubblgard", "Schwillmanicus", "Üdelfüdelmass", "Gründelmann", "Bestelmeier", "Schabsigaz", "Schiet", "Shellywelly", "Hillybilly", "Fummelgrotz", "Strawutzke", "Strawinsky", "Globglogabgalab", "Sabserli", "Meuchelpuffer", "McDonald"]
namemid = ["", "", "", "Junior", "Graf von", "von", "van", "de", "Kim", "Sabbel", "Grolli", "Sissi", "Wan", "der"]
namepre = ["Günther", "Roland", "Theophilius", "Pedda", "Schwanzus", "Jabba", "Rotta", "Ziro", "Obi", "Xaver", "Thorsten", "Erich", "Annie", "Sübi", "Sönke", "Sören", "Amigo", "Adalbert", "Jabs", "Legolas", "Gimli", "Frodo", "Sauron", "Gandalf", "Randalf", "Veronika", "Norbert", "Harry", "Hermine", "Ronald"]
names = []

def randomname():
    #for nametemp in names:
    namepretmp = random.choice(namepre)
    namemidtmp = random.choice(namemid)
    namesurtmp = random.choice(namesur)
    if namemidtmp == "":
        nametemp = namepretmp + " " + namesurtmp
    else:
        nametemp = namepretmp + " " + namemidtmp + " " + namesurtmp

    #names = names + nametemp
    return nametemp

name0 = randomname()
height = round(random.uniform(1.40,2.20), 2)
weight = round(height * 100 * (1/2.5) * random.uniform(0.75,1.65), 2)
bmi = round(weight / ((height)*(height)), 1)

print(f"Daten über {name0}:")
print(f"  {name0} ist {height}m groß.")
print(f"  {name0} wiegt {weight}kg.")
print(f"Demnach hat {name0} einen Body-Mass-Index von {bmi}.")


