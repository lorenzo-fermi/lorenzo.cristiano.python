# Leggi il file
with open("testo.txt", "r") as file:
    testo_lipsum = file.read()

# Definisci le punteggiature da rimuovere
punteggiature = [",", ".", ";", ":"]
slash = "\n"

# Rimuovi le punteggiature e converti il testo in minuscolo
for punto in punteggiature:
    testo_lipsum = testo_lipsum.replace(punto, "")
testo_lipsum = testo_lipsum.lower()

# Conta il numero totale di parole
parole = testo_lipsum.split()
numero_parole = len(parole)

# Conta il numero di righe
numero_righe = testo_lipsum.count(slash) + 1  # Aggiungi 1 per considerare l'ultima riga

# Conta il numero di caratteri senza considerare le nuove righe
numero_caratteri = len(testo_lipsum.replace(slash, ""))

# Stampa i risultati
print(f"Numero caratteri: {numero_caratteri}")
print(f"Numero righe: {numero_righe}")
print(f"Numero totale di parole: {numero_parole}")

