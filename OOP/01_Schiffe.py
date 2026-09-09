# Simulation von Schiffen, Variante 1
# Zustände in mehreren Listen

schiff_namen = ["RMS Titanic", "Santa Maria"]
schiff_position = [0.0, 2.5]
schiff_geschwindigkeit = [1.0, 0.5]

def bewege_schiffe(dt):
    # dt = delta time: Zeitschritt-Länge: Zeit, die in jedem Simulationsschritt vergeht
    # größeres dt: größere Schritte, Simulation schreitet schneller vorwärts
    # kleineres dt: kleinere Schritte

    # range: len(Position der Schiffe)
    # for i in range(???):
        schiff_position[i] += schiff_geschwindigkeit[i] * dt

def pruefe_kollisionen():

    # range: len(Position der Schiffe)
    for i in range(len(schiff_position)):

        # range: von i + 1 bis len(Position der Schiffe)
        # for j in range(???):
            if abs(schiff_position[i] - schiff_position[j]) < 0.1:

                # Print-Ausgabe vervollständigen: Name des Schiffes bei Index j
                print(f"Kollision zwischen {schiff_namen[i]} und ??? !")

# Simulationsschleife
for t in range(10):
    bewege_schiffe(dt = 1.0)
    pruefe_kollisionen()
    print(f"t={t}: Positionen = {schiff_position}")


# Erst nach erfolgreichem Test:
# Ergänze ein Schiff an zweiter Stelle: Mayflower
# Position = 10.0
# Geschwindigkeit = -0.5
