frase ="i topi non avevano nipoti"
frase_invertita = ''
punteggiatura=",. "
for carattere in frase:
    if carattere in punteggiatura:
        frase=frase.replace(carattere,"")
    else:
        frase_invertita = carattere + frase_invertita    #  In ogni iterazione, il carattere corrente viene concatenato alla stringa 'frase_invertita'

print(frase_invertita)

if frase==frase_invertita:
    print("questa frase è palindroma")
else:
    print("questa frase non è palindroma")
        


    
