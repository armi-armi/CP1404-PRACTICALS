from musician import Musician


class Band:
    """Band class representing a musical band."""

    def __init__(self, name):
        self.name = name
        self.musicians = []

    def add(self, musician):
        self.musicians.append(musician)

    def play(self):
        for musician in self.musicians:
            print(musician.play())

    def __str__(self):
        return f"{self.name} ({', '.join(str(musician) for musician in self.musicians)})"
