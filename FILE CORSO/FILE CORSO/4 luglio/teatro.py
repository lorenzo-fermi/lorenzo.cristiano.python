class Posto:
    def __init__(self, numero, fila):
        self._numero = numero
        self._fila = fila
        self._occupato = False

    def prenota(self):
        if not self._occupato:  # Controlla se il posto non è già occupato
            self._occupato = True  # Segna il posto come occupato
            print(f"Il posto {self._fila}{self._numero} è stato prenotato.")
        else:
            print(f"Il posto {self._fila}{self._numero} è già occupato.")  # Messaggio se il posto è già occupato

    def libera(self):
        if self._occupato:  # Controlla se il posto è occupato
            self._occupato = False  # Segna il posto come libero
            print(f"Il posto {self._fila}{self._numero} è stato liberato.")
        else:
            print(f"Il posto {self._fila}{self._numero} è già libero.")  # Messaggio se il posto è già libero

    # Metodi getter per gli attributi privati
    def numero(self):
        return self._numero

    def fila(self):
        return self._fila

    def occupato(self):
        return self._occupato


class PostoVIP(Posto):
    def __init__(self, numero, fila, servizi_extra):
        super().__init__(numero, fila)  # Chiama il costruttore della classe base
        self.servizi_extra = servizi_extra  # Attributo aggiuntivo per servizi extra

    def prenota(self):
        if not self._occupato:  # Controlla se il posto non è già occupato
            self._occupato = True  # Segna il posto come occupato
            print(f"Il posto VIP {self._fila}{self._numero} è stato prenotato con servizi extra: {self.servizi_extra}.")
        else:
            print(f"Il posto VIP {self._fila}{self._numero} è già occupato.")  # Messaggio se il posto è già occupato


class PostoStandard(Posto):
    def __init__(self, numero, fila, costo_aggiuntivo=0):
        super().__init__(numero, fila)  # Chiama il costruttore della classe base
        self.costo_aggiuntivo = costo_aggiuntivo  # Attributo aggiuntivo per costo extra

    def prenota(self):
        if not self._occupato:  # Controlla se il posto non è già occupato
            self._occupato = True  # Segna il posto come occupato
            print(f"Il posto standard {self._fila}{self._numero} è stato prenotato con un costo aggiuntivo di {self.costo_aggiuntivo}€.")
        else:
            print(f"Il posto standard {self._fila}{self._numero} è già occupato.")  # Messaggio se il posto è già occupato


class Teatro:
    def __init__(self):
        self._posti = []  # Inizializza una lista vuota di posti

    def aggiungi_posto(self, posto):
        self._posti.append(posto)  # Aggiunge un posto alla lista

    def prenota_posto(self, numero, fila):
        for posto in self._posti:
            if posto.numero() == numero and posto.fila() == fila:  # Cerca il posto con il numero e la fila specificati
                posto.prenota()  # Prenota il posto trovato
                return
        print(f"Il posto {fila}{numero} non è stato trovato.")  # Messaggio se il posto non è trovato

    def stampa_posti_occupati(self):
        print("Posti occupati:")
        for posto in self._posti:
            if posto.occupato():  # Controlla se il posto è occupato
                print(f"Fila: {posto.fila()}, Numero: {posto.numero()}")  # Stampa le informazioni del posto occupato


# Esempio di utilizzo:
teatro = Teatro()

# Aggiunta di posti al teatro
teatro.aggiungi_posto(PostoVIP(1, 'A', 'Accesso al lounge'))
teatro.aggiungi_posto(PostoStandard(2, 'A', 5))
teatro.aggiungi_posto(Posto(3, 'B'))

# Prenotazione di posti
teatro.prenota_posto(1, 'A')  # Prenota il posto VIP
teatro.prenota_posto(2, 'A')  # Prenota il posto standard
teatro.prenota_posto(3, 'B')  # Prenota il posto base

# Stampa dei posti occupati
teatro.stampa_posti_occupati()

# Liberazione di un posto
teatro._posti[0].libera()  # Libera il primo posto (PostoVIP)

# Stampa dei posti occupati dopo la liberazione
teatro.stampa_posti_occupati()

