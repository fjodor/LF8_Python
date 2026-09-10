class Haustier:
    def __init__(self, name):
        self.name = name
        self._energie = 100  # Unterstrich: Konvention für geschütztes Attribut (nicht von außen ändern)

    def spielen(self):
        self._energie -= 10
        print(f"{self.name} spielt. Energie = {self._energie}")

class Hund(Haustier):
    def spielen(self):
        self._energie -= 5
        print(f"{self.name} (Hund) apportiert. Energie = {self._energie}")

class Katze(Haustier):
    def spielen(self, eifer):
        self._energie -= eifer
        print(f"{self.name} (Katze) jagt einen Laserpunkt. Energie = {self._energie}")

Benno = Hund("Benno")
Benno.spielen()

Mietzi = Katze("Mietzi")
Mietzi.spielen(eifer = 10)
Mietzi.spielen(eifer = 15)

# Mietzi.spielen()
