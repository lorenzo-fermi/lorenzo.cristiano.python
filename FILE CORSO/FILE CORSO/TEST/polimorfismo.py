# Classe base per tutte le auto di Formula 1
class Formula1:
    def __init__(self, team, numero):
        self.team = team
        self.numero = numero
    
    def accelera(self):
        raise NotImplementedError("Questo metodo deve essere implementato nelle classi derivate.")

    def curva(self):
        raise NotImplementedError("Questo metodo deve essere implementato nelle classi derivate.")

# Classe per un tipo specifico di auto di Formula 1: Red Bull Racing
class RedBull(Formula1):
    def __init__(self, team, numero, pilota):
        super().__init__(team, numero)
        self.pilota = pilota
    
    def accelera(self):
        # Sovrascrittura del metodo accelera della classe base
        print(f"Red Bull {self.numero} accelera rapidamente con {self.pilota} al volante.")

    def curva(self):
        # Sovrascrittura del metodo curva della classe base
        print(f"Red Bull {self.numero} curva con agilità grazie alle innovazioni aerodinamiche.")

# Classe per un altro tipo di auto di Formula 1: Mercedes-AMG Petronas
class Mercedes(Formula1):
    def __init__(self, team, numero, pilota):
        super().__init__(team, numero)
        self.pilota = pilota
    
    def accelera(self):
        # Sovrascrittura del metodo accelera della classe base
        print(f"Mercedes {self.numero} accelera potenziata dalla tecnologia ibrida con {self.pilota} al volante.")

    def curva(self):
        # Sovrascrittura del metodo curva della classe base
        print(f"Mercedes {self.numero} curva con precisione grazie al bilanciamento aerodinamico.")

# Funzione per simulare il comportamento di guida di un'auto di Formula 1
def test_auto(auto):
    # Utilizzo del polimorfismo: chiamiamo i metodi accelera() e curva() su qualsiasi oggetto che erediti da Formula1
    auto.accelera()
    auto.curva()

# Creazione di istanze di diverse auto di Formula 1
redbull_car = RedBull("Red Bull Racing", 33, "Max Verstappen")
mercedes_car = Mercedes("Mercedes-AMG Petronas", 44, "Lewis Hamilton")

# Test del polimorfismo: chiamiamo la funzione test_auto con diverse istanze di auto
print("Test Red Bull:")
test_auto(redbull_car)

print("\nTest Mercedes:")
test_auto(mercedes_car)
