import math
class Forme:
    def area(self):
        raise NotImplementedError("La méthode area() doit être implémentée dans la classe fille.")


class Cercle(Forme):
    def __init__(self, rayon):
        self.rayon = rayon

    def area(self):
        return math.pi * self.rayon ** 2

class Carre(Forme):
    def __init__(self, cote):
        self.cote = cote

    def area(self):
        return self.cote ** 2

class Rectangle(Forme):
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur

    def area(self):
        return self.longueur * self.largeur



def afficher_aire(forme):
    print(f"Aire de la forme : {forme.area()}")


cercle = Cercle(5)
carre = Carre(4)
rectangle = Rectangle(6, 3)

afficher_aire(cercle)
afficher_aire(carre)
afficher_aire(rectangle)

