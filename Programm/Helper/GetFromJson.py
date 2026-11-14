

from Kategorie import Kategorie
from Einnahme import Einnahme
from Ausgabe import Ausgabe
import json


def laden(haushaltsbuch):

    with open("haushaltsbuch.json", "r") as file:
        daten = json.load(file)


    for eintrag in daten:
        betrag = eintrag ["betrag"]
        beschreibung = eintrag ["beschreibung"]
        kategorie = eintrag ["kategorie"]
        typ = eintrag["typ"]
        kategorie_name = eintrag["kategorie"]
        
        kategorie = None

    for vorhandene_kategorie in haushaltsbuch.kategorien:
        if vorhandene_kategorie.bezeichnung == kategorie_name:
            kategorie = vorhandene_kategorie
            break
    if kategorie is None:
            kategorie = Kategorie(kategorie_name)
            haushaltsbuch.kategorien.append(kategorie)
    
    if typ == "Einnahme":
        einnahme = Einnahme(betrag,kategorie,beschreibung)
        haushaltsbuch.buchungen.append(einnahme)
    else:
        ausgabe = Ausgabe(betrag,kategorie,beschreibung)
        haushaltsbuch.buchungen.append(ausgabe)

    


 