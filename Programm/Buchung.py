from datetime import datetime
from Kategorie import Kategorie

class Buchung:
    def __init__(self, betrag: float, kategorie: Kategorie, beschreibung: str = "Keine Beschreibung"):
        self.timestamp = datetime.now()
        self.betrag = betrag
        self.kategorie = kategorie
        self.beschreibung = beschreibung

    def get_datum_formatted(self) -> str:
        return self.timestamp.strftime("%d.%m.%Y")

