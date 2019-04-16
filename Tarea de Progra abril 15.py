class BuscarBin(object):
    def __init__(self):
        pass
    def busqueda(self,lista,numero):
        if isinstance(lista, list):
            return self.busqueda2(lista,numero,1,len(lista))
        else:
            return "Error, no es una lista"
    def busqueda2(self,lista,numero,inicio,fin):
        if fin < inicio :
            return False
        mitad = (inicio + fin)//2
        if lista[mitad] == numero:
            return mitad
        elif lista[mitad] < numero:
            return self.busqueda2(lista, numero, mitad - 1, fin)
        else:
            return self.busqueda2(lista, numero, inicio, mitad-1)
        
    
