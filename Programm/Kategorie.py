class Kategorie:
    def __init__(self, bezeichnung: str, budget: float = None):
        self.bezeichnung = bezeichnung.strip().capitalize()
        self.budget = budget

    def __str__(self):
        if self.budget:
            return f"{self.bezeichnung} / {self.budget:.2f}€"
        return f"{self.bezeichnung} / Kein Budget"

    def set_budget(self, budget: float):
        self.budget = budget
