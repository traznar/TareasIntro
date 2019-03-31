#Ejercicio1 Resive un numero entero y devuelve los numeros pares en una lista
def listapares(num):
    if isinstance (num,int) and (num>0):
        return listapares2(num)
    else:
        return "Error no es un numero entero mayor a cero"

def listapares2(num):
    if num==0:
        return []
    elif (num%10)%2==0:
        return listapares2(num//10)+[num%10]
    else:
        return listapares2(num//10)
#Ejercicio2 Resive un numero entero y dice si es palindromo o no

    
def palindromo(num):
    if isinstance(num,int) and num>0:
        return palin2(num,num,contador(num,0))
    else:
        return "Error no es un entero"
def palin2(num,num1,cont):
    if num==0:
        return True
    elif num%10==(num1//(10**(cont-1))):
        return  palin2(num//10,num1%(10**(cont-1)),cont-1)
    else:
        return False
def contador(num,contar):
    if num==0:
        return 0
    elif num>0:
        return (contar+1)+contador(num//10,contar)
    else:
        return 
#Ejercicio3 Resive una palabra y dice cuantas consonantes tiene

    
def contarconsonantes(cadena):
    if isinstance (cadena,str):
        return contarconsonantes2(cadena)
    else:
        return "ERROR NO SON CADENAS"
def contarconsonantes2(cadena):
    if len(cadena)==0:
        return 0
    elif cadena[0]=='a':
        return contarconsonantes2(cadena[1:])
    elif cadena[0]=='e':
        return contarconsonantes2(cadena[1:])
    elif cadena[0]=='i':
        return contarconsonantes2(cadena[1:])
    elif cadena[0]=='o':
        return contarconsonantes2(cadena[1:])
    elif cadena[0]=='u':
        return contarconsonantes2(cadena[1:])
    elif cadena[0]=='U':
        return contarconsonantes2(cadena[1:])
    elif cadena[0]=='O':
        return contarconsonantes2(cadena[1:])
    elif cadena[0]=='I':
        return contarconsonantes2(cadena[1:])
    elif cadena[0]=='E':
        return contarconsonantes2(cadena[1:])
    elif cadena[0]=='A':
        return contarconsonantes2(cadena[1:])
    else:
        return contarconsonantes2(cadena[1:])+1
    
#Ejercicio4 Resive una lista de numeros  e intercambia las posiciones con indices pares a las imparesy viceversa

    
def intercambia(num):
    if isinstance (num,list) and (len(num)%2==0):
        return intercambio2(num)
    else:
        return "No es un lista o la cantidad de elementos de la lista es impar"

def intercambio2(num):
    if num==[]:
        return []
    else:
        return [num[1],num[0]]+intercambio2(num[2:])

