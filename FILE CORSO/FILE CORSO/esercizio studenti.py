"""
Scrivete un programma che prenda i nomi degli alunni di una
classe e i loro voti, quando l’utente scrive media il programma
andrà a stampare i nomi di tutti gli alunni e per ogni alunno la
media dei voti.
Esempio:
Nome: Giovanni , Media: 7.5
Nome: Alfredo , Media: 9
Nome: Michela, Media 10
"""

classe = {
    "Alice": [7, 8, 9],
    "Bob": [6, 7, 8, 7],
    "Charlie": []
}
for nome, voti in classe.items():
    if len(voti) == 0:
        media = 0
    else:
        media = sum(voti) / len(voti)
    print(f"{nome}: {media}")





#utenti = {"id1":{"nome":"tommaso","cognome":"muraca", "indirizzo":"via roma"},
#"id2":{"nome":"Giovanni","cognome":"Rossi"},
#"id3":{"cognome":"Bianchi"}}

#for id in utenti:
#print(f"nome utente '{utenti[id].get('nome','nome non presente')}',
#indirizzo '{utenti[id].get('indirizzo','indirizzo non presente')}'")
