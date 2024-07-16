import numpy as np

while True:
    # Stampa il menu delle opzioni
    print("\nMenu:")
    print("1. Crea e stampa la matrice originale")
    print("2. Estrai e stampa la matrice 4x4")
    print("3. Inverti e stampa la matrice 4x4")
    print("4. Estrai e stampa la diagonale della matrice originale")
    print("5. Sostituisci i multipli di 3 con -1 nella matrice invertita e stampa")
    print("6. Esci")

    # Richiede all'utente di scegliere un'opzione
    scelta = input("Scegli un'opzione: ")

    # Esegui l'operazione corrispondente alla scelta dell'utente
    if scelta == '1':
        # Crea una matrice 6x6 di numeri interi casuali compresi tra 1 e 100
        array = np.random.randint(1, 101, size=(6, 6))
        # Stampa la matrice originale
        print("Ecco la matrice originale:")
        print(array)
    elif scelta == '2':
        # Estrai una matrice 4x4 dalla matrice originale
        array4x4 = array[1:5, 1:5]
        # Stampa la matrice 4x4
        print("Ecco la matrice 4x4 di quella originale:")
        print(array4x4)
    elif scelta == '3':
        # Inverti la matrice 4x4 (sia righe che colonne)
        array_invertito = array4x4[::-1, ::-1]
        # Stampa la matrice invertita
        print("Ecco la matrice invertita di quella 4x4:")
        print(array_invertito)
    elif scelta == '4':
        # Estrai la diagonale della matrice originale
        array_diagonale = array.diagonal()
        # Stampa la diagonale della matrice originale
        print("Ecco l'array della matrice diagonale:")
        print(array_diagonale)
    elif scelta == '5':
        # Sostituisci tutti gli elementi della matrice invertita che sono multipli di 3 con il valore -1
        array_invertito[array_invertito % 3 == 0] = -1
        # Stampa la matrice invertita modificata
        print("\nEcco la matrice invertita con i multipli di 3 sostituiti con -1:")
        print(array_invertito)
    elif scelta == '6':
        print("Uscita dal programma.")
        break
    else:
        print("Scelta non valida. Per favore, scegli un'opzione valida.")







