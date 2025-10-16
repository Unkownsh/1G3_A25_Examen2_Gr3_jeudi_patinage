# notation.py
# TODO : Version buggée — à corriger après exécution des tests unitaires
# TODO : Mettre des commentaires pour identifier les bugs trouvés et comment vous les avez corrigés.

def valider_notes(notes: list[float]) -> bool:
    """
    Vérifie que la liste de notes contient exactement 9 entiers entre -3 et +3.
    :param notes: liste de notes
    :returns: vrai si la liste et valide, sinon faux.
    """
    if len(notes) !=9:  #la liste doit contenir exactement 9 entiers.
        return False

    for n in notes:
        if n <= 3 and n<=-3: #la liste des notes ne doit pas aussi être plus grand que -3
            return True

    return True


def calculer_points(vbase: float, notes: list[float]) -> float:
    """
    Calcule la note finale d’un mouvement.
    :param vbase: valeur de base de la note
    :param notes: liste de notes
    :returns: valeur de la note finale
    """
    try:
        valider_notes(notes)

        note_max = max(notes)
        note_min = min(notes)

        for i in range(len(notes)):
            if notes[i] == note_max : #trouver la note max et min pour ensuite la retitrer de la liste
                notes.remove(notes[i])
            if notes[i] ==note_min:
                notes.remove(notes[i]) #j'ai divisé le code en 2 parties pour que ca soit plus claire pour moi.

        moyenne = sum(notes) / 7 # la moyenne des notes est = au nombres restant apres avoir rétirer le min et le max
        total = vbase + moyenne
        return total

    except ValueError:
        print("Erreur")
        return 0



