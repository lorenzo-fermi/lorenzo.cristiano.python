def cifratura():
    key = int(input("Inserisci la chiave di cifratura (0-25): "))
    dacifrare = input("Inserisci il testo da cifrare: ")
    cifrato = ""

    for x in dacifrare:
        if 'a' <= x <= 'z':
            cifrato += chr((ord(x) - ord('a') + key) % 26 + ord('a'))
        elif 'A' <= x <= 'Z':
            cifrato += chr((ord(x) - ord('A') + key) % 26 + ord('A'))
        else:
            cifrato += x

    return cifrato

def decifratura():
    key = int(input("Inserisci la chiave di decifratura (0-25): "))
    dacifrare = input("Inserisci il testo da decifrare: ")
    decifrato = ""

    for x in dacifrare:
        if 'a' <= x <= 'z':
            decifrato += chr((ord(x) - ord('a') - key) % 26 + ord('a'))
        elif 'A' <= x <= 'Z':
            decifrato += chr((ord(x) - ord('A') - key) % 26 + ord('A'))
        else:
            decifrato += x

    return decifrato

print("Testo cifrato:", cifratura())
print("Testo decifrato:", decifratura())
