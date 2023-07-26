def Crear_lista():
    lista=[]
    entrada=''
    while entrada!=0:
        entrada=float(input("Ingrese los Kg de fuerza que aguanta esta pieza (Para finalizar ingrese el numero 0): "))

        if entrada<0:
            print("Lo sentimos, ese valor no es valido, por favor intente con otro: ")
            entrada=float(input("Ingrese los Kg de fuerza que aguanta esta pieza (Para finalizar ingrese el numero 0): "))

        elif entrada in lista:
            print("Esa pieza ya ha sido registrada, coloque una distinta")
            entrada=float(input("Ingrese los Kg de fuerza que aguanta esta pieza (Para finalizar ingrese el numero 0): "))

        if entrada!=0:
            lista.append(entrada)
    return lista


def ordenar_creciente(lista2):
    ordenada1=list(lista2)
    intercambio=True

    while intercambio:
        intercambio=False
        for i in range(len(lista2)-1):
            if ordenada1[i]>ordenada1[i+1]:
                ordenada1[i],ordenada1[i+1]=ordenada1[i+1],ordenada1[i]
                intercambio=True
    return ordenada1

def ordenar_decreciente(lista3):
    ordenada=list(lista3)
    intercambio=True

    while intercambio:
        intercambio=False
        for i in range(len(ordenada)-1):
            if ordenada[i]<ordenada[i+1]:
                ordenada[i],ordenada[i+1]=ordenada[i+1],ordenada[i]
                intercambio=True
    return ordenada



def determinar_mas_debil(lista4):
    mas_Debil=ordenar_creciente(list(lista4))[0]
    return mas_Debil

def contar_resistentes(lista5):
    contadora=0
    for i in lista5:
        if i>300:
            contadora=contadora+1
    return contadora

lista=Crear_lista()


ordenado_en_creciente=ordenar_creciente(lista)
ordenado_en_decreciente=ordenar_decreciente(lista)
mas_debil=determinar_mas_debil(lista)
Cantidad_de_resistencias_aptas=contar_resistentes(lista)

print("---------------------------")
print("Las resistencias ordenadas de menor a mayor son:")
print(ordenado_en_creciente)

print("")

print("Las resistencias ordenadas de mayor a menor son:")
print(ordenado_en_decreciente)

print("")
print("La resistencia mas debil es la de: ")
print(mas_debil)

print("")
print("La cantidad de resistencias aptas para automoviles son: ")
print(Cantidad_de_resistencias_aptas)