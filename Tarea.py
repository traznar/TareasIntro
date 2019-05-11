class MULTIPLICACION(object):
    def __init__(self):
        pass
    def MATRICES(self,Matriz1,Matriz2):
        if isinstance(Matriz1,list) and Matriz1!=[] :
            return self.multipli(Matriz1,Matriz2,0,0,0,0,0)
    def multipli(self,Matriz1,Matriz2,indice,F,C,matrix,result):
        if indice == len(Matriz1):
            return matrix
        elif F==len(Matriz1[0]):
            return self.multipli(Matriz1,Matriz2,indice+1,0,0,matrix,0)
        elif C==len(Matriz1[0]):
            matrix[indice][F]= result
            return self.multipli(Matriz1, Matriz2, indice, F+1, 0, matrix, 0)
        else:
            result+= Matriz1[indice][C]*Matriz2[C][F]
            C+=1
            return self.multipli(Matriz1,Matriz2,indice, F, C, matrix, result)

