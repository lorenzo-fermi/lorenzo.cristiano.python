import random



class UnitaMilitare:
    def __init__(self,nome,numero_soldati):
        self.nome=nome
        self.numero_soldati=numero_soldati

    def muovi(self):                             #funzione per muovere i soldati con quantita randomiche
        self.numero_soldati=random.randint(0,100)      
        if self.numero_soldati== 0:
            print("non ci sono soldati da muovere")
        else:
            print("puoi spostare")

    def attacca(self):                 #funzione per attaccare con un numero di soldati solo in caso siano maggiori di 0 
        if self.numero_soldati==0:
            print("non puoi attaccare")
        else:
            print("puoi attaccare")


    def ritira(self):
        if self.numero_soldati>0:
            print(f"puoi ritirare massimo questo numero di soldati {self.numero_soldati}")
            ritira_soldati=int(input("scegli quanti soldati far ritirare: "))
        
        if ritira_soldati<=self.numero_soldati:
            print("puoi ritirarti")
        else:
            print("non puoi ritirare truppe")



class Fanteria(UnitaMilitare):
    def __init__(self, nome, numero_soldati):
        super().__init__(nome, numero_soldati)

    def costruisci_trincea(self):
        
        if self.numero_soldati <= 10:
            print("non puoi costruire una trincea siete in pochi")
        elif self.numero_soldati >= 10 and self.numero_soldati <=30:
            print("siete abbastanza per costruire una trincea")
        else:
            print("potete costruire facilmente una trincea")



class Artiglieria(UnitaMilitare):
    def __init__(self, nome, numero_soldati,pezzi_artiglieria,munizioni):
        super().__init__(nome, numero_soldati)
        self.pezzi_artiglieria=pezzi_artiglieria
        self.munizioni=munizioni


    def calibra_artiglieria(self):
        quantita=int(input(f"quante munizioni di artiglieria vuoi calibrare?? hai a disposizione {self.pezzi_artiglieria}: "))
        if quantita<=self.pezzi_artiglieria and quantita>0:
            print("Puoi calibrare questa quantita")
        elif quantita==0:
            print("allora non calibreremo niente")
        else:
            print("non puoi calibrare questa quantita")


    


class Cavalleria(UnitaMilitare):
    def __init__(self, nome, numero_soldati):
        super().__init__(nome, numero_soldati)

    def esplora_terreno(self):
        self.numero_soldati=random.randint(0,100)
        if self.numero_soldati>10:
            print("siete in troppi")
        else:
            print("potete andare ad esplorare")


class SupportoLogistica(UnitaMilitare):
    def __init__(self, nome, numero_soldati):
        super().__init__(nome, numero_soldati)










class ControlloMilitare(Fanteria,Artiglieria):
    def __init__(self, nome, numero_soldati):
        super().__init__(nome, numero_soldati,self.pezzi_artiglieria)
        self.unita_registrate=[]


    def mostra_unita(self):
        for unita in self.unita_registrate:
            print(unita)

    
    def dettagli_unita(self):
        while True:
            scelta=input("Scegli l'unita di cui vuoi vedere i dettagli").lower()
            if scelta in self.unita_registrate:
                print(self.unita_registrate[scelta])
            else:
                print("questa unità non esiste")



fanteria=Fanteria("fanteria", numero_soldati=random.randint(0,100))
artiglieria=Artiglieria("Artiglieria",numero_soldati=random.randint(0,100),pezzi_artiglieria=10,munizioni=200)
cavalleria=Cavalleria("Cavalleria",numero_soldati=random.randint(0,100))

        
fanteria.costruisci_trincea()  #funziona
fanteria.attacca()  #funziona
fanteria.muovi() #funziona
fanteria.ritira() #funziona
artiglieria.calibra_artiglieria()

cavalleria.esplora_terreno()     








        