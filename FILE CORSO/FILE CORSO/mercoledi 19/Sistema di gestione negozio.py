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
                    listaCarrello["Pantalone"] 
                print("Pantalone aggiunto al carrello")
            else:
                print("Articolo non disponibile")
        
        elif rispostaDomanda1== "no":
            break

        else:
            print("Risposta non valida. Riprova.")

    # Calcolare il totale del carrello
    totale = 0
    for articolo, quantita in listaCarrello:
        if articolo == "Maglietta":
            totale += quantita 
        elif articolo == "Pantalone":
            totale += quantita 

    print("Carrello:", listaCarrello)
    print("Totale:", totale, "€")

else:
    print("Sistema non avviato.")

articoliVenduti=listaCarrello
print(articoliVenduti)     