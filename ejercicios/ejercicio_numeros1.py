numero_usuario=int (input("de que nunmero quieres la tabla de mutiplicar:"))

for multiplo in range (5, 16):
    print("{} * {} = {}".format(numero_usuario,multiplo,numero_usuario * multiplo))