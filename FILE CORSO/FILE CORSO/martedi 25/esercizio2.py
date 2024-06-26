# Chiede all'utente di inserire una frase
frase = input("Inserisci una frase: ")

# Elenca i caratteri di punteggiatura che si desidera rimuovere
punteggiature = [",", ".", ";", ":"]

# Dizionario per tenere traccia della lunghezza delle parole
lung = {}

def duplicato(frase):
    # Dizionario per tenere traccia delle parole duplicate
    paroleDuplicate = {}

    # Rimuove la punteggiatura e converte la frase in minuscolo
    for punto in punteggiature:
        frase = frase.lower().replace(punto, "")
    
    # Divide la frase in parole, basandosi sugli spazi
    risultato = frase.split()
    
    # Conta le occorrenze di ciascuna parola e registra la lunghezza delle parole
    for i in risultato:
        # Calcola la lunghezza della parola
        val = len(i)
        # Aggiunge la parola al dizionario delle lunghezze, se non è già presente
        lung[i]=val
        
        # Conta le occorrenze della parola
        if i not in paroleDuplicate:
            paroleDuplicate[i] = 1  # Aggiunge la parola al dizionario con conteggio 1
        else:
            paroleDuplicate[i] += 1  # Incrementa il conteggio della parola esistente
    
    # Restituisce il dizionario delle parole duplicate
    return paroleDuplicate

# Stampa il risultato delle occorrenze delle parole
print("Occorrenze: ")
print(duplicato(frase))

# Stampa il risultato delle lunghezze delle parole
print("\n")
print("Lunghezza parole: ")
print(lung)