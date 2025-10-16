# test_notation.py
# Tests unitaires pour le module notation.py

import pytest
from notation import*

# -----------------------------
# TODO : Tests unitaires pour valider_notes()
# -----------------------------
def test_valider_notes():
    #arrange
    notes=[3,2,1,2,3,3,2,2,3]
    resultat_attendu = True
    #act
    resultat_obtenu = valider_notes(notes)
    #assert
    assert resultat_attendu == resultat_obtenu




# -----------------------------
# TODO : Tests unitaires pour calculer_points()
# -----------------------------
def test_calculer_points():
    #arrange
    vbase= 3.2
    notes = [3,2,1,2,3,3,2,2,3]
    resultat_attendu = 5.63

    #act
    resultat_obtenu = calculer_points(vbase,notes)

    #assert
    assert resultat_attendu == resultat_obtenu



