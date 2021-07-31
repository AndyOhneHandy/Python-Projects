import time

def split(mail):
    for i,c in enumerate(mail):
        if c == "@":
            name = "".join(mail[0:i])
            domain = "".join(mail[(i+1):len(mail)])
    return name,domain 

def mailcheck(mail):
    return " " in mail or "@" not in mail or "."not in mail

while True:    
    maileingabe = input("Bitte geben Sie die Email Adresse an, die sie spalten möchten:")
    if mailcheck(maileingabe):
        print(f"Ihre eingegebene Email Adresse ('{maileingabe}') ist nicht valide")
        continue
    print("Ihre Eingabe wurde akzeptiert. Email wird aufgespalten...")
    break

mail = list(maileingabe)
name1,domain1 = split(mail)
time.sleep(1)
print(f"Die Email-Adresse '{maileingabe}' wurde erfolgreich gespalten:")
print(f"    Der Email-Benutzername lautet:       '{name1}'.")
print(f"    Der Email-Provider ist:              '{domain1}'.")
