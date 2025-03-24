import random

def generatePassword():
    caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    longeur = 10
    mot = ""
    compteur = 0

    while compteur < longeur:
        lettre = caracteres[random.randint(0, len(caracteres) - 1)]
        mot += lettre
        compteur += 1

    return mot