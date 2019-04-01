#Tarea Taller
#Brandon Gomez Gomez 2019173506
#Resta de numeros en cualquier base
class resta(object):
    def __int__(self):
        pass
    def resta2(self, num1, num2,base):
        if (isinstance (num1, list) and isinstance (num2, list) and len(num1)==len(num2)):
            return self.resta3(num1,num2,base,0)
        else: return "Error no son listas de igual tamano"

    def resta3(self, num1,num2,base,prestado):
        if num1 == []:
            return []
        elif ((num1[-1]+prestado) - (num2[-1])) > 0:
            return self.resta3(num1[:-1], num2[:-1],base,prestado) + [(num1[-1]) - (num2[-1])]   
        elif ((num1[-1]+prestado) - (num2[-1])) < 0:
            return self.resta3(num1[:-2]+[num1[-2]-1],num2[:-1],base,prestado+1)+ [(num1[-1]+base)-(num2[-1])]
        elif((num1[-1]+prestado) - (num2[-1])) == 0:
            return self.resta3(num1[:-1], num2[:-1],base,prestado)+[0]
