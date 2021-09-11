class Matriz:
    def __init__(self,matriz,nfilas,ncol):
        self.Matriz=matriz
        self.Nfilas=nfilas
        self.NCol=ncol
        
        
    def mayor(self):
        mayor=0
        for fil in range(len(self.Matriz)):
            for col in range(len(self.Matriz)):
                if self.Matriz[fil][col] > mayor:
                    mayor = self.Matriz[fil][col]
        return mayor
    
# numeros=[[-11,-20,15],[-10,-40,30],[11,25,31]]
# mat1=Matriz(numeros,3,3)
# print(mat1.mayor())


class Pila:
    def __init__(self):
        self.items=[]
        
    def mayor(self):
        return self.items==[]
        
    def incluir (self,items):
        self.items.append(items)
        
    def extraer (self):
        return self.items.pop()
    
    def inspeccionar(self):
        print(self.items(len(self.items)-1))

pila = Pila()
pila.incluir("Danny")
pila.incluir("Yady")
pila.incluir("Romina")
pila.incluir("Dayana")
pila.extraer()
pila.incluir("Alex")
pila.extraer()
pila.inspeccionar()