import numpy as np

# Loop principale del menu
while True:
    # Stampa il menu delle opzioni
    print("\nMenu:")
    print("1. Crea un array di 12 numeri equidistanti tra 0 e 1")
    print("2. Cambia la forma dell'array a una matrice 3x4")
    print("3. Crea una nuova matrice 3x4 di numeri casuali tra 0 e 1")
    print("4. Calcola e stampa la somma della prima matrice 3x4")
    print("5. Calcola e stampa la somma della nuova matrice 3x4")
    print("6. Esci dal programma")

    # Richiede all'utente di scegliere un'opzione
    scelta = input("Scegli cosa fare: ")

    # Opzione 1: Crea un array di 12 numeri equidistanti tra 0 e 1
    if scelta == '1':
        array_equidistante = np.linspace(0, 1, 12)
        print("Array di 12 numeri equidistanti tra 0 e 1:")
        print(array_equidistante)

    # Opzione 2: Cambia la forma dell'array a una matrice 3x4
    elif scelta == '2':
        if 'array_equidistante' in locals():
            array_3x4 = array_equidistante.reshape(3, 4)
            print("Ecco il reshape dell'array iniziale in una matrice 3x4:")
            print(array_3x4)
        else:
            print("Prima devi creare l'array (opzione 1)")

    # Opzione 3: Crea una nuova matrice 3x4 di numeri casuali tra 0 e 1
    elif scelta == '3':
        array3x4nuovo = np.random.random(size=(3, 4))
        print("Ecco la nuova matrice 3x4:")
        print(array3x4nuovo)

    # Opzione 4: Calcola e stampa la somma della prima matrice 3x4
    elif scelta == '4':
        if 'array_3x4' in locals():
            somma_array3x4 = np.sum(array_3x4)
            print("Ecco la somma della prima matrice 3x4:")
            print(somma_array3x4)
        else:
            print("Prima devi creare la matrice 3x4 (opzione 2)")

    # Opzione 5: Calcola e stampa la somma della nuova matrice 3x4
    elif scelta == '5':
        if 'array3x4nuovo' in locals():
            somma_arraynuovo3x4 = np.sum(array3x4nuovo)
            print("Ecco la somma della nuova matrice 3x4:")
            print(somma_arraynuovo3x4)
        else:
            print("Prima devi creare la nuova matrice 3x4 (opzione 3)")

    # Opzione 6: Esci dal programma
    elif scelta == '6':
        print("Uscita dal programma.")
        break

    # Gestione delle opzioni non valide
    else:
        print("Scelta non valida. Per favore, scegli un'opzione valida.")








