from noeud import Noeud


# Création de l'arbre exp(2 + y)

racine = Noeud("exp")

addition = Noeud("+")

deux = Noeud(2)
y = Noeud("y")

addition.ajouter_enfant(deux)
addition.ajouter_enfant(y)

racine.ajouter_enfant(addition)


# Affichage en notation polonaise
print(racine.afficher())


# Évaluation avec y = 3
resultat = racine.evaluer({"y": 3})

print("Résultat pour y = 3 :", resultat)


# Tracé
valeurs = [-3, -2, -1, 0, 1, 2, 3]

racine.tracer("y", valeurs)