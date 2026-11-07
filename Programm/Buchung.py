from datetime import date
from Kategorie import Kategorie

class Buchung:
    def __init__(self, betrag: float, kategorie: Kategorie, beschreibung: str = "Keine Beschreibung"):
        self.datum = date
        self.betrag = betrag
        self.kategorie = kategorie
        self.beschreibung = beschreibung

