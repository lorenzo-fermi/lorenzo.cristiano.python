risposta1 = input("Vuoi avviare il sistema? (si/no): ")
articoliVenduti={}
if risposta1 == "si":
    listaCarrello = {}
    maglietta = 15  # Prezzo della maglietta
    pantalone = 20  # Prezzo del pantalone

    while True:
        listaArticoli = ["Maglietta", "Pantalone"]
        print("Articoli disponibili:", listaArticoli)

        rispostaDomanda1 = input("Vuoi acquistare qualcosa? (si/no): ")

        if rispostaDomanda1 == "si":
            rispostaAcquisti = input("Cosa vuoi acquistare? (maglietta/pantalone): ")
                #qui il codice verifica che tipo di articolo ha scelto il cliente e aggiunge gli item al carrello 
            if rispostaAcquisti == "maglietta":
                if "Maglietta" in listaCarrello:
                    listaCarrello["Maglietta"] += 1
                else:
                    listaCarrello["Maglietta"] = 1
                print("Maglietta aggiunta al carrello")
            elif rispostaAcquisti == "pantalone":
                if "Pantalone" in listaCarrello:
                    listaCarrello["Pantalone"] += 1
                else:
                    listaCarrello["Pantalone"] =1          
                print("Pantalone aggiunto al carrello")
            else:
                print("Articolo non disponibile")
        
        elif rispostaDomanda1== "no":       
            break      #il ciclo si ferma ser rispondiamo no 

        else:
            print("Risposta non valida. Riprova.")     

    # Calcolare il totale del carrello
    totale = 0
    for articolo, quantita in listaCarrello.items():
        if articolo == "Maglietta":
            totale += quantita * maglietta
        elif articolo == "Pantalone":
            totale += quantita * pantalone

    print("Carrello:", listaCarrello)
    print("Totale:", totale, "€")

else:
    print("Sistema non avviato.")
#questa parte servirà domani per implementare l'inventario per visualizzare il rapporto di vendite, lo stato dell'inventario e dei guadagni totali
articoliVenduti=listaCarrello
print(articoliVenduti)     