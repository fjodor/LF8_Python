class Auto:
    def __init__(self, marke, farbe, ps):
        self.marke = marke
        self.farbe = farbe
        self.ps = ps

mein_auto = Auto("Audi", "metallicblau", 150)

print(mein_auto)


# Zugriff auf Attribute

print(mein_auto.marke)
print(mein_auto.farbe)
print(mein_auto.ps)

# Print-Methode implementieren
# Quelle: Python lernen kurz & gut, Michael Inden, S. 119
# In die Klassendefinition integrieren:
# def __str__(self):
# Soll print-Methode für Marke, Farbe und PS enthalten

class Auto:
    def __init__(self, marke, farbe, ps):
        self.marke = marke
        self.farbe = farbe
        self.ps = ps

    def __str__(self):
        return f"???"

mein_auto = Auto("Audi", "metallicblau", 150)

print(mein_auto)
