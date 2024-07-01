class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"Punto(x={self.x}, y={self.y})"
    
    def muovi_punto(self):
        while True:
            
            newx = int(input("Scegli il punto dove spostare la x: "))
            newy = int(input("Scegli dove spostare la y: "))

            if newx >= 0 and newy >= 0:
                    self.x = newx
                    self.y = newy
                    print(f"La x si è spostata a {newx} e la y a {newy}")
                    break
            else:
                print("Le coordinate devono essere maggiori o uguali a 0.")
            
                

# Creazione di un oggetto Punto con coordinate iniziali (2, 3)
p = Punto(0, 0)
print(p)  # Output: Punto(x=2, y=3)

# Invocazione del metodo muovi_punto per spostare il punto
p.muovi_punto()

# Stampare le nuove coordinate del punto dopo lo spostamento
print(p)
