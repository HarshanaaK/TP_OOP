class Habitant:

    def __init__(self, nom, age, adresse, animaux=None):
        """Initialise un habitant avec un nom, un âge, une adresse et une liste d'animaux."""
        self.__nom = nom
        self.__age = age
        self.__adresse = adresse
        self.__animaux = animaux if animaux is not None else {}

    @property
    def age(self):
        """Getter : appelé lors de l'accès à l'age de l'habitant"""
        return self.__age

    @age.setter
    def age(self, age:int):
        """Setter : appelé lors de la modification de l'age de l'habitant"""
        if age < 0 or age > 130:
            raise ValueError("l'age ne peut pas être négatif ou supérieur à 130 ans")
        self.__age = age
    

    def get_nom(self)->str:
        """Retourne le nom de l'habitant."""
        return self.__nom

    def get_age(self)->int:
         """Retourne l'age de l'habitant"""
         return self.__age

    def get_adresse(self)->str:
         """Retourne l'adresse de l'habitant"""
         return self.__adresse

    def get_animaux(self)->dict:
         """Retourne le dictionnaire des animaux de l'habitant"""
         return self.__animaux

    def set_nom(self, nom: str):
        """Définit le nom de l'habitant."""
        self.__nom = nom

    def set_age(self, age:int):
        """Définit l'âge de l'habitant."""
        self.__age = age

    def set_adresse(self, adresse:str):
        """Définit l'adresse de l'habitant"""
        self.__adresse = adresse

    def set_animaux(self, animaux : dict):
        """définit le dictionnaire des animeaux de l' habitant"""
        self.__animaux= animaux

    def affichage_adresse(self):
        """Affiche l'adresse de l'habitant."""
        print(f"{self.__nom} habite à {self.__adresse}")

    def compte_animal(self, animal):
        """Retourne le nombre d'animaux de type 'animal' que possède l'habitant."""
        return self.__animaux.get(animal, 0)


# instance de la classe Habitant
h1 = Habitant("Aldric", 25, "Rue A", {"vaches": 3})

#Test des méthodes de la classe Habitant
h1.age = 26
assert h1.age == 26

try:
    h1.age = -5
    assert False, "une ValueError aurait du etre levee"
except ValueError:
    pass