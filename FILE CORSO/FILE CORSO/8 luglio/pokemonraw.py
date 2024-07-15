
from random import randint,choice

class Pokemon:
       

        def __init__(self, nome):
            self.nome=nome
            self.npoke=""
            self.setipo=""
            self.livello=5
            self.maxhp=40
            self.hp=self.maxhp
            self.dif=5
            self.atk=5
            self.difspec=5
            self.atkspec=5
            self.vel=5
            self.exp=1
            self.mosse = []

        


        def get_npoke(self):
            return self.npoke
        
          # Getter per nome
        def get_nome(self):
            return self.nome

        # Setter per nome
        def set_nome(self, nome):
            self.nome = nome

        # Getter per tipo
        def get_tipo(self):
            return self._tipo

        # Setter per tipo
        def set_tipo(self, tipo):
            self.tipo = tipo

        # Getter per livello
        def get_livello(self):
            return self.livello

        # Setter per livello
        def set_livello(self, livello):
            self.livello = livello

        # Getter per hp
        def get_hp(self):
            return self.hp

        # Setter per hp
        def set_hp(self, hp):
            self.hp = hp

        # Getter per maxhp
        def get_maxhp(self):
            return self.maxhp

        # Setter per maxhp
        def set_maxhp(self, maxhp):
            self.maxhp = maxhp

        # Getter per dif
        def get_dif(self):
            return self.dif

        # Setter per dif
        def set_dif(self, dif):
            self.dif = dif

        # Getter per atk
        def get_atk(self):
            return self.atk

        # Setter per atk
        def set_atk(self, atk):
            self.atk = atk

        # Getter per difspec
        def get_difspec(self):
            return self.difspec

        # Setter per difspec
        def set_difspec(self, difspec):
            self.difspec = difspec

        # Getter per atkspec
        def get_atkspec(self):
            return self.atkspec

        # Setter per atkspec
        def set_atkspec(self, atkspec):
            self.atkspec = atkspec

        # Getter per vel
        def get_vel(self):
            return self.vel

        # Setter per vel
        def set_vel(self, vel):
            self.vel = vel

        # Getter per exp
        def get_exp(self):
            return self.exp

        # Setter per exp
        def set_exp(self, exp):
            self.exp = exp
        
        def level_up(self):
            self.livello += 1
            self.maxhp = 15 + (self.livello * 0.3)
            self.hp=self.maxhp
            self.dif += randint(0, 5)
            self.atk += randint(0, 5)
            self.difspec += randint(0, 5)
            self.atkspec += randint(0, 5)
            self.vel += randint(0, 5) 
            self.exp = 0
        
        def randomizer(self):
            for x in range(randint(0,4)):
             self.level_up()   

        def stampa_pokemon(self):
            print(f"Nome: {self.nome}  --  Level: {self.livello} --  HP: {self.hp}/{self.maxhp} --  Dif: {self.dif} -- Atk: {self.atk} -- DifSp.: {self.difspec} -- AtkSp: {self.atkspec} -- Vel: {self.vel} -- Exp: {self.exp}")

class Bulbasaur(Pokemon):
    famiglia="Bulbasaur"
    def __init__(self, nome):
        super().__init__(nome)
        self.npoke = "001"
        self.tipo = "Erba/Veleno"
        self.mosse = Mosse.lista_mosse()[2]

class Charmander(Pokemon):
    famiglia="Charmander"
    def __init__(self, nome):
        super().__init__(nome)
        self.npoke = "002"
        self.tipo = "Fuoco"

class Squirtle(Pokemon):
    famiglia="Squirtle"
    def __init__(self, nome):
        super().__init__(nome)
        self.npoke = "003"
        self.tipo = "Acqua"

class Pikachu(Pokemon):
    famiglia="Pikachu"
    def __init__(self, nome):
        super().__init__(nome)
        self.npoke = "004"
        self.tipo = "Elettro"

class Mosse:

    def __init__(self, nome, tipo, potenza,categoria):
        self.nome = nome
        self.tipo = tipo
        self.potenza = potenza
        self.categoria = categoria

    def lista_mosse():
        mosse_base = [
        Mosse("Azione", "Normale", 40,"fisico"),
        Mosse("Foglielama", "Erba", 45,"speciale"),
        Mosse("Braciere", "Fuoco", 40,"speciale"),
        Mosse("Pistolacqua", "Acqua", 40,"speciale"),
        Mosse("Fulmine", "Elettro", 40,"speciale"),
        Mosse("Attacco Rapido","Normale",35,"fisico")
        ]

        return mosse_base



