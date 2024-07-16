import numpy as np

# Genera un array di 15 numeri interi casuali tra 1 e 100
array = np.random.randint(1, 101, size=15)

# Calcola la somma degli elementi dell'array
sum_array = np.sum(array)

# Calcola la media degli elementi dell'array
media_array = np.mean(array)

# Stampa l'array generato
print("Array generato:", array)

# Stampa la somma degli elementi dell'array
print("Somma degli elementi dell'array:", sum_array)

# Stampa la media degli elementi dell'array
print("Media degli elementi dell'array:", media_array)

