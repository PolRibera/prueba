frase_usuario= input("dime una frase: ")
palabra_substituir= input("dime una palabra que se va a substituir por a:")



for valor in frase_usuario:
    frase_usuario.replace("a",palabra_substituir)

print( frase_usuario.replace("a",palabra_substituir))

