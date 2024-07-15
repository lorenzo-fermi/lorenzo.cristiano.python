class Veicolo:
    def __init__(self, marca, modello, anno, accensione=False):
        self.__marca = marca
        self.__modello = modello
        self.__anno = anno
        self.__accensione = accensione

    def accendi(self):
        self.__accensione = True

    def spegni(self):
        self.__accensione = False

    def get_marca(self):
        return self.__marca

    def get_modello(self):
        return self.__modello

    def get_anno(self):
        return self.__anno

    def is_accensione(self):
        return self.__accensione


class Auto(Veicolo):
    def __init__(self, marca, modello, anno, accensione, numero_porte):
        super().__init__(marca, modello, anno, accensione)
        self.__numero_porte = numero_porte

    
    def suona_clacson():
        print("HA-UU-HA")


class Furgone(Veicolo):
    def __init__(self, marca, modello, anno, accensione, capacita_carico):
        super().__init__(marca, modello, anno, accensione)
        self.__capacita_carico = capacita_carico

    def carica(self):
        quantita = int(input("Quante scatole vuoi caricare sul furgone?: "))
        if quantita > self.__capacita_carico:
            print("Non puoi caricare questa quantità")
        else:
            self.__capacita_carico -= quantita
            print(f"Hai caricato {quantita} scatole. Capacità rimanente: {self.__capacita_carico} scatole.")

    def scarica(self):
        quantita = int(input("Quanti scatole vuoi scaricare?: "))
        if quantita > self.__capacita_carico:
            print("Non hai tutte queste scatole")
        else:
            self.__capacita_carico -= quantita
            print(f"Hai scaricato {quantita} scatole. Capacità rimanente: {self.__capacita_carico} scatole.")


class Motocicletta(Veicolo):
    def __init__(self, marca, modello, anno, accensione, tipo):
        super().__init__(marca, modello, anno, accensione)
        self.__tipo = tipo

    def wheelie(self):
        if self.__tipo == "sportiva":
            print("Eseguo un'impennata")


class GestoreParcoVeicoli:
    def __init__(self):
        self.__veicoli = {}

    def aggiungi_veicolo(self):
        while True:
            marca = input("Inserisci la marca del veicolo (o digita 'stop' per terminare): ")
            if marca.lower() == 'stop':
                break
            modello = input(f"Inserisci il modello per la marca '{marca}': ")
            anno = input(f"Inserisci l'anno di produzione per la marca '{marca}', modello '{modello}': ")
            accensione = input(f"Il veicolo è acceso? (True/False) ")
            accensione = True if accensione.lower() == 'true' else False
            
            self.__veicoli[marca] = {'modello': modello, 'anno': anno, 'accensione': accensione}
            
            scelta = input("Vuoi aggiungere un altro veicolo? (si/no): ")
            if scelta.lower() != 'si':
                break

    def rimuovi_veicolo(self):
        while True:
            scelta = input("Quale veicolo vuoi rimuovere? Inserisci la marca (o digita 'stop' per terminare): ")
            if scelta.lower() == 'stop':
                break
            if scelta in self.__veicoli:
                self.__veicoli.pop(scelta)
                print(f"Il veicolo {scelta} è stato rimosso.")
            else:
                print("Il veicolo specificato non è presente nel parco veicoli.")

    def lista_veicoli(self):
        print("Lista dei veicoli nel parco:")
        for marca, info in self.__veicoli.items():
            print(f"Marca: {marca}, Modello: {info['modello']}, Anno: {info['anno']}, Accensione: {info['accensione']}")


# Esempio di utilizzo:
gestore_parco = GestoreParcoVeicoli()

# Aggiunta di veicoli al parco
gestore_parco.aggiungi_veicolo()

# Rimozione di un veicolo
gestore_parco.rimuovi_veicolo()

# Stampa della lista dei veicoli nel parco
gestore_parco.lista_veicoli()

