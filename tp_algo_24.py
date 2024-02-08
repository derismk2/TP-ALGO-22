class Fraction:
    def __init__(self, num, den):
        assert den > 0, "Le dénominateur doit être un entier strictement positif"
        self.__num = num
        self.__den = den

    def __str__(self):
        if self.__den == 1:
            return str(self.__num)
        else:
            return f'{self.__num}/{self.__den}'

    def __eq__(self, other):
        return self.__num * other.__den == self.__den * other.__num

# Création des instances F1, F2, F3 et F4
F1 = Fraction(3, 4)
F2 = Fraction(-8, 1)
F3 = Fraction(2, 3)
F4 = Fraction(21, 28)

# Affichage des instances
print(F1)
print(F2)
print(F3)
print(F4)

# Test d'égalité
print(F1 == F4)  # Doit renvoyer True
print(F2 == F3)  # Doit renvoyer False
