# 1. Datenbasis
kunden = [
    {"name": "Max", "stadt": "Berlin", "aktiv": True},
    {"name": "Lisa", "stadt": "Hamburg", "aktiv": False},
    {"name": "Tom", "stadt": "Berlin", "aktiv": True}
]

# 2. Funktion zum Anzeigen aller Kunden
def alle_kunden_zeigen(kundenliste):
    print("\n--- Alle Kunden ---")
    for index, kunde in enumerate(kundenliste, start=1):
        status = "aktiv" if kunde["aktiv"] else "inaktiv"
        print(f"{index}. {kunde['name']} ({kunde['stadt']}) - Status: {status}")

# 3. Funktion zum Filtern nach Stadt
def kunden_nach_stadt_filtern(kundenliste, stadt):
    gefundene = []
    for kunde in kundenliste:
        if kunde["stadt"].lower() == stadt.lower():
            gefundene.append(kunde)
    return gefundene  # Gibt die gefundene Teilliste zurück!

# --- Hauptprogramm ---
def main():
    while True:
        print("\n--- MODULARER KUNDEN-MANAGER ---")
        print("1: Alle Kunden anzeigen")
        print("2: Kunden nach Stadt filtern")
        print("3: Programm beenden")
        
        wahl = input("\nWähle eine Option: ")
        
        if wahl == "3":
            print("Programm beendet.")
            break
        elif wahl == "1":
            alle_kunden_zeigen(kunden)
        elif wahl == "2":
            suchstadt = input("Welche Stadt? ")
            ergebnis = kunden_nach_stadt_filtern(kunden, suchstadt)
            
            print(f"\nErgebnisse für '{suchstadt}':")
            if len(ergebnis) == 0:
                print("Keine Kunden gefunden.")
            else:
                for k in ergebnis:
                    print(f"- {k['name']}")
        else:
            print("Ungültige Eingabe.")

# Startpunkt des Skripts
if __name__ == "__main__":
    main()