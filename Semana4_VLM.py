def volviendo():
    return print("Volviendo al inicio...")
    
def descuento_mayorista():
    base = 40
    try:
        descuento = 0
        articulos = int(input("ingrese la cantidad de articulos a comprar: "))
        if articulos < 0:
            print("La cantidad de articulos no puede ser negativa.")
            volviendo()
            return
        if articulos >= 20:
            descuento = 0.25
        elif articulos >= 10: 
            descuento = 0.15
        else: 
            descuento = 0
        
        
        sin_descuento = base * articulos
        descuento_base = base - (base * descuento)
        total = descuento_base * articulos
        print(f"El total de articulos comprados es: {articulos}")
        print(f"Valor de productos sin descuento: ${sin_descuento}")
        if descuento > 0:
            print(f"El descuento aplicado es de: {descuento * 100:g}%")
            print(f"El valor base con descuento aplicado es de: ${descuento_base:g}")
        print(f"El valor total de la compra es: ${total:g}")
    except ValueError:
        print("Error: Ingrese un numero válido de articulos")
        volviendo()
        return
    
def alc():
    try:
        radio = float(input("Ingrese radio del cilindro: "))
        altura = float(input("Ingrese altura del cilindro: "))
        if radio < 0 or altura <0:
            print("Error: Radio y altura deben ser positivos.")
            return
        
        pi = 3.14
        arealc= 2*pi*radio*altura
        print(f"Radio de cilindro: {radio}")
        print(f"Altura de cilindro: {altura}")
        print(f"El area de superficie lateral del cilindro es: {arealc:.2f}")
    except ValueError:
        print("Ingrese numeros validos")
        
        return

#Funcion para crear menú usando bucle while True
def menu():
    while True:
        print("""    _____________________________________________________________
    |    ---BIENVENIDO---                                        |
    |    Seleccione una opción:                                  |
    |    1. Calcular descuento por compra mayorista              |
    |    2. Calcular area de superficie lateral de un cilindro   |
    |    3. Salir                                                |      
    |____________________________________________________________|""")
        
        opcion = input("Ingrese que desea realizar: ")
        if opcion == "1":   
            descuento_mayorista()   #Opcion 1 invoca funcion para los descuentos
        elif opcion == "2":
            alc()                   #Opcion 2 invoca funcion para el area del cilindro.
        elif opcion == "3":
            print("¡Adios!")        #Opcion 3 detiene el bucle while para salir del programa.
            break
        else:                       #cualquier otra opción que ingrese el usuario vuelve al inicio del bucle.
            print("Error: Ingrese una opcion valida, entre el 1 y el 3.")

#Se inicializa el codigo invocando la función menu con el bucle while.
menu()