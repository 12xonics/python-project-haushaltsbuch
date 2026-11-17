import json
from Einnahme import Einnahme

def speichern(haushaltsbuch):
    daten : dict = {}

    for einnahme in haushaltsbuch.einnahmen:

        eintrag : dict = {
            "betrag": einnahme.betrag,
            "beschreibung": einnahme.beschreibung,
            "kategorie": einnahme.kategorie.bezeichnung
        }
        daten["einnahmen"].append(eintrag)



    

    with open("haushaltsbuch.json", "w") as file:
        json.dump(daten, file, indent=4, ensure_ascii=False)
