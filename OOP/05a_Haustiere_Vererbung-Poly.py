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
        print(f"{self.name} (Hund) apportiert. " + \
              f"Energie = {self._energie}")

class Katze(Haustier):
    def spielen(self):
        self._energie -= 15
        print(f"{self.name} (Katze) jagt einen Laserpunkt. Energie = {self._energie}")

Benno = Hund("Benno")
Benno.spielen()
Benno.ausruhen()

Mietzi = Katze("Mietzi")
Mietzi.spielen()
Mietzi.ausruhen()
