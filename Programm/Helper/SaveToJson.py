import json

def speichern(haushaltsbuch):
    daten = []

    for buchung in haushaltsbuch.buchungen:
        eintrag : dict = {
            "betrag": buchung.betrag,
            "beschreibung": buchung.beschreibung,
            "kategorie": buchung.kategorie.bezeichnung
        }
        daten.append(eintrag)

    with open("haushaltsbuch.json", "w") as file:
        json.dump(daten, file)
