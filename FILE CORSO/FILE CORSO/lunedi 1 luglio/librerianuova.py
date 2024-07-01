"""creare una classe libro che ha al suo interno
titolo autore prezzo e codice isbn che viene generato in automatico
stato prestito
metodo sconto
metodo prestito quindi restituzione e reso
"""


import random

class biblioteca:
    def __init__(self, titolo, autore, prezzo):
        self.titolo = titolo
        self.autore = autore
        self.prezzo = prezzo
        self.prestito = False  # false indica che il libro non è in prestito mentre true significa che è in prestito
        self.isbn = self.genera_isbn()

    def __str__(self):
        stato_prestito = "in prestito" if self.prestito else "disponibile"
        return f"Titolo: {self.titolo}, Autore: {self.autore}, Prezzo: {self.prezzo}, ISBN: {self.isbn}, Stato: {stato_prestito}"

    def genera_isbn(self):
        # Genera un codice ISBN fittizio di 13 cifre
        isbn = ''.join(str(random.randint(0, 9)) for _ in range(13))
        return isbn
    
    def noleggia(self):
        if not self.prestito:
            self.prestito = True
            print(f"Il libro '{self.titolo}' è stato noleggiato.")
        else:
            print(f"Il libro '{self.titolo}' è già noleggiato.")
    
    def restituisci(self):
        if self.prestito:
            self.prestito = False
            print(f"Il libro '{self.titolo}' è stato restituito.")
        else:
            print(f"Il libro '{self.titolo}' non è attualmente noleggiato.")
    
# Funzione per aggiungere un nuovo libro
def aggiungi_libro(lista_libri):
    titolo = input("Inserisci il titolo del libro: ")
    autore = input("Inserisci l'autore del libro: ")
    prezzo = float(input("Inserisci il prezzo del libro: "))
    nuovo_libro = biblioteca(titolo, autore, prezzo)
    lista_libri.append(nuovo_libro)
    print(f"Il libro '{titolo}' è stato aggiunto alla lista.")

# Funzione per noleggiare un libro a scelta
def noleggia_libro(lista_libri):
    titolo = input("Inserisci il titolo del libro da noleggiare: ")
    for libro in lista_libri:
        if libro.titolo.lower() == titolo.lower():
            libro.noleggia()
            return
    print(f"Il libro '{titolo}' non è stato trovato nella lista.")

# Funzione per visualizzare tutti i libri
def visualizza_libri(lista_libri):
    if lista_libri:
        for libro in lista_libri:
            print(libro)
    else:
        print("Nessun libro nella lista.")

# Creazione di oggetti libro
libro1 = biblioteca("Il Nome della Rosa", "Umberto Eco", 15.99)
libro2 = biblioteca("Il Signore degli Anelli", "J.R.R. Tolkien", 25.50)

# Lista dei libri
lista_libri = [libro1, libro2]

# Menu di interazione
def menu():
    while True:
        print("\nMenu:")
        print("1. Visualizza tutti i libri")
        print("2. Aggiungi un nuovo libro")
        print("3. Noleggia un libro")
        print("4. Restituisci un libro")
        print("5. Esci")
        scelta = input("Scegli un'opzione: ")
        
        if scelta == "1":
            visualizza_libri(lista_libri)
        elif scelta == "2":
            aggiungi_libro(lista_libri)
        elif scelta == "3":
            noleggia_libro(lista_libri)
        elif scelta == "4":
            restituisci_libro(lista_libri)
        elif scelta == "5":
            print("Uscita dal programma.")
            break
        else:
            print("Opzione non valida. Riprova.")

# Funzione per restituire un libro a scelta
def restituisci_libro(lista_libri):
    titolo = input("Inserisci il titolo del libro da restituire: ")
    for libro in lista_libri:
        if libro.titolo.lower() == titolo.lower():
            libro.restituisci()
            return
    print(f"Il libro '{titolo}' non è stato trovato nella lista.")

# Esecuzione del menu
menu()





    