class Pokedex:

    def __init__(self):
        self.user="Player"

    parole=[]
    with open ("C:\\Users\\Elron\\Desktop\\Python\\Pokemon_Acerra\\pokedex.txt","r") as file:
         contenuto = file.read()
    parole = contenuto.split()

    def stampasprite(self,pokemon):
        id = Pokemon.get_npoke(pokemon)
        path="C:\\Users\\Elron\\Desktop\\Python\\Pokemon_Acerra\\Sprite\\"+str(id)+".txt"
        with open(path,"r") as file:
            sprite=file.read()
        return print(sprite)

    def stampa_descrizione(self,pokemon):
        id = Pokemon.get_npoke(pokemon)
        if id in self.parole:
            x = self.parole.index(id)
            self.stampasprite(pokemon)
            print(f"{self.parole[x]} :  {self.parole[x+1]} , pokemon {self.parole[x+3]}, è di tipo {self.parole[x+2]} \n")
        else:
            print("Pokemon ancora non catturato , informazioni non disponibili")

class Team:

    def __init__(self):
        self.team = []
        self.counter = 0

    def cattura_pokemon(self, pokemon):
        if self.counter < 6:
            self.counter += 1
            self.team.append(pokemon)
        else: print("Non è possibile aggiungere il pokemon, team al completo\n")

    def scegli_pokemon(self):
        self.mostra_team()
        scelta = input("Seleziona il primo pokemon del team: ")
        pass

    def mostra_team(self):
        print("Il tuo team:")
        for pokemon in self.team:
            print(f"{Pokemon.get_nome(pokemon)}  ---  Livello: {Pokemon.get_livello(pokemon)}")
        print("\n")

    def mostra_statistiche(self):
        print("Statistiche dei Pokemon del tuo team: ")
        for pokemon in self.team:
         Pokemon.stampa_pokemon(pokemon)



    def start():
        print("Scegli il tuo Pokémon iniziale:")
        print("1. Bulbasaur")
        print("2. Charmander")
        print("3. Squirtle")
        
        scelta = input("Inserisci il numero del Pokémon scelto: ")

        if scelta.isalpha():
            print("Errore Input ")
        if scelta.isspace():
            print("Errore Input ")
    
        if scelta == "2":
            return Bulbasaur("Bulbasaur")
        if scelta == "3":
            return Charmander("Charmander")
        if scelta == "4":
            return Squirtle("Squirtle")
        else:
            print("Scelta non valida.")


    def trova_pokemon():
        locali = [
            Pikachu("Pikachu"),
            Bulbasaur("Bulbasaur"),
            Charmander("Charmander"),
            Squirtle("Squirtle")
        ]
        return choice(locali)

class Azioni:

    def erba_alta():
     pokemon_selvatico = [
        Pikachu("Pikachu"),
        Bulbasaur("Bulbasaur"),
        Charmander("Charmander"),
        Squirtle("Squirtle")
    ]
     return choice(pokemon_selvatico)

    def combattimento(self, pscelto, pselvatico):
        print(f"E' apparso un {Pokemon.get_nome(pselvatico)} selvatico! Cosa vuoi fare? ")
        while Pokemon.get_hp(pscelto) > 0 and Pokemon.get_hp(pselvatico) > 0:
         break
        ##IMPLEMENTA COMBATTIMENTO E MOSSE


###TEST
# Creazione delle istanze di Pokémon

bulbasaur = Bulbasaur("Bulbasaur")
charmander = Charmander("Charmander")
selvatico = Pikachu("Pika")
selvatico2 = Squirtle("Squirtle")
selvatico3 = Pikachu("Pikachu Surfer")
selvatico4 = Pikachu("Pikachu Cosplay")

# Stampa delle informazioni delle istanze create
print("\nPokemon 1:")
bulbasaur.stampa_pokemon()

print("\nPokemon 2:")
charmander.stampa_pokemon()


print("\n")

pokedex=Pokedex()
pokedex.stampa_descrizione(selvatico3)

team=Team()

team.cattura_pokemon(bulbasaur)
team.cattura_pokemon(charmander)
team.cattura_pokemon(selvatico)
team.cattura_pokemon(selvatico2)
team.cattura_pokemon(selvatico3)
team.cattura_pokemon(selvatico4)
team.cattura_pokemon(bulbasaur)

Pokemon.level_up(bulbasaur)
Pokemon.randomizer(charmander)
Pokemon.randomizer(selvatico)
Pokemon.randomizer(selvatico4)
Pokemon.randomizer(selvatico3)
team.mostra_team()
team.mostra_statistiche()