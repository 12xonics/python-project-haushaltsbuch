

from Kategorie import Kategorie
from Einnahme import Einnahme

import json

def laden(haushaltsbuch):

    for eintrag in daten:
        betrag = eintrag ["betrag"]
        beschreibung = eintrag ["beschreibung"]
        kategorie = eintrag ["kategorie"]
        haushaltsbuch.buchungen.append(Einnahme)

    with open("haushaltsbuch.json", "r") as file:
    daten = json.load(file) #wird als dict geladen
    print(json_anzeigen) 
    