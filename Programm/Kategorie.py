class Kategorie:
    def __init__(self, bezeichnung: str):
        self.bezeichnung = bezeichnung.strip().capitalize()
        self.budget = None

    def __str__(self):
        if self.budget:
            return f"{self.bezeichnung} / {self.budget}€"
        return f"{self.bezeichnung} / Kein Budget"

    def set_budget(self, budget: float):
        self.budget = budget
