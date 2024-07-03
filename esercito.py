import random


class UnitaMilitare:
    def __init__(self,nome,numero_soldati):
        self.nome=nome
        self.numero_soldati=numero_soldati

    def muovi(self):
        self.numero_soldati=random.randint(0,100)
        if self.numero_soldati== 0:
            print("non ci sono soldati da muovere")
        else:
            print("puoi attaccare")

    def attacca(self):
        if self.numero_soldati==0:
            print("non puoi attaccare")
        else:
            print("puoi attaccare")


    def ritira(self):
        if self.numero_soldati>0:
            ritira_soldati=int(input("scegli quanti soldati far ritirare"))
        else:
            print("non puoi spostare truppe")



class Fanteria(UnitaMilitare):
    def __init__(self, nome, numero_soldati):
        super().__init__(nome, numero_soldati)

    def costruisci_trincea(self):
        self.numero_soldati=random.randint(0,100)
        if self.numero_soldati <= 10:
            print("non puoi costruire una trincea siete in pochi")
        elif self.numero_soldati >= 10 and self.numero_soldati <=30:
            print("siete abbastanza per costruire una trincea")
        else:
            print("potete costruire facilmente una trincea")




class Artiglieria(UnitaMilitare):
    def __init__(self, nome, numero_soldati,pezzi_artiglieria=50):
        super().__init__(nome, numero_soldati)
        self.pezzi_artiglieria=pezzi_artiglieria


    def calibra_artiglieria(self):
        quantita=input(f"quante munizioni di artiglieria vuoi calibrare?? hai a disposizione {self.pezzi_artiglieria}")
        if quantita==self.pezzi_artiglieria:
            print("Puoi calibrare questa quantita")
        else:
            print("non puoi calibrare questa quantita")

    


class Cavalleria(UnitaMilitare):
    def __init__(self, nome, numero_soldati):
        super().__init__(nome, numero_soldati)
        

        
        









        