import numpy as np

# Creiamo un array di numeri interi da 10 a 49
arr = np.arange(10, 50)

# Iniziamo un ciclo while infinito per permettere all'utente di fare delle scelte
while True:
    # Mostriamo le opzioni disponibili per l'utente
    print("ecco cosa puoi fare:")
    print("1. visualizzare l'array")
    print("2. cambiare il tipo di dato in float")
    print("3. cambiare il tipo di dato in int")
    print("4. visualizzare la forma dell'array")
    print("5. visualizzare il tipo di dato dell'array")
    print("Scrivi stop se vuoi terminare il programma")
    
    # Richiediamo all'utente di fare una scelta
    scelta = input("scegli cosa fare: ")
    
    # Se l'utente sceglie 1, visualizziamo l'array
    if scelta == "1":
        print("Ecco l'array:", arr)
    
    # Se l'utente sceglie 2, cambiamo il tipo di dato dell'array in float
    elif scelta == "2":
        arr = arr.astype(float)
    
    # Se l'utente sceglie 3, cambiamo il tipo di dato dell'array in int
    elif scelta == "3":
        arr = arr.astype(int)
    
    # Se l'utente sceglie 4, visualizziamo la forma dell'array
    elif scelta == "4":
        print("ecco la forma dell'array", arr.shape)
    
    # Se l'utente sceglie 5, visualizziamo il tipo di dato dell'array
    elif scelta == "5":
        print("ecco il tipo di dato dell'array", arr.dtype)
    
    # Se l'utente scrive "stop", terminiamo il programma
    elif scelta == "stop":
        break



    




