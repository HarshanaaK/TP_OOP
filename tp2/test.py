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


if __name__ == "__main__":
    unittest.main(verbosity=2)