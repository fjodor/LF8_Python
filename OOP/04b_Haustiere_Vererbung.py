class Haustier:
    def __init__(self, name):
        self.name = name
        self._energie = 100

    def spielen(self):
        self._energie -= 10
        print(f"{self.name} spielt. Energie = {self._energie}")

    def ausruhen(self):
        self._energie += 5
        print(f"{self.name} ruht sich aus. Energie = {self._energie}")

class Hund(Haustier):
    pass    # erbt alles unverändert

class Katze(Haustier):
    pass    # erbt alles unverändert

class Goldfisch(Haustier):
    def __init__(self, name, farbe = "rotgold"):
        super().__init__(name)   # ruft Konstruktor der Elternklasse auf
        self.farbe = farbe                # neues Attribut der Unterklasse

bruno = Goldfisch("Bruno")
print(bruno.farbe)
bruno.spielen()

# bello = Hund("Bello")
# minka = Katze("Minka")

# bello.spielen()   # nutzt die geerbte Methode
# minka.ausruhen()  # nutzt die geerbte Methode

