def input_con_confirmacion(pregunta):
    confirmacion = False
    dato_usuario= ""
    while not confirmacion:
        dato_usuario = input(pregunta)
        seguro = input("Has dicho {}, Estas seguro (Si/No)".format(dato_usuario))
        if seguro == "Si":
            confirmacion = True
    return dato_usuario

nombre = input_con_confirmacion("Com et dius?")
print ("Et dius {} ".format(nombre))


def reverse_string  (string_to_reverse):
    string_reversed = ""
    current_index = len(string_to_reverse) - 1
    while current_index >= 0:
        string_reversed += string_to_reverse[current_index]
        current_index -= 1
    return string_reversed

frase_a_voltear = input("Que frase quieres darle la vuelta?")

print(reverse_string("{}".format(frase_a_voltear)))