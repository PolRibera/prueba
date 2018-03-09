
agente_elegido = input("¿Contra que agente especialitsa quieres luchar? (francotirador/asalto/soporte)")

print("Tu agente es de asalto, asi que tienes 100 de vida")
vida_agente=100
vida_enemigo= 0
ataque_enemigo= 0



if agente_elegido == "francotirador":
    vida_enemigo = 75
    nombre_enemigo = "francotirador"
    ataque_enemigo=25
elif agente_elegido == "asalto":
    vida_enemigo = 100
    nombre_enemigo = "asalto"
    ataque_enemigo=17
elif agente_elegido == "soporte":
    vida_enemigo = 125
    nombre_enemigo = "soporte"
    ataque_enemigo=13

while vida_agente > 0 and vida_enemigo > 0:
   ataque_elegido = input("¿Donde quieres dispararle? (cabeza / cuerpo)")

   if ataque_elegido == "cabeza":
       vida_enemigo -= 25
   elif ataque_elegido == "cuerpo":
       vida_enemigo -= 17

   print("La vida de {} ahora es de {}".format(nombre_enemigo, vida_enemigo))

   print("El agente de {} te hace un ataque de {} de daño".format(agente_elegido, ataque_enemigo))
   vida_agente -= ataque_enemigo

   print("Tienes {} de vida".format(vida_agente))




if vida_enemigo <= 0:
    print("¡¡lo has matado bien!!")
elif vida_agente <= 0:
    print("¡¡te ha matado, no te ralles!!")





