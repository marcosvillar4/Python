# ---------------------------------------------

def mateo(texto, texto2, texto3):

    # Codigo a ejecutar de la funcion

    print(texto, texto2 + texto3)


# ---------------------------------------------

def multiplicar(nro1, nro2):

    respuestaFunc = nro1 * nro2
    


    return respuestaFunc


def busquedaSecuencial(lista, valor):
    
    for i in range(0, len(lista)):
        
        if lista[i] == valor:
            posicion = i
            return posicion
        
        
        
    return -1

# ---------------------------------------------
def main():
    #var1 = mateo([1,2,3,4], 10, 20)
    #respuesta = multiplicar(multiplicar(10, 2),10) # Ejecutar la funcion   -----> funcion -----> procesar ------>  devolver a respuesta
    #print(var1)
    lista = [1,2,3,10,25,4,5,2,4]
    val = 0

    print(val)
    val = busquedaSecuencial(lista, 254)



    print("Index encontrado: ", val)


# ---------------------------------------------



main()



