def preguntar(mensaje):
    while True:
        respuesta = input(mensaje).strip().lower()

        if respuesta == "si" or respuesta == "sí":
            return True
        elif respuesta == "no":
            return False
        else:
            print("Respuesta no válida. Escribe 'si' o 'no'.")


edad = preguntar("¿Tienes más de 18 años? (si/no): ")
entrada = preguntar("¿Tienes entrada? (si/no): ")
vestimenta = preguntar("¿Llevas la vestimenta apropiada? (si/no): ")

motivos = []

if not edad:
    motivos.append("No tienes más de 18 años.")

if not entrada:
    motivos.append("No tienes entrada.")

if not vestimenta:
    motivos.append("No llevas la vestimenta apropiada.")


if len(motivos) == 0:
    print("\nPuedes entrar. ¡Bienvenido!")
else:
    print("\nNo puedes entrar por los siguientes motivos:")
    
    for motivo in motivos:
        print("- " + motivo)