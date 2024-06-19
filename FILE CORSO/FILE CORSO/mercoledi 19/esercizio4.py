print("PER ACCEDERE INSERISCI NOME UTENTE E PASSWORD")

datiDiAccesso = {
    "password": "1234",
    "nomeUtente": "admin"
}
#inserimento delle credenziali 
nomeUtente1 = input("Inserisci nome utente: ")
password1 = input("Inserisci la password: ")

#controllo delle credenziali con quelle inserite 

if nomeUtente1 == datiDiAccesso["nomeUtente"] and password1 == datiDiAccesso["password"]:
    print("Accesso consentito!")
    print("Benvenuto admin")
    rispostaDiSicurezza = str(input("Ecco una domanda di sicurezza in caso tu voglia reimpostare la password: 'Dimmi il tuo animale preferito': "))
else:
    print("Accesso negato, credenziali errate.")
    risposta = input("Vuoi reimpostare le credenziali? (si/no): ") 
    if risposta == "si":
        rispostaDiSicurezza1 = str(input("Dimmi il tuo animale preferito: "))
        #inserimento delle nuove credenziali
        if rispostaDiSicurezza1=="cane" : 
            utente1 = input("Inserisci il nuovo nome utente: ")
            password1 = input("Inserisci la nuova password: ")
            datiDiAccesso["nomeUtente"] = utente1
            datiDiAccesso["password"] = password1
            print("Credenziali aggiornate con successo!")
        else:
            print("Risposta di sicurezza errata. Impossibile reimpostare le credenziali.")
    else:
        print("Esci dal sistema o riprova.")

