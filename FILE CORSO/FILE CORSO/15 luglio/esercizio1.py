import numpy as np

# Creiamo un array di numeri interi da 10 a 49
arr = np.arange(10, 50)

# Verifichiamo il tipo di dato dell'array
print(arr)
print("Tipo di dato:", arr.dtype)
print("ecco la forma dell'array", arr.shape)
arr.dtype=float
print("tipo di dato nuovo:", arr.dtype)
print("ecco la forma nuova dell'array:", arr.shape)
