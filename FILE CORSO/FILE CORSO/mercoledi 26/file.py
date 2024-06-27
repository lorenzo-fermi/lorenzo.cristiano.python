with open("file.csv","r") as file:
    contenuto = file.read()

righe = contenuto.split("\n")

elementi = []
for element in righe:
    elementi.append(element.split(","))

elementi = [element.split(",") for element in righe]
print(elementi[1][1])