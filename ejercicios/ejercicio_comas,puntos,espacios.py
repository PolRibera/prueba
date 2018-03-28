frase_usuario=input("dime una frase: ")

comas = [","]
puntos= ["."]
espacios= [" "]

n_comas=0
n_puntos=0
n_espacios =0

for letra in frase_usuario:
    if letra in comas:
        n_comas += 1
    else:
        n_comas += 0

for letra in frase_usuario:
    if letra in puntos:
        n_puntos += 1
    else:
        n_puntos += 0

for letra in frase_usuario:
    if letra in espacios:
        n_espacios += 1
    else:
        n_espacios += 0


print("Hay {} comas, {} puntos y {} espacios".format(n_comas,n_puntos,n_espacios))