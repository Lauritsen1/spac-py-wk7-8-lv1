class Category:
    def __init__(
        self,
        id: str,
        name: str,
        description: str,
    ):
        self.id = id
        self.name = name
        self.description = description

    def __str__(self):
        return self.name
