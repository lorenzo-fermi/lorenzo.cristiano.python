import random

class GestioneClienti:
    # Dizionario per memorizzare i clienti
    clienti = {}
    
    def crea_clienti(self,cliente):
        cliente._ContoBancarioset_nome(input("inserisci il nome: "))
        cliente._ContoBancarioset_cognome(input("inserisci il cognome: "))
        cliente._ContoBancarioset_saldo(int(input("inserisci il saldo iniziale: ")))
        self.clienti[cliente._ContoBancarioget_numero_conto()] = cliente

    def elimina_cliente(self,conto):
        trovato = False
        for n_conto,cliente in self.clienti.items():
            if cliente == conto:
                i = n_conto
                trovato = True
        if trovato:
            self.clienti.pop(i)
            print("Eliminato!")
        else:
            print("Cliente non trovato")

    def modifica_cliente(self,conto):
        trovato = False
        for n_conto,cliente in self.clienti.items():
            if cliente == conto:
                i = n_conto
                trovato = True
        if trovato:
            while True:
                a = input("Indica azione:\n1: Modifica Nome\n2: Modifica Cognome\n3: Exit\n")
                if a == "1":
                    conto._ContoBancarioset_nome(input("inserisci il nome: "))
                elif a == "2":
                    conto._ContoBancarioset_cognome(input("inserisci il cognome: "))
                elif a == "3":
                    break
                else:
                    print("Error")
            self.clienti[i] = conto
            print("Modificato con successo!")
        else:
            print("Conto non trovato")

class ContoBancario:
    def __init__(self):
        self.__saldo = 0
        self.__nome = ""
        self.__cognome = ""
        # Genera un numero di conto casuale di 13 cifre
        self.__numero_conto = ''.join(str(random.randint(0, 9)) for _ in range(13))

    # Metodo privato per impostare il nome
    def __set_nome(self, nome):
        self.__nome = nome

    # Metodo privato per impostare il cognome
    def __set_cognome(self, cognome):
        self.__cognome = cognome

    # Metodo privato per impostare il saldo
    def __set_saldo(self, saldo):
        self.__saldo = saldo

    # Metodo pubblico per ottenere il nome
    def get_nome(self):
        return self.__nome
    
    # Metodo pubblico per ottenere il cognome
    def get_cognome(self):
        return self.__cognome
    
    # Metodo privato per ottenere il numero di conto
    def __get_numero_conto(self):
        return self.__numero_conto
    
    # Visualizza i dettagli del cliente
    def visualizza_dettagli_cliente(self):
        print(f"Nome: {self.__nome} {self.__cognome}")
        print(f"Numero conto: {self.__numero_conto}")
        
    # Metodo per depositare un importo nel conto
    def deposita(self,importo):
        if importo>0:
            self.saldo=self.saldo+importo
        else:
            print("Importo errato")

    def preleva(self,importo):
        if self.saldo>=importo and importo>0:
            self.saldo=self.__saldo-importo
        else:
            print("Saldo Insufficiente")

    # Metodo per effettuare un pagamento dal conto
    def effettua_pagamento(self, importo, beneficiario):
        if self.__saldo >= importo and importo > 0:
            self.__saldo -= importo
            beneficiario.deposita(importo)
            print(f"Pagamento di {importo} effettuato a favore di {beneficiario.get_nome()} {beneficiario.get_cognome()}.")
        else:
            return "Saldo insufficiente o importo non valido"
        
    # Visualizza il saldo disponibile
    def visualizza_saldo(self):
        print(f"Saldo disponibile: {self.__saldo}")
    
    # Metodo pubblico per ottenere il saldo
    def get_saldo(self):
        return self.__saldo
    
class Prodotto():

    def init(self,nome,prezzo,quantita):
          self.nome=nome
          self.prezzo=prezzo
          self.quantita=quantita

    def _set_nome(self,nome):
         self.nome=nome

    def _set_prezzo(self,prezzo):
         self.prezzo=prezzo

    def _set_quantita(self,quantita):
         self.quantita=quantita

    def get_nome(self):
         return self.nome

    def get_prezzo(self):
         return self.prezzo

    def get_quantita(self):
         return self.quantita

class Negozio(Prodotto):

    inventario={}

    def inserisci_prodotto(self,prodotto,quantita):
        nomeprodotto = self.get_nome(prodotto)

        self.inventario[nomeprodotto]=quantita

    def mostra_inventario(self):
        return self.inventario.items()    

# Esempio di utilizzo
cliente1 = ContoBancario()
cliente2 = ContoBancario()
gestione = GestioneClienti()

# Crea nuovi clienti
gestione.crea_clienti(cliente1)
gestione.crea_clienti(cliente2)
print(gestione.clienti)

# Deposita denaro nei conti dei clienti
cliente1.deposita(300)
cliente2.deposita(300)

# Effettua un pagamento da cliente1 a cliente2
cliente1.effettua_pagamento(200, cliente2)

# Visualizza i dettagli dei clienti e i loro saldi
cliente1.visualizza_dettagli_cliente()
cliente1.visualizza_saldo()

cliente2.visualizza_dettagli_cliente()
cliente2.visualizza_saldo()

# Elimina un cliente
gestione.elimina_cliente(cliente1)
print(gestione.clienti)
