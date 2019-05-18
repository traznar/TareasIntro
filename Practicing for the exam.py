##II Examen Parcial
#Primer Ejercicio
class sumaMatrix(object):
    def __init__(self):
        pass
    def sumaMM(self,m1,m2):
        if isinstance (m1,list) and (m2,list):
            return self.sumalas(m1,m2,0,0,[],[])
        else:
            return "Error no es una lista o sumaMM"
    def sumalas(self,m1,m2,f,c,R,Mat):
        if len(m1) and len(m2)== f:
            return Mat
        elif len(m1[0]) and len(m2[0])==c:
            return self.sumalas(m1,m2,f+1,0,[],Mat+[R])
        else:
            return self.sumalas(m1,m2,f,c+1,R+[m1[f][c]+m2[f][c]],Mat)
    def Mfunciones(self,M):
        if isinstance(M,list):
            return self.sumaExt(M,-1,0,0),self.sumaColum(M,0,0,0),self.anti(M,0,len(M[0])-1,0),(self.sumaExt(M,-1,0,0)+self.sumaColum(M,0,0,0)+self.anti(M,0,len(M[0])-1,0))
        else:
            return "Error"
    def sumaExt(self,M,F,C,R):
        if len(M)==F:
            return R
        elif len(M[0])==C:
            return self.sumaExt(M,F+1,0,R)
        elif F==0 or F==len(M)-1:
            return self.sumaExt(M,F,C+1,R+M[F][C])
        else:
            return self.sumaExt(M,F,C+1,R)
    def sumaColum(self,M,F,C,R):
        if len(M)==F:
            return R
        elif len(M[0])==C:
            return self.sumaColum(M,F+1,0,R)
        elif len(M[0])-1==C or C==0:
            return self.sumaColum(M,F,C+1,R+M[F][C])
        else: return self.sumaColum(M,F,C+1,R)
    def anti(self,M,F,C,R):
        if len(M)==F:
            return R
        else:
            return self.anti(M,F+1,C-1,R+M[F][C])
##Segundo Ejercicio
class stats(object):
    def __init__(self):
         pass
    def stats2(self,M):
        if isinstance(M,list) and M!=[]:
            return self.prome(M,0,0,0),self.sacar(M,[])
        else:
            return "error"
    def prome(self,M,F,C,R):
        if len(M)==F:
            return R/len(M[0])
        else:
            return self.prome(M,F+1,C+1,R+M[F][C])
    def sacar(self,M,r):
        if M==[]:
            return self.Mediana(r,0)
        else:
            return self.sacar(M[1:],r+M[0])
        
    def Mediana(self,r,R):
        if R!=0:
           return R
        elif len(r)%2==0:
            return self.Mediana(r,R+(r[len(r)//2]+r[(len(r)//2)-1])/2)
        else:
            return self.Mediana(r,R+((r[(len(r)//2)])/2))
##Tercer Ejercicio
class Ecuac(object):
    def __init__(self):
        pass
    def Ecuaciones(self,b,c):
        if isinstance(b,int) and (c,int):
            return self.Multiplos(c,c,c,[],b)
        else: return "Error"
    def Multiplos(self,c,c1,c2,lista,b):
        if c==0:
            return self.Multipli(lista,0,0,c2,b,[])
        else:
            return self.Multiplos(c-1,c1,c2,lista+[(c1//c-1)+1],b)
    def Multipli(self,lista,Ind1,Ind2,c2,b,R):
        if R!=[]:
            return R
        elif len(lista)==Ind2:
            return self.Multipli(lista,Ind1+1,0,c2,b,R)
        elif lista[Ind1]*lista[Ind2]==c2 and lista[Ind1]+lista[Ind2]==b:
            return self.Multipli(lista,Ind1,Ind2,c2,b,(lista[Ind1],lista[Ind2]))
        else:
            return self.Multipli(lista,Ind1,Ind2+1,c2,b,R)
##Cuarto Ejercicio
class Notacion(object):
    def __init__(self):
        pass
    def Cientifica(self,Num):
        if isinstance(Num,int) or (Num,float):
            return self.Contador(Num,Num,0,0)
        else:
            return "Error"
    def NotCien(self,Num2,Ind1,Ind2,R):
        if R!=0:
            return R
        elif Num2//(Ind1+Ind2-1)==0:
            return self.NotCien(Num2,Ind1,Ind2,((Num2%10**Ind2),("x10"),("**"),(-Ind1)))
        else:
            return self.NotCien(Num2,Ind1,Ind2,((Num2//10**Ind1),("x10"),("**"),(Ind1)))
    def Contador(self,Num,Num2,Ind1,Ind2):
        if Num==0:
            return self.NotCien(Num2,Ind1,Ind2,0)
        elif Num%10==0:
            return self.Contador(Num//10,Num2,Ind1+1,Ind2)
        else:
            return self.Contador(Num//10,Num2,Ind1,Ind2+1)
