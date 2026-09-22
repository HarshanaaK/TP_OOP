import unittest
from habitant_protege import Habitant
from heritage import Adulte, Enfant, affichage
from village import Village


class TestHabitant(unittest.TestCase):
    """Tests pour la classe Habitant et l’encapsulation."""

    def test_compte_animal(self):
        """Cas normal : l'habitant possède l'animal."""
        h1 = Habitant("Aldric", 25, "Rue A", {"vaches": 3})
        self.assertEqual(h1.compte_animal("vaches"), 3)

    def test_compte_animal_inexistant(self):
        """Cas limite : l'habitant ne possède pas l'animal."""
        h1 = Habitant("Aldric", 25, "Rue A", {"vaches": 3})
        self.assertEqual(h1.compte_animal("moutons"), 0)


    def test_age_setter_valide(self):
        """Cas normal : age valide."""
        h1 = Habitant("Aldric", 25, "Rue A", {"vaches": 3})
        h1.age = 26
        self.assertEqual(h1.age, 26)

    def test_age_setter_invalide(self):
        """Cas limite : age negatif."""
        h1 = Habitant("Aldric", 25, "Rue A", {"vaches": 3})
        with self.assertRaises(ValueError):
            h1.age = -5


"""Écrivez une classe TestVillage testant les deux méthodes d’ajout d’habitant de la question 5 (compo-
sition et agrégation). Le cas limite attendu est un même habitant ajouté par agrégation à deux villages différents : il
doit apparaître dans les deux listes."""

class TestVillage(unittest.TestCase):
    """Tests pour la classe Village et les méthodes d’ajout d’habitants."""

    def test_ajouter_habitant_composition(self):
        """Cas normal : ajout d'un habitant par composition"""
        village = Village("PyTown")
        village.ajouter_habitant_composition("Aldric", 25, "Rue A", {"vaches": 3})
        self.assertEqual(len(village.get_habitants()), 1)

    def test_ajouter_habitant_agregation(self):
        """Cas normal : ajout d'un habitant par agrégation"""
        village = Village("PyTown")
        habitant = Habitant("Elise", 28, "Rue B", {"poules": 10})
        village.ajouter_habitant_agregation(habitant)
        self.assertEqual(len(village.get_habitants()), 1)

    def test_ajouter_habitant_agregation_meme_habitant(self):
        """Cas limite : ajout du même habitant par agrégation à deux villages différents"""
        village1 = Village("PyTown")
        village2 = Village("VillageVoisin")
        habitant = Habitant("Elise", 28, "Rue B", {"poules": 10})
        village1.ajouter_habitant_agregation(habitant)
        village2.ajouter_habitant_agregation(habitant)
        self.assertIn(habitant, village1.get_habitants())
        self.assertIn(habitant, village2.get_habitants())


if __name__ == "__main__":
    unittest.main(verbosity=2)