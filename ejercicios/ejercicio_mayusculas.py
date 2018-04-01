frase_usuario=input("dime una frase: ")

mayusculas = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","X","U","Y","Z"]

n_mayusculas = 0

for letra in frase_usuario:
    if letra in mayusculas:
        n_mayusculas += 1
    else:
        n_mayusculas += 0

print("Hay {} mayusculas".format(n_mayusculas))