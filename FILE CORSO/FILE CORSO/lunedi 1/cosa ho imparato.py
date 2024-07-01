def classi():
    class Scuderia:
        numero_di_scuderie = 10

        def __init__(self, nome_scuderia, nomi_piloti):
            self.nome_scuderia = nome_scuderia
            self.nomi_piloti = nomi_piloti

        def info(self):
            print(f"Nome Scuderia: {self.nome_scuderia}")
            print("Nomi Piloti:")
            for pilota in self.nomi_piloti:
                print(f"- {pilota}")

    # Esempio di utilizzo
    scuderia1 = Scuderia("Ferrari", ["Charles Leclerc", "Carlos Sainz"])
    scuderia2 = Scuderia("Mercedes", ["Lewis Hamilton", "George Russell"])

    scuderia1.info()
    scuderia2.info()










   


def menu():
    print("Ecco un menù di cosa ho imparato")
    print("1. Classi ( La funzione si trova a riga: 1 del codice )")


    scelta=input("scegli cosa vedere: ")
    if scelta=="1":
        classi()









menu()





    

    
