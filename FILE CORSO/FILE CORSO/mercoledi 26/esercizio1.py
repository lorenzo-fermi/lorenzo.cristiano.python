'''
Scrivete un programma che genera 5 numeri casuali e li salva su un file, l’utente dovrà
cercare di indovinarne almeno 2 oppure avrà perso.'''

import random

#Inizializza una lista vuota per memorizzare i numeri casuali
random_numbers = []
num_input = 5

#Usa un ciclo for per generare i numeri casuali e aggiungerli alla lista
while num_input > 0:
    random_number = random.randint(1, 6) 
    if str(random_number) not in random_numbers:
        random_numbers.append(str(random_number))
        num_input -= 1
    
                                                                        # Genera un numero intero casuale tra 1 e 100
    
with open("numericasuali.txt","w") as file:
    file.write(",".join(random_numbers))

with open("numericasuali.txt","r") as file:
    contenuto = file.read()
print(contenuto)

lista = contenuto.split(",")
print(lista)
contatore= 5
indovinate = 0
while contatore > 1:
    valore = input("inserisci 5 valori ")
    if valore in lista:
        indovinate += 1
        print("hai indovinato un numero")
    contatore -= 1
if indovinate >1:
    print("hai vinto")
else:
    print("hai perso")
    
