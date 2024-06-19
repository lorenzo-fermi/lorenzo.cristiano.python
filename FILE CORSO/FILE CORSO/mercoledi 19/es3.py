valore_booleano = input("Inserisci un valore booleano (True o False): ")
valore_intero = input("Inserisci un numero intero: ")
valore_stringa = input("Inserisci una stringa: ")

# Creazione della lista contenente i valori
lista_dati = [valore_booleano, valore_intero, valore_stringa]

# Creazione del dizionario con 'tipididato' come chiave e la lista come valore
dizionario = {'tipididato': lista_dati}

# Stampiamo il dizionario per visualizzare il risultato
print(dizionario)