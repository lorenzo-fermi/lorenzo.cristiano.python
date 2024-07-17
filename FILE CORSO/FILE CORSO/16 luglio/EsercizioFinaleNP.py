import numpy as np


def crea():
    x=int(input("Scrivi numero righe: "))
    y=int(input("Scrivi numero colonne: "))
    array=np.random.randint(0,10,size=(x,y))
    print(array)
    return array,x,y

def estrazione(array,x,y):
    a=int(input("Inserisci inizio riga: "))
    b=int(input("Inserisci fine riga: "))
    c=int(input("Inserisci inizio colonna: "))
    d=int(input("Inserisci fine colonna: "))
    if a<x and b <x and c < y and d< y:
        sotto_matrice = array[a:b, c:d]
        print(sotto_matrice)
    else:
        print("La sottomatrice non può essere più grande della matrice")
    
    
def somma_matrice_principale(array):
    print(np.sum(array))

def moltiplicazione(array, x, y):
    array2 = np.random.randint(0, 10, size=(x, y))
    array_moltiplicazione = array * array2
    print(array2)
    print("Matrice moltiplicazione:")
    print(array_moltiplicazione)

def media(array):
    print(np.mean(array))

def determinante(array,x,y):
    if x==y:
        determinante = np.linalg.det(array)
        print(determinante)

def matrice_inversa(array):
    matrice_inversa = np.linalg.inv(array)
    print("Inversa di A:\n", matrice_inversa)

def seno_matrice(array):
    seno=np.sin(array)
    print(seno)

def diagonale(array):
    diagonale=np.diagonal(array)
    print(diagonale)

def elementi5(array):
    elementi = array[(array > 3) & (array < 5)]
    print(elementi)

    

print("Ciao e benvenuto =) ")
print("Menù\n 1)Crea e visualizza array\n 2)Visualizza una sottomatrice\n 3)Somma della matrice principale\n 4)Moltiplica con un'altra matrice\n 5)Fai la media della matrice originale\n 6)Visualizza il determinante\n 7)Visualizza matrice inversa\n 8)Visualizza il seno\n 9)Visualizza diagonale\n 10)Visualizza elementi tra 3 e 5\n 11)Esci")
array=None
x=0
y=0
while True:
    scelta=input("Cosa vuoi fare?: ")
    if scelta=="1":
        array,x,y=crea()
    elif scelta=="2":
        if array is None:
            print("devi creare la matrice")
        else:
            estrazione(array,x,y)
    elif scelta=="3":
        if array is None:
            print("devi creare la matrice")
        else:
            somma_matrice_principale(array)
    elif scelta=="4":
        if array is None:
            print("devi creare la matrice")
        else:
            moltiplicazione(array,x,y)
    elif scelta=="5":
        if array is None:
            print("devi creare la matrice")
        else:
            media(array)
    elif scelta=="6":
        if array is None:
            print("devi creare la matrice")
        else:
            determinante(array,x,y)     
    elif scelta=="7":
        if array is None:
            print("devi creare la matrice")
        else:
            matrice_inversa(array)
    elif scelta=="8":
        if array is None:
            print("devi creare la matrice")
        else:
            seno_matrice(array)
    elif scelta=="9":
        if array is None:
            print("devi creare la matrice")
        else:
            diagonale(array)
    elif scelta=="10":
        if array is None:
            print("devi creare la matrice")
        else:
            elementi5(array)
    elif scelta=="11":
        print("Grazie per l'uso")
        break
    else:
        print("Errore")

