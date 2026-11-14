from datetime import datetime
from Kategorie import Kategorie

class Buchung:
    def __init__(self, betrag: float, kategorie: Kategorie, beschreibung: str = "Keine Beschreibung"):
        self.timestamp: datetime = datetime.now()
        self.betrag: float = betrag
        self.kategorie: Kategorie = kategorie
        self.beschreibung: str = beschreibung

    def __str__(self):
        return f"{self.get_datum_formatted()} / {self.betrag:.2f}€ / {self.kategorie.bezeichnung} / {self.beschreibung}"

    def get_datum_formatted(self) -> str:
        return self.timestamp.strftime("%d.%m.%Y")

