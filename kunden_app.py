# Initialer Datenbestand
kunden = [
    {"name": "Max", "stadt": "Berlin", "aktiv": True},
    {"name": "Lisa", "stadt": "Hamburg", "aktiv": False},
    {"name": "Tom", "stadt": "Berlin", "aktiv": True}
]

# 1. Funktion zum Anzeigen aller Kunden
def alle_kunden_zeigen(kundenliste):
    print("\n--- Alle Kunden ---")
    for index, kunde in enumerate(kundenliste, start=1):
        status = "aktiv" if kunde["aktiv"] else "inaktiv"
        print(f"{index}. {kunde['name']} ({kunde['stadt']}) - Status: {status}")

# 2. Funktion zum Filtern nach Stadt
def kunden_nach_stadt_filtern(kundenliste, stadt):
    gefundene = []
    for kunde in kundenliste:
        if kunde["stadt"].lower() == stadt.lower():
            gefundene.append(kunde)
    return gefundene

# 3. NEU: Funktion zum Hinzufügen eines Kunden
def kunde_hinzufuegen(kundenliste):
    print("\n--- Neuen Kunden anlegen ---")
    name = input("Name des Kunden: ").strip()
    stadt = input("Stadt des Kunden: ").strip().capitalize()
    
    aktiv_eingabe = input("Ist der Kunde aktiv? (j/n): ").strip().lower()
    aktiv = True if aktiv_eingabe == 'j' else False
    
    # Neues Dictionary erstellen
    neuer_kunde = {
        "name": name,
        "stadt": stadt,
        "aktiv": aktiv
    }
    
    # Zur Liste hinzufügen (.append verändert die Liste direkt)
    kundenliste.append(neuer_kunde)
    print(f"Erfolgreich! Kunde '{name}' wurde hinzugefügt.")

# --- Hauptprogramm ---
def main():
    while True:
        print("\n--- MODULARER KUNDEN-MANAGER ---")
        print("1: Alle Kunden anzeigen")
        print("2: Kunden nach Stadt filtern")
        print("3: Neuen Kunden hinzufügen")
        print("4: Programm beenden")
        
        wahl = input("\nWähle eine Option (1-4): ")
        
        if wahl == "4":
            print("Programm wird beendet. Bis zum nächsten Mal!")
            break
        elif wahl == "1":
            alle_kunden_zeigen(kunden)
        elif wahl == "2":
            suchstadt = input("Welche Stadt? ").strip()
            ergebnis = kunden_nach_stadt_filtern(kunden, suchstadt)
            
            print(f"\nErgebnisse für '{suchstadt}':")
            if len(ergebnis) == 0:
                print("Keine Kunden gefunden.")
            else:
                for k in ergebnis:
                    status = "aktiv" if k["aktiv"] else "inaktiv"
                    print(f"- {k['name']} ({status})")
        elif wahl == "3":
            kunde_hinzufuegen(kunden)
        else:
            print("Ungültige Eingabe. Bitte wähle eine Zahl von 1 bis 4.")

# Startpunkt des Skripts
if __name__ == "__main__":
    main()