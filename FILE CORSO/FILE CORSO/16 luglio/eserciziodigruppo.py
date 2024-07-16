import numpy as np

def crea():
    # Funzione per creare una matrice con dimensioni specificate dall'utente
    x = int(input("Scrivi numero righe: "))
    y = int(input("Scrivi numero colonne: "))
    array = np.random.randint(0, 10, size=(x, y))  # Creazione della matrice con numeri casuali da 0 a 9
    print("Matrice creata:")
    print(array)  # Stampiamo la matrice appena creata
    return array, x, y  # Ritorniamo la matrice e le sue dimensioni

def estrazione(array, x, y):
    # Funzione per estrarre una sottomatrice specificata dall'utente
    a = int(input("Inserisci inizio riga: "))
    b = int(input("Inserisci fine riga: "))
    c = int(input("Inserisci inizio colonna: "))
    d = int(input("Inserisci fine colonna: "))
    
    if a < x and b <= x and c < y and d <= y:
        # Verifica che gli indici siano all'interno delle dimensioni della matrice
        sotto_matrice = array[a:b, c:d]  # Estrarre la sottomatrice
        print("Sottomatrice ottenuta:")
        print(sotto_matrice)  # Stampiamo la sottomatrice ottenuta
    else:
        print("Errore: La sottomatrice non può essere più grande della matrice.")

def somma_matrice_principale(array):
    # Funzione per calcolare e stampare la somma di tutti gli elementi della matrice
    print("Somma della matrice principale:")
    print(np.sum(array))

def moltiplicazione(array, x, y):
    # Funzione per moltiplicare la matrice principale con una matrice secondaria generata casualmente
    array2 = np.random.randint(0, 10, size=(x, y))  # Creazione della matrice secondaria
    print("Matrice secondaria creata:")
    print(array2)  # Stampiamo la matrice secondaria appena creata
    array_moltiplicazione = array * array2  # Moltiplicazione elemento per elemento
    print("Matrice moltiplicazione:")
    print(array_moltiplicazione)  # Stampiamo la matrice risultante dalla moltiplicazione

def media(array):
    # Funzione per calcolare e stampare la media degli elementi della matrice
    print("Media della matrice:")
    print(np.mean(array))

def determinante(array, x, y):
    # Funzione per calcolare e stampare il determinante della matrice (se quadrata)
    if x == y:  # Verifica se la matrice è quadrata
        determinante = np.linalg.det(array)  # Calcolo del determinante
        print("Determinante della matrice:")
        print(determinante)
    else:
        print("Errore: Il determinante può essere calcolato solo per matrici quadrate.")

# Messaggio di benvenuto e menu delle opzioni
print("Ciao e benvenuto =) ")
print("Menù\n 1) Crea e visualizza array\n 2) Visualizza una sottomatrice\n 3) Somma della matrice principale\n 4) Moltiplica con un'altra matrice\n 5) Fai la media della matrice originale\n 6) Visualizza il determinante\n 7) Esci")

while True:
    scelta = input("Cosa vuoi fare?: ")
    
    if scelta == "1":
        array, x, y = crea()
    
    elif scelta == "2":
        estrazione(array, x, y)
    
    elif scelta == "3":
        somma_matrice_principale(array)
    
    elif scelta == "4":
        moltiplicazione(array, x, y)
    
    elif scelta == "5":
        media(array)
    
    elif scelta == "6":
        determinante(array, x, y)     
   
    elif scelta == "7": 
        print("Grazie per l'uso. Arrivederci!")
        break 
    
    else:
        print("Errore: Scelta non valida. Per favore, scegli un'opzione valida.")

