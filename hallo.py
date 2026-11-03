name = input("Wie hiesst du? ")
geburtsjahr_text = input("In welchem Jahr bist du geboren? ")
geburtsjahr = int(geburtsjahr_text)

alter = 2026 - geburtsjahr

print("Hallo " + name + "! Du wirst dieses Jahr " " str(alter) " " Jahre alt.")

if alter >= 18:
    print("Super, du bist volljährig!")
else:
    print("Du bist noch minderjährig - geniess die Jugend!")
