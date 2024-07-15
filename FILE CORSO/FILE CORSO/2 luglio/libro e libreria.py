import random

class Libro:
    def __init__(self, titolo, autore, isbn):
        self.titolo = titolo
        self.autore = autore
        self.isbn = isbn
    
    def descrizione(self):
        print(f"Titolo libro: {self.titolo}, Autore: {self.autore}, ISBN: {self.isbn}")

class Libreria:
    def __init__(self):
        self.lista_libri = []

    def aggiungi_libro(self):
        titolo = input("Inserisci il titolo del libro: ")
        autore = input("Inserisci l'autore del libro: ")
        isbn = ''.join(str(random.randint(0, 9)) for _ in range(13))
        nuovo_libro = Libro(titolo, autore, isbn)
        self.lista_libri.append(nuovo_libro)
        print(f"Libro '{titolo}' aggiunto alla libreria.")

    def aggiungi_libro_predefinito(self, titolo, autore, isbn):
        nuovo_libro = Libro(titolo, autore, isbn)
        self.lista_libri.append(nuovo_libro)
        print(f"Libro '{titolo}' aggiunto alla libreria.")

    def mostra_libri(self):
        if not self.lista_libri:
            print("La libreria è vuota.")
        else:
            print("Libri nella libreria:")
            for libro in self.lista_libri:
                libro.descrizione()

    def rimuovi_libro(self):
        isbn_libro = input("Inserisci l'ISBN del libro da rimuovere: ")
        for libro in self.lista_libri:
            if libro.isbn == isbn_libro:
                self.lista_libri.remove(libro)
                print(f"Libro con ISBN '{isbn_libro}' rimosso dalla libreria.")
                return
        print(f"Nessun libro trovato con ISBN '{isbn_libro}'.")

    def cerca_per_titolo(self):
        titolo_da_cercare = input("Inserisci il titolo del libro da cercare: ")
        for libro in self.lista_libri:
            if libro.titolo.lower() == titolo_da_cercare.lower():
                print("Questo libro è presente in libreria:")
                libro.descrizione()
                return
        print("Questo libro non esiste in libreria.")

# Esempio di utilizzo delle classi
libreria = Libreria()

# Aggiunta di un libro predefinito
libro1 = ("Ayrton Senna", "Giorgio Terruzzi", "9788879110501")
libreria.aggiungi_libro_predefinito(*libro1)

# Mostra i libri nella libreria
libreria.mostra_libri()

# Aggiunta di un libro tramite input dell'utente
libreria.aggiungi_libro()

# Mostra i libri nella libreria
libreria.mostra_libri()

# Rimuovi un libro tramite ISBN
libreria.rimuovi_libro()

# Mostra i libri nella libreria dopo la rimozione
libreria.mostra_libri()

# Cerca un libro per titolo
libreria.cerca_per_titolo()



