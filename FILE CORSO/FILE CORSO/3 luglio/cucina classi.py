


class Personalecucina:
    def __init__(self,nome,eta,comanda):
        self.nome=nome
        self.eta=eta
        self.comanda=comanda
        self.ordinazioni=[]
    
    def lavora(self):
        print(f"In questo momento sta lavorando {self.nome} e ha eta {self.eta}")

    def ordinazioni(self):
        while True:
            self.comanda=input("Ecco le ordinazioni")
            self.ordinazioni.append(self.comanda)
            scelta=input("vuoi continuare ad ordinare???")
            if scelta=="si":
                pass
            elif scelta=="no":
                break
            else:
                print("non ho capito bene può ripetere???")



        
        
class Chef(Personalecucina):
    def __init__(self, nome, eta,specialità):
        super().__init__(nome, eta)
        self.specialità=specialità
        self.menu=[]


    def prepara_menu(self):
       for _ in range (9):
            piatto=input("inserisci i piatti per una degustazione gourmet: ")
            self.menu.append(piatto)

    def mostra_menu(self):
        print("il menu preparato è: ")
        for piatto in self.menu:
            print(piatto)



class Souschef(Personalecucina):
    def __init__(self, nome, eta):
        super().__init__(nome, eta)

    def gestisci_inventario(self):
        print("sto controllando se ci sono le materie prime")


class Cuocolinea(Personalecucina,Chef):


    def __init__(self, nome, eta, comanda):
        super().__init__(nome, eta, comanda)

    def cucinare():
        print("sto cucinando")
        


    def cucina_piatto(self):
        if self.ordinazioni in self.menu:
            print("posso cucinare tutto")
        else:
            print("non posso cucinare tutto")





chef=Chef("Antonino Cannavacciuolo",49,"italiana")
souschef=Souschef("Barbieri", 50,)
cuocolinea=Cuocolinea("giuseppe",24)
chef.lavora()
chef.prepara_menu()
chef.mostra_menu()
souschef.gestisci_inventario()
cuocolinea.cucina_piatto()
cuocolinea.cucinare()




