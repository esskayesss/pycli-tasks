class Category:
    def __init__(self, name: str, ID:int = None):
        self.ID = ID
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Category({self.name}<{self.ID}>)"
