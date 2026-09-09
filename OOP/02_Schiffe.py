# Simulation von Schiffen, Variante 2

class Schiff:
    def __init__(self, name, position, geschwindigkeit):
        self.name = name
        self.position = position
        self.geschwindigkeit = geschwindigkeit

    def bewege(self, dt):
        self.position += self.geschwindigkeit * dt

    def abstand_zu(self, anderes):
        return abs(self.position - anderes.position)

schiffe = [
    Schiff("RMS Titanic", 0.0, 1.0),
    Schiff("Santa Maria", 2.5, 0.5)
]

def sim_schritt(dt):
    for s in schiffe:
        s.bewege(dt)

    # range: bis Länge (len) der Liste schiffe
    # for i in range(???):
        for j in range(i + 1, len(schiffe)):
            if schiffe[i].abstand_zu(schiffe[j]) < 0.1:
                print(f"Kollision zwischen {schiffe[i].name} und {schiffe[j].name}!")

for t in range(10):
    sim_schritt(dt = 1.0)
    print(f"t={t}: Positionen = {[s.position for s in schiffe]}")


# Erst nach erfolgreichem Test:
# Ergänze ein Schiff an zweiter Stelle: Mayflower
# Position = 10.0
# Geschwindigkeit = -0.5

