import json
from Einnahme import Einnahme

def speichern(haushaltsbuch):
    daten : dict = {
          "einnahmen": [],
          "ausgaben": [],
          "kategorien":[]
    }


    for einnahme in haushaltsbuch.einnahmen:

        eintrag : dict = {
            "betrag": einnahme.betrag,
            "beschreibung": einnahme.beschreibung,
            "kategorie": einnahme.kategorie.bezeichnung
        }
        daten["einnahmen"].append(eintrag)


    for ausgabe in haushaltsbuch.ausgaben:
    
            eintrag : dict = {
                "betrag": ausgabe.betrag,
                "beschreibung": ausgabe.beschreibung,
                "kategorie": ausgabe.kategorie.bezeichnung
            }
            daten["ausgaben"].append(eintrag)


    for kategorie in haushaltsbuch.kategorien:
    
            eintrag : dict = {
                "bezeichnung": kategorie.bezeichnung,
                "budget": kategorie.budget
            }
            daten["kategorien"].append(eintrag)

    with open("haushaltsbuch.json", "w") as file:
        json.dump(daten, file, indent=4, ensure_ascii=False)
