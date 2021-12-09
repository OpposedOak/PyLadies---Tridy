# Metody
class Ctverec():
    pocet_stran = 4
    def __init__(self,delka_strany):
        self.delka_strany = delka_strany

    def vypocitej_obvod(self):
        return self.pocet_stran * self.delka_strany

    def vypocitej_obsah(self):
        return self.delka_strany * self.delka_strany

muj_ctverec = Ctverec(10)
print(muj_ctverec.delka_strany)

# Volani metody
print(muj_ctverec.vypocitej_obvod())
print(muj_ctverec.vypocitej_obsah())

# Dedicnost
class Zvire():
    def __init__(self):
        print("Zvire vytvoreno")

    def jez(self):
        print("Jím")

class Pes(Zvire):
    def __init__(self):
        print("Pes vytvoren")

z = Zvire()
z.jez()
# Moznost pouziti metod z jine tridy
p = Pes()
p.jez()

# Prepisovani metod
class Zvire():
    def __init__(self):
        print("Zvire vytvoreno")

    def udelej_zvuk(self):
        print("Brzabspasd")

    def jez(self):
        print("Jím")

class Pes(Zvire):
    def __init__(self):
        Zvire.__init__(self)
        print("Pes vytvoren")

    def udelej_zvuk(self):
        print("Haf")
# Zmena v metode init v Parent class

class Zvire():
    def __init__(self,jmeno):
        self.jmeno = jmeno

    def jez(self):
        print("Jím")

class Pes(Zvire):
    def __init__(self,jmeno):
        Zvire.__init__(self,jmeno)
        print("Pes vytvoren")

    def udelej_zvuk(self):
        print("Haf")

p = Pes("Jack")
# super()

class Zvire():
    def __init__(self,jmeno):
        self.jmeno = jmeno

    def udelej_zvuk(self):
        print("Zvuk")

    def jez(self):
        print("Jím")

class Pes(Zvire):
    def __init__(self,jmeno):
        Zvire.__init__(self,jmeno)
        print("Pes vytvoren")

    def udelej_zvuk(self):
        print("Haf")

    def jez(self):
        print(f"{self.jmeno} si potravu prohlizi")
        super().jez()

p = Pes("Jack")
p.jez()
