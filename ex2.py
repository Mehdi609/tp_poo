import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def afficher(self):
        print(f"Point({self.x}, {self.y})")

    def distance_origine(self):
        return math.sqrt(self.x**2 + self.y**2)

    def calculer_vecteur(self, autre_point):
        return Vecteur(autre_point.x - self.x, autre_point.y - self.y)

# instancier des points
p1 = Point(2, 3)
p2 = Point(5, 7)
# afficher les points
p1.afficher()
p2.afficher()
# afficher la distance à l'origine
print("Distance de p1 à l'origine :", p1.distance_origine())
print("Distance de p2 à l'origine :", p2.distance_origine())

print("=====================================")

class Vecteur:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def afficher(self):
        print(f"Vecteur({self.x}, {self.y})")

    def additionner(self, vecteur):
        return Vecteur(self.x + vecteur.x, self.y + vecteur.y)

    def produit_scalaire(self, vecteur):
        return self.x * vecteur.x + self.y * vecteur.y

    def norme(self):
        return math.sqrt(self.x**2 + self.y**2)

# Calculer le vecteur entre p1 et p2
v1 = p1.calculer_vecteur(p2)
v1.afficher()
v2 = Vecteur(1, 4)
v2.afficher()
# Additionner deux vecteurs
v3 = v1.additionner(v2)
print("Résultat de l'addition :")
v3.afficher()
# Calculer le produit scalaire de deux vecteurs
print("Produit scalaire :", v1.produit_scalaire(v2))
# Calculer la norme d'un vecteur
print("Norme de v1 :", v1.norme())
print("Norme de v2 :", v2.norme())
