
agente_elegido = input("¿Contra que agente especialitsa quieres luchar? (francotirador/asalto/soporte)")

print("Tu agente es de asalto, asi que tienes 100 de vida")
vida_agente=100
vida_enemigo= 0

if agente_elegido == "francotirador":
    vida_enemigo = 75

if agente_elegido == "asalto":
    vida_enemigo = 100

if agente_elegido == "soporte":
    vida_enemigo = 125


while vida_agente > 0 and vida_enemigo > 0:
   ataque_elegido = input("¿Donde quieres dispararle? (cabeza / cuerpo)")

   if ataque_elegido == "cabeza":
       vida_enemigo -= 25
   if ataque_elegido == "cuerpo":
       vida_enemigo -= 17

   if agente_elegido == "asalto":
       print("El agente de asalto te hace una ataque de 17 de daño")
       vida_agente -= 17
       print("Tu vida ahora es de {} ".format(vida_agente))
   if agente_elegido == "soporte":
       print("El agente de soporte te hace una ataque de 13 de daño")
       vida_agente -= 13
       print("Tu vida ahora es de {} ".format(vida_agente))
   if agente_elegido == "francotirador":
      print("El agente de francotirador te hace una ataque de 25 de daño")
      vida_agente -= 25
      print("Tu vida ahora es de {} ".format(vida_agente))



if vida_enemigo <= 0:
    print("¡¡lo has matado bien!!")
if vida_agente <= 0:
    print("¡¡te ha matado, no te ralles!!")




print("El combate ha terminado")
