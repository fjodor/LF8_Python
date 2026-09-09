class Haustier:
    def __init__(self, name):
        self.name = name
        self._energie = 100  # Unterstrich: Konvention für geschütztes Attribut (nicht von außen ändern)

    def spielen(self):
        self._energie -= 10
        print(f"{self.name} spielt. Energie = {self._energie}")

    def ausruhen(self):
        self._energie += 5
        print(f"{self.name} ruht sich aus. Energie = {self._energie}")

class Hund(Haustier):
    def spielen(self):
        self._energie -= 5
        print(f"{self.name} (Hund) apportiert. Energie = {self._energie}")

class Katze(Haustier):
    def spielen(self):
        self._energie -= 15
        print(f"{self.name} (Katze) jagt einen Laserpunkt. Energie = {self._energie}")

haustiere = [
    Hund("Bello"),
    Katze("Minka"),
    Haustier("Goldfisch")
]

for h in haustiere:
    h.spielen()   # polymorph: je nach Typ passiert etwas anderes
