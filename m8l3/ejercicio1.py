# Yo aqui remplazaria los nombres de lass variables l1, l2 y l3 para que hagan mas sentido a lo que verdaderamente se refiere.
# agrego un import time para el break del loop.

import time

#aqui pienso que seria mejor agregar en el print del menu que estamos buscando y tambien hacer que la lista no se vea tan complicada y salga sin los [] y las comas, para que sea mas facil de leer.
articulos = ["Perro-Adulto", "Gato-Kitten", "Arena-Premium"]
stock = [10, 5, 20]
precios = [80000, 45000, 30000]
def menu():
    print("Artículos:", ", ".join(articulos))
    print("Stock:", ", ".join(map(str, stock)))
    print("Precios:", ", ".join(map(str, precios)))
def compra():
    global stock
#yo invocaria claridad con las variables para saber que se esta piediendo en compra()
    articulo = input("Ingrese el artículo que desea comprar: ")
    cantidad = int(input("Ingrese la cantidad que desea comprar: "))
    for i in range(len(articulos)):
        if articulos[i] == articulo:
            stock[i] = stock[i] - cantidad
            #aqui yo agregaria un mensaje para que el usuario sepa que su compra se realizo y cuanto stock queda del articulo que compro.
            print("Compra realizada. Compraste", cantidad, "de", articulo, ". Stock restante:", stock[i])

# cambiaria la x a "orden" ,ya que es lo que el usuario escribe para elegir que quiere ejecutar. Tambien un mensaje de bienvenida a la tienda.
# escribo una mensaje en el imput para que el usuario sepa que tiene que ingresar para ejecutar su opcion.
print("¡Bienvenido a la tienda de mascotas!")
while True:
    orden = input("Ingrese la opción que desea ejecutar = 1 - menu, 2 - compra, 3 - salir: ")
    if orden == "1":
        menu()
    elif orden == "2":
        compra()
    elif orden == "3":
# esta muy bien este comando de salida, pero para que el usuario sepa que salio, agrego el print del mensaje de salida y el tiemppo
        print("Saliendo de la tienda...")
        time.sleep(2)
        break