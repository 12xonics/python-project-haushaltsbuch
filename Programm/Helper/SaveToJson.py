import json
from Einnahme import Einnahme

def speichern(haushaltsbuch):
    daten = []

    for buchung in haushaltsbuch.buchungen:
        if isinstance(buchung, Einnahme):
            typ = "Einnahme"
        else:
            typ = "Ausgabe"  

        eintrag : dict = {
            "betrag": buchung.betrag,
            "beschreibung": buchung.beschreibung,
            "kategorie": buchung.kategorie.bezeichnung,
            "typ" : typ
        }
        daten.append(eintrag)

    with open("haushaltsbuch.json", "w") as file:
        json.dump(daten, file, indent=4, ensure_ascii=False)
