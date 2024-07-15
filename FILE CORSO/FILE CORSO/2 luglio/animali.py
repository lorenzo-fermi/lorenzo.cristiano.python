# Definizione della classe genitore
class Animale:
    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta
    
    def saluta(self):
        print(f"Ciao, sono un animale e mi chiamo {self.nome} e ho {self.eta} anni.")

# Definizione della classe figlia che eredita da Animale
class Cane(Animale):
    def __init__(self, nome, eta, razza):
        super().__init__(nome, eta)
        self.razza = razza
    
    def abbaia(self):
        print("Woof! Woof!")
    
    def zampa(self):
        print("Il cane usa la zampa per giocare.")

    def saluta(self):
        print(f"Ciao, sono un cane della razza {self.razza} e mi chiamo {self.nome}.")

class Gatto(Animale):
    def __init__(self, nome, eta, razza):
        super().__init__(nome, eta)
        self.razza = razza
    
    def miagola(self):
        print("Miao miao!")

    def fusa(self):
        print("Il gatto fa le fusa quando è felice.")

    def saluta(self):
        print(f"Ciao, sono un gatto della razza {self.razza} e mi chiamo {self.nome}.")

class Coccodrillo(Animale):
    def __init__(self, nome, eta):
        super().__init__(nome, eta)
    
    def mordi(self):
        print("Il coccodrillo mordicchia.")

    def verso(self):
        print("Come fa il coccodrillo???")

    def saluta(self):
        print(f"Ciao, sono un coccodrillo di nome {self.nome} e ho {self.eta} anni.")

# Creazione di un'istanza della classe figlia
mio_cane = Cane("Bea", 6, "Golden Retriever")
mio_cane.saluta()  # Output: Ciao, sono un cane della razza Golden Retriever e mi chiamo Bea.
mio_cane.abbaia()  # Output: Woof! Woof!
mio_cane.zampa()  # Output: Il cane usa la zampa per giocare.

mio_gatto = Gatto("Gattunzo", 2, "Persiano")
mio_gatto.miagola()  # Output: Miao miao!
mio_gatto.saluta()  # Output: Ciao, sono un gatto della razza Persiano e mi chiamo Gattunzo.
mio_gatto.fusa()  # Output: Il gatto fa le fusa quando è felice.

mio_coccodrillo = Coccodrillo("Cocco", 5)
mio_coccodrillo.verso()  # Output: Come fa il coccodrillo???
mio_coccodrillo.saluta()  # Output: Ciao, sono un coccodrillo di nome Cocco e ho 5 anni.
mio_coccodrillo.mordi()  # Output: Il coccodrillo mordicchia.





    




    





