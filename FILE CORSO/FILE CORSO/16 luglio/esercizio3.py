import numpy as np

# Crea un array di 50 numeri equidistanti tra 0 e 10
array = np.linspace(0, 10, 50)

# Crea un array di 50 numeri equidistanti tra 0 e 1
array01 = np.linspace(0, 1, 50)

while True:
    # Stampa il menu delle opzioni
    print("\nMenu:")
    print("1. Stampare l'array 'array'")
    print("2. Stampare l'array 'array01'")
    print("3. Sommare 'array' e 'array01' e stampare il risultato")
    print("4. Calcolare e stampare la somma di tutti gli elementi di 'array_sum'")
    print("5. Calcolare e stampare la somma degli elementi di 'array_sum' maggiori di 5")
    print("6. Esci")

    # Richiede all'utente di scegliere un'opzione
    scelta = input("Scegli un'opzione: ")

    if scelta == '1':
        # Opzione 1: Stampare l'array 'array'
        print("\nArray 'array':")
        print(array)

    elif scelta == '2':
        # Opzione 2: Stampare l'array 'array01'
        print("\nArray 'array01':")
        print(array01)

    elif scelta == '3':
        # Opzione 3: Sommare 'array' e 'array01' e stampare il risultato
        array_sum = array + array01
        print("\nRisultato della somma di 'array' e 'array01':")
        print(array_sum)

    elif scelta == '4':
        # Opzione 4: Calcolare e stampare la somma di tutti gli elementi di 'array_sum'
        if 'array_sum' not in locals():
            print("\nErrore: devi prima eseguire l'opzione 3 per calcolare 'array_sum'.")
        else:
            sum_array_sum = np.sum(array_sum)
            print("\nSomma di tutti gli elementi di 'array_sum':", sum_array_sum)

    elif scelta == '5':
        # Opzione 5: Calcolare e stampare la somma degli elementi di 'array_sum' maggiori di 5
        if 'array_sum' not in locals():
            print("\nErrore: devi prima eseguire l'opzione 3 per calcolare 'array_sum'.")
        else:
            sum_array_sum_5 = np.sum(array_sum[array_sum > 5])
            print("\nSomma degli elementi di 'array_sum' maggiori di 5:", sum_array_sum_5)

    elif scelta == '6':
        # Opzione 6: Esci dal programma
        print("\nUscita dal programma.")
        break

    else:
        # Opzione non valida
        print("\nScelta non valida. Per favore, scegli un'opzione valida.")







