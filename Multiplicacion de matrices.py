class Composicion(object):
    def __init__(self):
        pass
    def Multipl(self, Matriz1,Matriz2):
        if isinstance (Matriz1,list) and isinstance (Matriz2, list):
            return self.Multiplicar(Matriz1,Matriz2,0,0,0,0,[[]],0)
        else:
            return "Error no es una matriz"
        

    def Multiplicar(self,Matriz1,Matriz2,Fila1,Fila2,Col1,Col2,resultado,Mat):
        if len(resultado)*len(resultado[1]) == (len(Matriz1))*(len(Matriz2[0])):
            return resultado
        elif Col1 == len(Matriz1[0]) and Fila2== len(Matriz2):
            return self.Multiplicar(Matriz1,Matriz2,0,0,0,0,resultado+[Mat],0)
        else:
            return self.Multiplicar(Matriz1,Matriz2,Fila1,Fila2+1,Col1+1,Col2,resultado,Mat+(Matriz1[Fila1][Col1]*Matriz2[Fila2][Col2]))

