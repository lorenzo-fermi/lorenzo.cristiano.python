import numpy as np

#Crea un array contenente numeri interi sequenziali da 1 a 25
array_sequenziale = np.arange(1, 26)

#Ridimensiona l'array in una matrice 5x5
matrice_5x5 = array_sequenziale.reshape(5, 5)

#Stampa la matrice
print("Matrice 5x5 con numeri interi sequenziali da 1 a 25:")
print(matrice_5x5)

#Estrai la seconda colonna
seconda_colonna = matrice_5x5[:, 1]

#Stampa la seconda colonna
print("\nSeconda colonna della matrice:")
print(seconda_colonna)


#Estrai la terza riga della  matrice
terza_riga = matrice_5x5[2,:]

#Stampa la terza riga
print("Terza riga della matrice")
print(terza_riga)

#Estrai la diagonale della matrice e fai la somma di esso 
diagonale_matrice=matrice_5x5.diagonal()
somma_diagonale_matrice=np.sum(diagonale_matrice)

#Stampa la somma della diagonale
print("La somma della diagonale")
print(somma_diagonale_matrice)



