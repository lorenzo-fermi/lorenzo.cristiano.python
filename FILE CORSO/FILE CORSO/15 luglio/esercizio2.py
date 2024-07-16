import numpy as np

# Genera un array di 20 numeri interi casuali compresi tra 10 e 50
arr_casuale = np.random.randint(10, 51, size=20)

# Stampa l'array originale
print("Array originale:")
print(arr_casuale)

# Estrai e stampa i primi 10 elementi
primi_10_elementi = arr_casuale[0:10]
print("Primi 10 elementi:")
print(primi_10_elementi)

# Estrai e stampa gli elementi dall'indice 15 fino alla fine
elementi_dal_15 = arr_casuale[15:]
print("Elementi dall'indice 15 alla fine:")
print(elementi_dal_15)

# Estrai e stampa gli elementi dall'indice 5 all'indice 15
elementi_5_a_15 = arr_casuale[5:15]
print("Elementi dall'indice 5 all'indice 15:")
print(elementi_5_a_15)

# Estrai e stampa gli elementi dall'inizio alla fine con un passo di 3
elementi_passi_3 = arr_casuale[0:20:3]
print("Elementi dall'inizio alla fine con passo di 3:")
print(elementi_passi_3)

# Modifica gli elementi dall'indice 5 all'indice 10 assegnando loro il valore 99
arr_casuale[5:10] = 99

# Stampa l'array modificato
print("Array dopo aver assegnato il valore 99 agli elementi dall'indice 5 all'indice 10:")
print(arr_casuale)




