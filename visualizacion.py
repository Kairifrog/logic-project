import  numpy as np
import matplotlib.pyplot as plt

class crearTablero:
    def __init__(self):
        
        self.n=5
        self.coordenadas = []

        #CREAR CARACTERISTICAS DEL TABLERO
        self.tablero = np.zeros((5,5), dtype = int)
        self.tablero[::2, 1::2] = 1
        self.tablero[1::2, ::2] = 1

        #INICIALIZAR MODULOS 
        self.MatrizValues()
        
    def MatrizValues(self):
        self.coordenadas = [] #Guardar posicion (i,j) y el valor VI((i,j)) = 1 o 0
        sublista = [] 
        dic = {} 

        for i in range(self.n): # 0 - 5
            for j in range(self.n): #0 - 5 
                dic[i, j] = 0 #cordenadas tipo (i,j) con valor inicial = 0
                sublista.append(dic) 
                dic = {} 
            self.coordenadas.append(sublista) #agragar a COORDENADAS la lista para la matrix
            sublista = [] 

        self.coordenadas = np.array(self.coordenadas)
    def checkValues(self):
        for fila in range(self.n): 
            for elementos in range(self.n): 
                if self.coordenadas[fila,elementos][fila,elementos] == 1 : #Si en la coordenada el VI = 1 
                    self.tablero[fila,elementos] = 2 #Cambie la matrix tablero para mostrar

    def changeValue(self,x,y):
        try:
            self.coordenadas[x,y][x,y] = 1
        except IndexError:
            print("ERROR!! al ingresar:(",x,",",y,") Ingrese la coodernada teniendo encuenta que su tablero es de " , self.n ,"x", self.n)
        self.checkValues()

    def ShowTab(self):
        plt.imshow(self.tablero, cmap ='gray')
        plt.axis()
        plt.show()
