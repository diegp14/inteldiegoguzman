
def suma(arreglo):
    if len(arreglo)== 0:
        return 0
    else:

        aux = arreglo.pop()
        
       # print(arreglo)
        
        aux =aux+ suma(arreglo)
        
        return aux 



def fact(x):
    if x==0:
        return 1
    else:
       aux= x*fact(x-1)
       return aux 


print(fact(2))

def primerParte(numerador, numInteres):
    resNum = fact(numerador)
    facNumInteres = fact(numInteres)
    factNumEnsayo = fact(numerador-numInteres) 
    resDeno = facNumInteres * factNumEnsayo

    return resNum/resDeno

arregloRes = []
def funcionBinomial(numEnsayos, numInteres, exito):
   
    if numInteres>-1:
        fracaso = 1-exito
        
        combinatoria = primerParte(numEnsayos, numInteres)
        exitoElevado = pow(exito, numInteres)
        fracasoElevado = pow(fracaso, numEnsayos-numInteres)
        resultado = combinatoria * exitoElevado * fracasoElevado
        resultado ='{:f}'.format(resultado)
        arregloRes.append(resultado)
        funcionBinomial(numEnsayos, numInteres-1, exito)
        return arregloRes

numeroEnsayos = int(input("Introduce un numero de ensayos:"))
numeroInteres = int(input("Introduce un numero de interes: "))
exito = float(input("Introduce el exito: "))




#print(primerParte(numeroEnsayos, numeroInteres))
print(funcionBinomial(numeroEnsayos,numeroInteres,exito))
res = funcionBinomial(numeroEnsayos,numeroInteres,exito)
#print(suma(res))
#print('{:f}'.format(res.pop(0)))

