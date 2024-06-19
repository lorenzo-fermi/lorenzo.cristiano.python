num1 = input("Indovina il primo numero: ")
# Confronta l'input con il numero corretto (convertito in stringa)
if num1 == "6":
    print("Hai indovinato! Passiamo al prossimo numero.")
    
    # Chiede all'utente di indovinare il secondo numero
    num2 = input("Indovina il secondo numero: ")
    # Confronta l'input con il numero corretto (convertito in stringa)
    if num2 == "20":
        print("Hai indovinato! Passiamo all'ultimo numero.")
        
        # Chiede all'utente di indovinare l'ultimo numero
        num3 = input("Indovina l'ultimo numero: ")
        # Confronta l'input con il numero corretto (convertito in stringa)
        if num3 == "1":
            print("Bravo! Hai indovinato l'ultimo numero.")
        else:
            print("Non hai indovinato l'ultimo numero.")
    else:
        print("Non hai indovinato il secondo numero.")
else:
    print("Non hai indovinato il primo numero.")






