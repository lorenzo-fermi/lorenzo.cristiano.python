"""Create un programma python utilizzando le api
https://pokeapi.co/api/v2/pokemon/ {numero} che simula un
pokedex, quando troverete un pokemon in maniera randomica
verificherà se è presente nel vostro pokedex (pokedex.json), in
caso non fosse presente vi permetterà di catturarlo salvando il numero identificativo, nome, abilità, xp(punti esperienza),peso
e altezza.
(Sul sistema API sono presenti poco più di 1000 pokemon)"""

#height #nome(forms.name) #abilities #weight #punti #base_experience
import random
import requests
import json


def pokemon_random():
    id = random.randint(1,1026)
    return id

def info_pokemon(id):
    url = f"https://pokeapi.co/api/v2/pokemon/{id}"
    risposta = requests.get(url) #eff richiesta get dell'api
    risposta_json = risposta.json() #conversione in dict
    nome = risposta_json["forms"][0]["name"] #primo elemento lista forms e poi alla chiave name
    peso = risposta_json["weight"] #accede alla chiave
    altezza = risposta_json["height"]
    exp = risposta_json["base_experience"] 
    lista_abilità = [] #creo lista per salvare le abililità
    for diz_abilità in risposta_json["abilities"]: #itero sugli elementi della lista abilities
        abilità=diz_abilità["ability"]["name"] #si accede al dizionario ability e poi alla chiave name
        lista_abilità.append(abilità) #prende il nome dell'abilità e lo aggiunge alla lista
    
    dizionario = {"id":id,"nome":nome,"peso":peso,"altezza":altezza,"exp":exp,"abilita":lista_abilità}
    return dizionario
        


def converti_in_json(dizionario):
    json_pokedex= json.dumps(dizionario)
    
    with open("pokedex.json","a") as file:
        file.write(json_pokedex)
    print("Pokemon aggiunto!")


def verifica_pokedex():    
    try:
        pokedex = leggi_pokedex()
    except:
        print("Pokedex vuoto")
    return pokedex

def leggi_pokedex():
    with open("pokedex.json", "r") as file:
        pokedex = file.read()
    return pokedex

"""def confronto(id):
    pokedex = leggi_pokedex()
    dizionario_json = json.loads(pokedex)
    for element in dizionario_json:
        print(element)
    #print(dizionario_json["nome"])"""


def main():
    while True:
        print("Hai incontrato un pokemon...")
        id=pokemon_random()
        print(info_pokemon(id))
        

        dizionario = info_pokemon(id)
        scelta=input("Vuoi catturarlo (si/no/altro per uscire): ")
        if scelta =="si":
            converti_in_json(dizionario)
        elif scelta == "no":
            continue
        else:
            break
    
   
main()
