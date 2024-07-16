import numpy as np

# Creiamo una matrice 4x4 di numeri casuali compresi tra 10 e 50
matrice4x4 = np.random.randint(10, 50, size=(4, 4))
print("Matrice 4x4 originale:")
print(matrice4x4)

# Utilizziamo il fancy indexing per selezionare gli elementi agli indici (0,1),(0,3),(2,2),(3,0)
indici_righe = [0, 0, 2, 3]
indici_colonne = [1, 3, 2, 0]
elementi_selezionati = matrice4x4[indici_righe, indici_colonne]

# Stampiamo gli elementi selezionati
print("\nElementi selezionati agli indici (0,1), (0,3), (2,2), (3,0):")
print(elementi_selezionati)

# Stampiamo tutte le righe dispari della matrice
print("\nTutte le righe dispari della matrice:")
righe_dispari = matrice4x4[0::2]
print(righe_dispari)

# Aggiungiamo il numero 10 ad ogni elemento della matrice originale
matrice10 = matrice4x4 + 10

# Stampiamo la matrice con il numero 10 addizionato ad ogni elemento della matrice originale
print("\nEcco la matrice con il numero 10 addizionato ad ogni elemento della matrice originale:")
print(matrice10)
