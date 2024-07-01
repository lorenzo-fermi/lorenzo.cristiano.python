class Ristorante:
    def __init__(self, nome, tipo_cucina):
        self.nome = nome
        self.tipo_cucina = tipo_cucina
        self.aperto = False  # Il ristorante è chiuso di default
        self.menu = {}  # Dizionario vuoto per il menu

    def apri_ristorante(self):
        self.aperto = True

    def chiudi_ristorante(self):
        self.aperto = False

    def aggiungi_piatto(self, nome_piatto, prezzo):
        self.menu[nome_piatto] = prezzo

    def stampa_menu(self):
        print(f"Menu del ristorante {self.nome}:")
        for piatto, prezzo in self.menu.items():
            print(f"{piatto}: {prezzo} euro")

    def descrivi_ristorante(self):
        print(f"Il ristorante {self.nome} propone cucina {self.tipo_cucina}.")

    def stato_apertura(self):
        if self.aperto:
            print(f"Il ristorante {self.nome} è aperto.")
        else:
            print(f"Il ristorante {self.nome} è chiuso.")

    def togli_dal_menu(self):
        while True:
            nome_piatto = input("Scegli il piatto da togliere: ")
            if nome_piatto in self.menu:
                del self.menu[nome_piatto]
                print(f"Piatto '{nome_piatto}' rimosso dal menu.")
            else:
                print(f"Il piatto '{nome_piatto}' non è presente nel menu.")
            
            scelta = input("Vuoi togliere un altro piatto? (si/no): ")
            if scelta.lower() != "si":
                break

# Esempio di utilizzo della classe Ristorante
ristorante1 = Ristorante("La Pizzeria", "Italiana")
ristorante1.aggiungi_piatto("Margherita", 5.50)
ristorante1.aggiungi_piatto("Carbonara", 8.00)
ristorante1.aggiungi_piatto("Tiramisù", 4.50)

ristorante1.stampa_menu()

ristorante1.togli_dal_menu()
ristorante1.stampa_menu()

def menu():
    print("1. Descrizione del ristorante")
    print("2. Stampa menù")
    print("3. Vedi se il ristorante è aperto")
    print("4. Aggiungi piatto")
    print("5. Togli dal menù un piatto")

menu()
scelta = input("Scegli cosa fare: ")
if scelta == "1":
    ristorante1.descrivi_ristorante()
elif scelta == "2":
    ristorante1.stampa_menu()
elif scelta == "3":
    ristorante1.stato_apertura()
elif scelta == "4":
    nome_piatto = input("Inserisci il nome del piatto da aggiungere: ")
    prezzo = float(input("Inserisci il prezzo del piatto: "))
    ristorante1.aggiungi_piatto(nome_piatto, prezzo)
    print(f"Piatto '{nome_piatto}' aggiunto al menu.")
    ristorante1.stampa_menu()
elif scelta == "5":
    ristorante1.togli_dal_menu()
    ristorante1.stampa_menu()
else:
    print("Scelta non valida.")

    
    
        
    












    