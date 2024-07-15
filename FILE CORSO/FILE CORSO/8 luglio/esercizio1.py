import numpy as np

# 1. Utilizza la funzione np.arange per creare un array di numeri interi da 10 a 49.
array = np.arange(10, 50)

# 2. Verifica il tipo di dato dell'array e stampa il risultato.
initial_dtype = array.dtype
print("Tipo di dato iniziale dell'array:", initial_dtype)

# 3. Cambia il tipo di dato dell'array in float64 e verifica di nuovo il tipo di dato.
array = array.astype(np.float64)
new_dtype = array.dtype
print("Tipo di dato dell'array dopo la conversione:", new_dtype)

# 4. Stampa la forma dell'array.
shape = array.shape
print("Forma dell'array:", shape)

