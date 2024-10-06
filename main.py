#Lista de nombres
nombres = [
    "Harry Houdini", "Newton", "David Blaine", "Hawking", "Messi", "Teller", "Einstein", "Pele", "Juanes"
]

#Listas específicas
magos = ["Harry Houdini", "David Blaine", "Teller"]
cientificos = ["Newton", "Hawking", "Einstein"]
otros = []

#Funcíón para hacer grandioso
def hacer_grandioso(magos):
    for i in range(len(magos)):
        magos[i] = f"El gran {magos[i]}"

#Función para imprimir nombres
def imprimir_nombres(titulo, lista):
    print(f"\n{titulo}")
    for nombre in lista:
        print(nombre)

#Bucle para recorrer lista de nombres y agregar sólo a "otros"
for nombre in nombres:
    if nombre not in magos and nombre not in cientificos:
        otros.append(nombre)

#Llamo a la función "hacer_grandioso" para que se apliquen los cambios antes de imprimir
hacer_grandioso(magos)

#Imprimir listas
imprimir_nombres("Nombres originales:", nombres)
imprimir_nombres("Magos grandiosos:", magos)
imprimir_nombres("Científicos:", cientificos)
imprimir_nombres("Otros:", otros)