import math
import matplotlib.pyplot as plt


class Noeud:
    def __init__(self, valeur):
        self.valeur = valeur
        self.enfants = []

    def ajouter_enfant(self, noeud):
        self.enfants.append(noeud)

    def afficher(self):
        """
        Affiche l'expression en notation polonaise.
        """
        resultat = str(self.valeur)

        for enfant in self.enfants:
            resultat += " " + enfant.afficher()

        return resultat

    def evaluer(self, variables):
        """
        Évalue l'expression avec les valeurs des variables.
        """
        # Constante
        if isinstance(self.valeur, (int, float)):
            return float(self.valeur)

        # Variable
        if self.valeur not in ["+", "-", "*", "/", "exp", "log", "sin", "cos"]:
            if self.valeur not in variables:
                raise ValueError(
                    f"La variable '{self.valeur}' n'a pas de valeur."
                )
            return float(variables[self.valeur])

        # Opérateur +
        if self.valeur == "+":
            return self.enfants[0].evaluer(variables) + self.enfants[1].evaluer(variables)

        # Opérateur -
        if self.valeur == "-":
            return self.enfants[0].evaluer(variables) - self.enfants[1].evaluer(variables)

        # Opérateur *
        if self.valeur == "*":
            return self.enfants[0].evaluer(variables) * self.enfants[1].evaluer(variables)

        # Opérateur /
        if self.valeur == "/":
            return self.enfants[0].evaluer(variables) / self.enfants[1].evaluer(variables)

        # exp
        if self.valeur == "exp":
            return math.exp(self.enfants[0].evaluer(variables))

        # log
        if self.valeur == "log":
            return math.log(self.enfants[0].evaluer(variables))

        # sin
        if self.valeur == "sin":
            return math.sin(self.enfants[0].evaluer(variables))

        # cos
        if self.valeur == "cos":
            return math.cos(self.enfants[0].evaluer(variables))

        raise ValueError(f"Opérateur inconnu : {self.valeur}")

    def tracer(self, variable, valeurs):
        """
        Trace l'expression en fonction d'une variable.
        """
        resultats = []

        for valeur in valeurs:
            resultats.append(
                self.evaluer({variable: valeur})
            )

        plt.plot(valeurs, resultats)
        plt.xlabel(variable)
        plt.ylabel("f(" + variable + ")")
        plt.grid()
        plt.show()