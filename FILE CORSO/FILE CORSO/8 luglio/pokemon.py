from random import randint, choice

class Pokemon:
    def __init__(self, nome):
        self.nome = nome
        self.npoke = ""
        self.tipo = ""
        self.livello = 5
        self.maxhp = 40
        self.hp = self.maxhp
        self.dif = 5
        self.atk = 5
        self.difspec = 5
        self.atkspec = 5
        self.vel = 5
        self.exp = 1
        self.mosse = []

    def get_npoke(self):
        return self.npoke

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_tipo(self):
        return self.tipo

    def set_tipo(self, tipo):
        self.tipo = tipo

    def get_livello(self):
        return self.livello

    def set_livello(self, livello):
        self.livello = livello

    def get_hp(self):
        return self.hp

    def set_hp(self, hp):
        self.hp = hp

    def get_maxhp(self):
        return self.maxhp

    def set_maxhp(self, maxhp):
        self.maxhp = maxhp

    def get_dif(self):
        return self.dif

    def set_dif(self, dif):
        self.dif = dif

    def get_atk(self):
        return self.atk

    def set_atk(self, atk):
        self.atk = atk

    def get_difspec(self):
        return self.difspec

    def set_difspec(self, difspec):
        self.difspec = difspec

    def get_atkspec(self):
        return self.atkspec

    def set_atkspec(self, atkspec):
        self.atkspec = atkspec

    def get_vel(self):
        return self.vel

    def set_vel(self, vel):
        self.vel = vel

    def get_exp(self):
        return self.exp

    def set_exp(self, exp):
        self.exp = exp

    def level_up(self):
        self.livello += 1
        self.maxhp = 15 + (self.livello * 3)
        self.hp = self.maxhp
        self.dif += randint(0, 5)
        self.atk += randint(0, 5)
        self.difspec += randint(0, 5)
        self.atkspec += randint(0, 5)
        self.vel += randint(0, 5)
        self.exp = 0

    def randomizer(self):
        for _ in range(randint(0, 4)):
            self.level_up()

    def reset_hp(self):
        self.hp = self.maxhp

    def stampa_pokemon(self):
        print(f"Nome: {self.nome}  --  Level: {self.livello} --  HP: {self.hp}/{self.maxhp} --  Dif: {self.dif} -- Atk: {self.atk} -- DifSp.: {self.difspec} -- AtkSp: {self.atkspec} -- Vel: {self.vel} -- Exp: {self.exp}")

class Bulbasaur(Pokemon):
    famiglia = "Bulbasaur"
    def __init__(self, nome):
        super().__init__(nome)
        self.npoke = "001"
        self.tipo = "Erba/Veleno"
        self.mosse = Mosse.lista_mosse()[2]

class Charmander(Pokemon):
    famiglia = "Charmander"
    def __init__(self, nome):
        super().__init__(nome)
        self.npoke = "002"
        self.tipo = "Fuoco"

class Squirtle(Pokemon):
    famiglia = "Squirtle"
    def __init__(self, nome):
        super().__init__(nome)
        self.npoke = "003"
        self.tipo = "Acqua"

class Pikachu(Pokemon):
    famiglia = "Pikachu"
    def __init__(self, nome):
        super().__init__(nome)
        self.npoke = "004"
        self.tipo = "Elettro"

class Mosse:
    def __init__(self, nome, tipo, potenza, categoria):
        self.nome = nome
        self.tipo = tipo
        self.potenza = potenza
        self.categoria = categoria

    def lista_mosse():
        mosse_base = [
            Mosse("Azione", "Normale", 40, "fisico"),
            Mosse("Foglielama", "Erba", 45, "speciale"),
            Mosse("Braciere", "Fuoco", 40, "speciale"),
            Mosse("Pistolacqua", "Acqua", 40, "speciale"),
            Mosse("Fulmine", "Elettro", 40, "speciale"),
            Mosse("Attacco Rapido", "Normale", 35, "fisico")
        ]
        return mosse_base

class Pokedex:
    def __init__(self):
        self.user = "Player"
        self.parole = []
        with open("C:\\Users\\Elron\\Desktop\\Python\\Pokemon_Acerra\\pokedex.txt", "r") as file:
            contenuto = file.read()
            self.parole = contenuto.split()

    def stampasprite(self, pokemon):
        id = pokemon.get_npoke()
        path = f"C:\\Users\\Elron\\Desktop\\Python\\Pokemon_Acerra\\Sprite\\{id}.txt"
        with open(path, "r") as file:
            sprite = file.read()
        print(sprite)

    def stampa_descrizione(self, pokemon):
        id = pokemon.get_npoke()
        if id in self.parole:
            x = self.parole.index(id)
            self.stampasprite(pokemon)
            print(f"{self.parole[x]} :  {self.parole[x+1]} , pokemon {self.parole[x+3]}, è di tipo {self.parole[x+2]} \n")
        else:
            print("Pokemon ancora non catturato, informazioni non disponibili")

