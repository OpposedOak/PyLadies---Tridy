# Pravidlo LEGB

# L - LOCAL
# E - ENCLOSING
# G - GLOBAL
# B - BUILT-IN

# L
a = "global"
def funkce():
    a = "local"
    print(a)
funkce()
# Co se vytiskne do konzole ?

# E
a = "global"
def funkce():
    a = "enclosing"
    def vnitrni_funkce():
        print(a)
    vnitrni_funkce()
funkce()
# Co se vytiskne do konzole ?

# G
a = "global"
def funkce():
    def vnitrni_funkce():
        print(a)
    vnitrni_funkce()
funkce()
# Co se vytiskne do konzole ?

# B
def funkce():
    print(None)
funkce()
# Co se vytiskne do konzole ?

# - Jen pro ilustraci, radeji se tomuto pouziti vyhnout!!!
a = "global"
def funkce():
    global a
    a = "local"
    print(a)

funkce()
print(a)

"""Python se ridi pravilem LEGB. Nejpre hleda na lokalni urovni, a pokud nic
nenajde, pak na "enclosing" urovni, potom na global az nakonec v bulit-in
Pokud mluvime o pythonu, lze rici, ze promennou hleda na stejne urovni odsazeni
"""
