class ContoBancario:
    def __init__(self, titolare, saldo):
        self.__titolare = titolare  # Attributo privato titolare
        self.__saldo = saldo  # Attributo privato saldo
    
    def deposita(self, importo):
        """ Metodo per depositare denaro nel conto """
        if importo > 0:
            self.__saldo += importo  # Incrementa il saldo
        else:
            return "Importo insufficiente"  # Restituisce un messaggio se l'importo è negativo o zero
        
    def preleva(self, importo):
        """ Metodo per prelevare denaro dal conto """
        if self.__saldo >= importo and importo > 0:
            self.__saldo -= importo  # Decrementa il saldo
        else:
            return "Saldo insufficiente"  # Restituisce un messaggio se non ci sono abbastanza fondi o l'importo è negativo
        
    def visualizza_saldo(self):
        """ Metodo per visualizzare il saldo attuale """
        print(f"Saldo disponibile: {self.__saldo}")

    def get_titolare(self):
        """ Metodo per ottenere il titolare del conto """
        return self.__titolare
    
    def get_saldo(self):
        """ Metodo per ottenere il saldo """
        return self.__saldo

# Creazione di un'istanza di ContoBancario
conto = ContoBancario("Cristiano Malgioglio", 3000)

# Esempio di utilizzo dei metodi della classe
conto.deposita(39)  # Deposita 39 euro
conto.visualizza_saldo()  # Output: Saldo disponibile: 3039
conto.preleva(200)  # Preleva 200 euro
conto.visualizza_saldo()  # Output: Saldo disponibile: 2839

# Esempio di accesso diretto agli attributi tramite i metodi getter
x = conto.get_saldo()
y = conto.get_titolare()
print(x)  # Output: 2839
print(y)  # Output: Cristiano Malgioglio




