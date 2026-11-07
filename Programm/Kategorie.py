class Kategorie:
    def __init__(self, bezeichnung: str, budget: float = None):
        self.bezeichnung = bezeichnung.upper()
        self.budget = budget
