class Dati:
    def __init__(self):
        self.importi_vendita = ""
        self.lista_importi_vendita = []

    def prendi_e_converti_importi(self):
        self.importi_vendita = input("Inserisci una serie di importi di vendita separati da spazi: ")
        # Converti ogni importo a un numero float
        self.lista_importi_vendita = [float(importo) for importo in self.importi_vendita.split()]

# Creazione dell'oggetto Dati
dati = Dati()

# Chiamata al metodo per prendere e convertire gli importi
dati.prendi_e_converti_importi()

# Stampa per verificare la lista degli importi
print("Lista degli importi di vendita convertiti:", dati.lista_importi_vendita)





    


