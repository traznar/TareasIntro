#Ejercicio1
def multipliqueind(num):
    if isinstance (num,list):
        return multiind(num,0)
    else:
        return "Error no es una lista"
def multiind(num,ind):
    if num==[]:
        return []
    else:
        return [num[0]*ind]+multiind(num[1:],ind+1)
#Ejercicio 2
def sumatoria(num):
    if isinstance(num,list):
        return sumatoria1(num,1)
    else:
        return "Error no es una lista"
def sumatoria1(num,suma):
    if num==[]:
        return 0
    elif isinstance(num[0],list):
        return sumatoria1(num[0]+num[1:],suma)
    else:
        return num[0]**suma+sumatoria1(num[1:],suma+1)
#Ejercicio 3 Examen 3 Sumatoria y Productoria
    

#Ejercicio 4 Exammen 3 Darle vuelta a los pares de numeros
def reversa(num):
    if isinstance(num,int) and num>0 and (contar(num,0))%2==0:
        return reversadoble(num,2,contar(num,0))
    else:
        return "Error no es un entero o la cantidad de digitos no es par"
def reversadoble(num,cont,n):
    if num==0:
        return 0
    else:
        return (((num%100)%10)*10**(cont-1))+(((num%100)//10)*10**(cont-2))+reversadoble(num//100,cont+2,n)
def contar(num,contar1):
    if num==0:
        return 0
    else:
        return (contar1+1)+ contar(num//10,contar1)
