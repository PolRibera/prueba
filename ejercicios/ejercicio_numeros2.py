numero_usuario=int (input("de que nunmero quieres la tabla de mutiplicar:"))

multiplos= 2,4,6,8,10

for multiplo in range(1,11):
    print("{} * {} = {}".format(numero_usuario,multiplo,numero_usuario * multiplo))