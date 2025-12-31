class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"Nom : {self.name}, Age : {self.age}"
    def birthday(self):
        print(f"{self.name}, tu avais {self.age} ans.")
        self.age += 1
        print(f"Tu as maintenant {self.age} ans.")
    def greeter(self, name, title='Dr', prompt='welcome', message='Live Long and Prosper'):
        print(f"{prompt} {title} {name} - {message}")


#Création d’une Instance (objet) de la Classe Person   
p1 = Person("Mehdi", 22)
p2 = Person("Sara", 25)


# affichage de contenu des Instances de la Classe Person
print(p1.name, 'is', p1.age)
print(p2.name, 'is', p2.age)
print("=====================================")
#Affichage de la nouvelle méthode birthday()
p3 = Person("Lina", 30)
p3.birthday()
p4 = Person("Omar", 28)
p4.birthday()
print("=====================================")
# Afficher un autre message « greeter » sous mon nom avec un autre « message »
p1.greeter("Mehdi", "Mr", "Hello", "Have a great day!")
# Afficher le message « greeter » par défaut sous le nom de Sara
p2.greeter("Sara")

#Supprimer un objet avec la fonction del()
del p2


class Sport_car:
    def __init__(self, brand, model, color, horsepower, speed):
        self.brand = brand
        self.model = model
        self.color = color
        self.horsepower = horsepower
        self.speed = speed

    def __str__(self):
        return (f"Brand: {self.brand}, Model: {self.model}, "
                f"Color: {self.color}, Horsepower: {self.horsepower} HP, "
                f"Speed: {self.speed} km/h")

car1 = Sport_car("Lamborghini", "Huracan", "Yellow", 602, 325)
car2 = Sport_car("Porsche", "911 Turbo S", "Blue", 640, 330)
car3 = Sport_car("Bugatti", "W16 Mistral", "Black", 1500, 420)
car4 = Sport_car("Ferrari", "SF90 Stradale", "Red", 1000, 340)


print(car1)
print(car2)
print(car3)
print(car4)



class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimetre(self):
        return 2 * (self.length + self.width)

    def __str__(self):
        return (f"Rectangle [Length = {self.length}, Width = {self.width}] "
                f"Area = {self.area()}, Perimetre = {self.perimetre()}")


rect1 = Rectangle(10, 5)
rect2 = Rectangle(7, 3)

print(rect1)
print(rect2)


