import numpy as np


# Creiamo un array di numeri interi da 10 a 49
arr = np.arange(10, 50)

# Verifichiamo il tipo di dato dell'array

   


while True:
    print("ecco cosa puoi fare:")
    print("1. visualizzare l'array:")
    print("2. cambiare il tipo di dato in float")
    print("3. cambiare il tipo di dato in int")
    print("4. visualizzare la forma dell'array")
    print("5. visualizzare il tipo di dato dell'array")
    print("Scrivi stop se vuoi terminare il programma")
    
    scelta=input("scegli cosa fare: ")
    if scelta=="1":
        print("Ecco l'array:", arr)

    elif scelta=="2":
        arr.dtype=float

    elif scelta=="3":
         arr.dtype=int

    elif scelta=="4":
         print("ecco la forma dell'array", arr.shape)

    elif scelta=="5":
        print("ecco il tipo di dato dell'array", arr.dtype)

    elif scelta=="stop":
        break


    




