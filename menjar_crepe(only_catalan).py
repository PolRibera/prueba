apetece_crepe_input =input("Vols una crep? (Si/No): ").upper()

if apetece_crepe_input =="SI":
     apetece_crepe = True
elif apetece_crepe == "NO":
     apetece_crepe = False
else:
    print("Digues Si o No, com no se que has dit ho compto com no")
    apetece_crepe = False

tiene_dinero_input =input("Tens diners per comprar-la? (Si/No): ").upper()
estas_avia_input =input("Estas amb l'avia? (Si/No):").upper()
esta_creperia_input =input("Esta la creperia? (Si/No): ").upper()



tiene_dinero = tiene_dinero_input == "Si"
estas_avia = estas_avia_input == "SI"

apetece_crepe = apetece_crepe_input == "SI"
puede_permitirlo = tiene_dinero or estas_avia
esta_creperia = esta_creperia_input=="SI"


if apetece_crepe and puede_permitirlo and esta_creperia:
    print("Dons menjat la crep")
else:
    print("ET FOTS!!")