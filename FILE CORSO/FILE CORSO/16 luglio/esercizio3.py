import numpy as np


while True:
    print("menu")
    print("1.creiamo l'array che ")
    print("2. crea un array di 0 e 1")
    print("3. somma i due array creati")
    print("4. fai la somma degli elementi della somma dei due array")
    print("5. somma solo i numeri del nuovo array maggiori di 5")
    print("6. esci dal programma")
    scelta=input("scegli cosa fare: ")

    if scelta=="1":
        array=np.linspace(0,10,50)
        print(array)

    elif scelta=="2":
        array01=np.linspace(0,1,50)
        print(array)

    elif scelta=="3":
        array_sum=array+array01
        print(array_sum)
    
    elif scelta=="4":
        array_sum_sum=np.sum(array_sum)
        print(array_sum_sum)

    elif scelta=="5":
        array_sum_5 = np.sum(array_sum[array_sum > 5])
        print(array_sum_5)

    elif scelta=="6":
        print("uscita dal programma in corso")
        break


    








