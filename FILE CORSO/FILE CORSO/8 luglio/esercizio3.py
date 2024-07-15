import numpy as np

# 1. Creazione e Manipolazione degli Array:
# Crea un array di 10 elementi, tutti uguali a 5.
array_5 = np.full(10, 5)

# Cambia la forma dell'array creato in una matrice 2x5.
array_2x5 = array_5.reshape(2, 5)

# Crea un array di numeri casuali tra 0 e 1 di dimensione 4x4.
array_random_4x4 = np.random.rand(4, 4)

# 2. Operazioni sugli Array:
# Crea due array di dimensione 3x3 e calcola il loro prodotto elemento per elemento.
array_3x3_a = np.random.rand(3, 3)
array_3x3_b = np.random.rand(3, 3)
elementwise_product = array_3x3_a * array_3x3_b

# Calcola la somma di tutti gli elementi di un array 3x3 creato con valori da 1 a 9.
array_1_to_9 = np.arange(1, 10).reshape(3, 3)
sum_1_to_9 = np.sum(array_1_to_9)

# 3. Utilizzo delle Funzioni:
# Crea un array contenente 20 numeri equidistanti tra 0 e 10.
array_20 = np.linspace(0, 10, 20)

# Utilizza numpy.random per generare un array di numeri interi casuali tra 1 e 100 di dimensione 5x5.
array_random_integers_5x5 = np.random.randint(1, 101, size=(5, 5))

# 4. Operazioni sugli Array:
# Crea un array di numeri casuali di dimensione 5x5 e calcola la media dei valori di ciascuna colonna.
array_random_5x5_a = np.random.rand(5, 5)
column_means = np.mean(array_random_5x5_a, axis=0)

# Crea un array di numeri casuali di dimensione 5x5 e calcola la somma dei valori di ciascuna riga.
array_random_5x5_b = np.random.rand(5, 5)
row_sums = np.sum(array_random_5x5_b, axis=1)

# 5. Manipolazione degli Array:
# Crea un array 1D con 12 elementi e trasformalo in una matrice 3x4.
array_1D_12 = np.arange(12)
matrix_3x4 = array_1D_12.reshape(3, 4)

# Estrai la prima colonna dalla matrice creata e sostituiscila con un array di zeri.
matrix_3x4[:, 0] = 0

# 6. Utilizzo di Funzioni:
# Utilizza numpy.random per generare un array di numeri interi casuali tra 50 e 100 di dimensione 3x3. Trova il massimo e il minimo valore di questo array.
array_random_integers_3x3 = np.random.randint(50, 101, size=(3, 3))
max_value = np.max(array_random_integers_3x3)
min_value = np.min(array_random_integers_3x3)

# Crea due array 1D di dimensione 5 con numeri casuali e trova il prodotto scalare tra i due.
array_1D_a = np.random.rand(5)
array_1D_b = np.random.rand(5)
dot_product = np.dot(array_1D_a, array_1D_b)

# Output results
print("Array di 10 elementi, tutti uguali a 5:", array_5)
print("Array 2x5:", array_2x5)
print("Array di numeri casuali 4x4:", array_random_4x4)
print("Prodotto elemento per elemento di due array 3x3:", elementwise_product)
print("Somma degli elementi dell'array 3x3 con valori da 1 a 9:", sum_1_to_9)
print("Array di 20 numeri equidistanti tra 0 e 10:", array_20)
print("Array di numeri interi casuali 5x5 tra 1 e 100:", array_random_integers_5x5)
print("Media dei valori di ciascuna colonna dell'array 5x5 casuale:", column_means)
print("Somma dei valori di ciascuna riga dell'array 5x5 casuale:", row_sums)
print("Matrice 3x4 con la prima colonna sostituita da zeri:", matrix_3x4)
print("Array di numeri interi casuali 3x3 tra 50 e 100:", array_random_integers_3x3)
print("Massimo valore dell'array 3x3:", max_value)
print("Minimo valore dell'array 3x3:", min_value)
print("Prodotto scalare tra due array 1D di dimensione 5:", dot_product)
