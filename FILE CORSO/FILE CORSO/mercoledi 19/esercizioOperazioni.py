print("inserisci due numeri")
num1=int(input("inserisci il primo numero"))
num2=int(input("inserisci il secondo numero"))
operazione=str(input("Inserisci il tipo di operazione da effettuare"))
calcolo=""
if operazione=="addizione":
    calcolo=num1+num2
    print(calcolo)

elif operazione=="sottrazione":
    calcolo=num1-num2
    print(calcolo)

elif operazione=="moltiplicazione":
    calcolo=num1*num2
    print(calcolo)

elif operazione=="divisione":
    if num2 >0:
        calcolo=num1/num2
        print(calcolo)
    else:
        print("Errore: Divisione per zero")
else:
    print("Operazione non valida") 
 
    
    
