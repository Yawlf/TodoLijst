import os

taken = []

def toon_taken():
    if taken:
        print("\nTo-Do Lijst")
        for i, taak in enumerate(taken, start=1):
            print(f"{i}. {taak}")
        print()
    else:
        print("\nNog geen taken toegevoegd. Voeg eerst een taak toe!\n")

def voeg_taak_toe():
    nieuwe_taak = input("Voer de taak in die je wilt toevoegen: ").strip()
    if nieuwe_taak:
        taken.append(nieuwe_taak)
        print(f"Taak '{nieuwe_taak}' toegevoegd aan je lijst.\n")
    else:
        print("Taak kan niet leeg zijn. Probeer het opnieuw.\n")

def verwijder_taak():
    toon_taken()
    try:
        taak_nummer = int(input("Voer het nummer van de taak in die je wilt verwijderen: "))
        if 1 <= taak_nummer <= len(taken):
            verwijderde_taak = taken.pop(taak_nummer - 1)
            print(f"Taak '{verwijderde_taak}' verwijderd uit je lijst.\n")
        else:
            print("Ongeldig taaknummer. Probeer opnieuw.\n")
    except ValueError:
        print("Voer een geldig nummer in.\n")

def sla_taken_op():
    bestandsnaam = "taken.txt"
    with open(bestandsnaam, "w") as bestand:
        for taak in taken:
            bestand.write(taak + "\n")
    print(f"Taken opgeslagen in '{bestandsnaam}'.\n")

def main():
    print("To-Do Lijst 📝 (#MBO Project #14221)")
    while True:
        print("Kies een optie:")
        print("1. Bekijk taken")
        print("2. Voeg een taak toe")
        print("3. Verwijder een taak")
        print("4. Sla taken op in bestand")
        print("5. Afsluiten")
        
        keuze = input("Voer je keuze in (1-5): ").strip()

        if keuze == '1':
            toon_taken()
        elif keuze == '2':
            voeg_taak_toe()
        elif keuze == '3':
            verwijder_taak()
        elif keuze == '4':
            sla_taken_op()
        elif keuze == '5':
            print("\nTot ziens!\n")
            break
        else:
            print("Ongeldige keuze. Voer een nummer in tussen 1 en 5.\n")

main()
