lista_stringhe = ""

# Mostra il menu
print("Menu CRUD")
print("1. Aggiungi elemento")
print("2. Rimuovi elemento")
print("3. Visualizza tutti gli elementi")
print("4. Elimina tutti gli elementi")

# Chiedi all'utente di selezionare un'opzione
scelta = input("Seleziona un'opzione (1-4): ")

# Gestisci la scelta dell'utente
if scelta == '1':
    # Aggiungi elemento
    if lista_stringhe:
        nuovo_elemento = input("Inserisci l'elemento da aggiungere: ")
        lista_stringhe = ", {nuovo_elemento}"
    else:
        lista_stringhe = input("Inserisci l'elemento da aggiungere: ")
    print("Elemento aggiunto. Lista attuale: {lista_stringhe}")
elif scelta == '2':
    # Rimuovi elemento
    if lista_stringhe:
        elemento_da_rimuovere = input("Inserisci l'elemento da rimuovere: ")
        lista_stringhe = lista_stringhe.replace(elemento_da_rimuovere, "")(", ")
        print("Elemento rimosso. Lista attuale: {lista_stringhe}")
    else:
        print("La lista è vuota. Non ci sono elementi da rimuovere.")
elif scelta == '3':
    # Visualizza tutti gli elementi
    if lista_stringhe:
        print("Gli elementi nella lista sono: {lista_stringhe}")
    else:
        print("La lista è vuota.")
elif scelta == '4':
    # Elimina tutti gli elementi
    lista_stringhe = ""
    print("Tutti gli elementi sono stati eliminati.")
else:
    # Scelta non valida
    print("Selezione non valida.")

# Fine del programma
print("Fine del programma.")