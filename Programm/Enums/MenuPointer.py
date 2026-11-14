from enum import Enum

class PointingAt(Enum):
    MainMenu = 0
    EinnahmenErfassen = 1
    AusgabenErfassen = 2
    EinnahmenAnzeigen = 3
    AusgabenAnzeigen = 4
    KategorienAnzeigen = 5

    @classmethod
    def value_exists(cls, value: int) -> bool:
        """Überprüft ob gegebener Wert im PointingAt Enum enthalten ist und gibt in dem Fall True zurück"""
        for entry in cls:
            if entry.value == value:
                return True
        return False
    