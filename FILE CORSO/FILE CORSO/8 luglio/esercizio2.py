import numpy as np

# 1. Crea un array di 12 numeri equidistanti tra 0 e 1 usando linspace.
array_linspace = np.linspace(0, 1, 12)

# 2. Cambia la forma dell'array a una matrice 3x4.
array_linspace_reshaped = array_linspace.reshape(3, 4)

# 3. Genera una matrice 3x4 di numeri casuali di 0 e 1.
array_random = np.random.rand(3, 4)

# 4. Calcola e stampa la somma degli elementi di entrambe le matrici.
sum_linspace = np.sum(array_linspace_reshaped)
sum_random = np.sum(array_random)

print("Matrice linspace reshaped:\n", array_linspace_reshaped)
print("Matrice random:\n", array_random)
print("Somma degli elementi della matrice linspace reshaped:", sum_linspace)
print("Somma degli elementi della matrice random:", sum_random)
