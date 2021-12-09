
# Motivace
class TridaJedna():
    x = 10
    def __init__(self,param1,param2):
        self.param1 = param1
        self.param2 = param2

    def prvni_metoda(self):
        print(self.param1)

Instance = TridaJedna()
TridaJedna.prvni_metoda()

# Ukázka použití built-in tříd a metod

print(type(10))
print(type("abc"))
print(type(True))

# VLastní třídy
class Kotatko():
    def zamoukej(self):
        print("Mnau!")

kote = Kotatko()

# Atributy

kote.jmeno = "Mourek"
dalsi_kote = Kotatko()
dalsi_kote.jmeno = "Micka"

# Parametr self

class Kotatko():
    def zamoukej(self):
        print(f"{self.jmeno}:Mnau!")

kote = Kotatko()
kote.jmeno = "Mourek"

# Metoda __init__

class Kotatko():
    def zamoukej(self):
        print(f"{self.jmeno}:Mnau!")

kote = Kotatko()
kote.zamoukej()
# Co když zapomenete nastavit atribut ?
kote.jmeno = "Mourek"

class Kotatko():
    def nastav_parametry(self,jmeno):
        self.jmeno = jmeno

    def zamoukej(self):
        print(f"{self.jmeno}:Mnau!")

kote = Kotatko()
kote.nastav_parametry("Micka")

# Použití __init__
class Kotatko():
    def __init__(self,jmeno):
        self.jmeno = jmeno

    def zamoukej(self):
        print(f"{self.jmeno}:Mnau!")

kote = Kotatko("Micka")

# Speciální metody
class Kotatko():
    def __init__(self,jmeno):
        self.jmeno = jmeno

    def __repr__(self):
        return f'<Kotatko jmenem {self.jmeno}>'

    def zamoukej(self):
        print(f"{self.jmeno}:Mnau!")

kote = Kotatko("Micka")
print(kote)
