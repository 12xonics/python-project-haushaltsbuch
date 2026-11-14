class Kategorie:
    def __init__(self, bezeichnung: str, budget: float = None):
        self.bezeichnung = bezeichnung.upper()
        self.budget = budget

    def set_budget(self, budget: float):
        self.budget = budget