class Team:
    def __init__(self):
        self.team = []
        self.counter = 0

    def cattura_pokemon(self, pokemon):
        if self.counter < 6:
            self.counter += 1
            self.team.append(pokemon)
            print(f"{pokemon.get_nome()} è stato aggiunto al team!")
        else:
            print("Non è possibile aggiungere il pokemon, team al completo\n")

    def scegli_pokemon(self):
        self.mostra_team()
        scelta = input("Seleziona il primo pokemon del team: ")
        return self.team[int(scelta) - 1]

    def mostra_team(self):
        print("Il tuo team:")
        for i, pokemon in enumerate(self.team):
            print(f"{i + 1}. {pokemon.get_nome()}  ---  Livello: {pokemon.get_livello()}")
        print("\n")

    def mostra_statistiche(self):
        print("Statistiche dei Pokemon del tuo team: ")
        for pokemon in self.team:
            pokemon.stampa_pokemon()

    def reset_hp_team(self):
        for pokemon in self.team:
            pokemon.reset_hp()

class Azioni:
    def erba_alta():
        pokemon_selvatico = [
            Pikachu("Pikachu"),
            Bulbasaur("Bulbasaur"),
            Charmander("Charmander"),
            Squirtle("Squirtle")
        ]
        return choice(pokemon_selvatico)

    def combattimento(pscelto, pselvatico):
        print(f"È apparso un {pselvatico.get_nome()} selvatico! Cosa vuoi fare?")
        while pscelto.get_hp() > 0 and pselvatico.get_hp() > 0:
            # Implementa la logica di combattimento qui
            print(f"{pscelto.get_nome()} sta combattendo contro {pselvatico.get_nome()}")
            # Semplice esempio di attacco
            danno = randint(1, 10)
            pselvatico.set_hp(pselvatico.get_hp() - danno)
            if pselvatico.get_hp() <= 0:
                print(f"Hai sconfitto {pselvatico.get_nome()}!")
                break
            # Attacco del selvatico
            danno = randint(1, 10)
            pscelto.set_hp(pscelto.get_hp() - danno)
            if pscelto.get_hp() <= 0:
                print(f"{pscelto.get_nome()} è stato sconfitto!")
                break

def start():
    print("Scegli il tuo Pokémon iniziale:")
    print("1. Bulbasaur")
    print("2. Charmander")
    print("3. Squirtle")
    print("4. Pikachu")
    
    scelta = input("Inserisci il numero del Pokémon scelto: ")

    if scelta == "1":
        return Bulbasaur("Bulbasaur")
    elif scelta == "2":
        return Charmander("Charmander")
    elif scelta == "3":
        return Squirtle("Squirtle")
    elif scelta == "4":
        return Pikachu("Pikachu")
    else:
        print("Scelta non valida.")
        return start()

def main():
    print("Benvenuto nel mondo dei Pokémon!")
    player_team = Team()
    pokedex = Pokedex()

    pokemon_iniziale = start()
    player_team.cattura_pokemon(pokemon_iniziale)

    while True:
        print("Cosa vuoi fare?")
        print("1. Mostra team")
        print("2. Mostra statistiche team")
        print("3. Cerca Pokémon")
        print("4. Esci")

        scelta = input("Inserisci la tua scelta: ")

        if scelta == "1":
            player_team.mostra_team()
        elif scelta == "2":
            player_team.mostra_statistiche()
        elif scelta == "3":
            pokemon_trovato = Azioni.erba_alta()
            print(f"Hai trovato un {pokemon_trovato.get_nome()} di livello {pokemon_trovato.get_livello()}. Vuoi combattere? (sì/no)")
            combatti = input()
            if combatti.lower() == "sì":
                pscelto = player_team.scegli_pokemon()
                Azioni.combattimento(pscelto, pokemon_trovato)
                if pokemon_trovato.get_hp() <= 0:
                    player_team.cattura_pokemon(pokemon_trovato)
                else:
                    print(f"{pokemon_trovato.get_nome()} è scappato!")
                player_team.reset_hp_team()
        elif scelta == "4":
            break
        else:
            print("Scelta non valida.")

if __name__ == "__main__":
    main()


    


   