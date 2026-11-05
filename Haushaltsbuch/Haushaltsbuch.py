from Kategorie import Kategorie
from Buchung import Buchung
from Ausgabe import Ausgabe
from Einnahme import Einnahme
from UIManager import UIManager

class Haushaltsbuch:
    def __init__(self):
        self.buchungen: list[Buchung] = []
        self.kontostand: float = 0

    def haushaltsbuch_starten(self):
        """Läd bei vorhandener JSON die Daten in den Speicher oder legt die JSON Speicherdatei initial an."""


    def ausgabe_buchen():
        pass

    def einnahme_buchen():
        pass

    def berechne_kontostand():
        pass

    def monatsbericht_ausgeben():
        pass

    def budget_setzen(kategorie: Kategorie):
        pass