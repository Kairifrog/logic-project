
class objetoCodificacion3D :
    
    def __init__ (self,Nf,Nc,Nn,chrInit) :
        self.Nf = Nf
        self.Nc = Nc
        self.Nn = Nn
        self.chrInit = chrInit

    def codifica(self,f,c,n) :
        v1 = self.Nc * f + c
        return self.Nn * v1 + n

    def decodifica(self,codigo):
        n = codigo % self.Nn
        v1 = int(codigo / self.Nn)
        c = v1 % self.Nc
        f = int(v1 / self.Nc)
        return f, c, n
    
    def P(self,f,c,n) :
        codigo = self.codifica(f,c,n)
        return chr(self.chrInit + codigo)
    
    def Pinv(self,codigo) :
        v = ord(codigo)-self.chrInit
        return self.decodifica(v)
Nfilas = 5
Ncolumnas = 5
torres = 4
cods = objetoCodificacion3D(Nfilas,Ncolumnas,torres,256)

letras = []
for n in range(torres):
    print("Torre: "+str(n))
    print("filas x columnas")
    for f in range(Nfilas):
        for c in range(Ncolumnas):
            cod = cods.P(f,c,n)
            
            letras.append(cod)
        



for cod in letras:
    print("n = "+ cod, end = ", ")
    f, c, o = cods.Pinv(cod)
    print ("La Torre " + str(o), end = " ")
    print ("esta en: (Fila " + str(f), end = ", ")
    print ("Columna  " + str(c)+')')

inicial=True
for n in range(4):
    if inicial:
        formula=cods.P(0,0,n)
        inicial=False
    else:
        formula=cods.P(0,0,n)+formula+"O"





class Tree(object):
    def __init__(self, label, left, right):
        self.left = left
        self.right = right
        self.label = label
        
def String2Tree(A):

    pila = []
    for c in A:

        if c in letrasProposicionales:
          
            pila.append(Tree(c, None, None))
        elif c == '-':
           
            formulaAux = Tree(c, None, pila[-1])
            del pila[-1]
            pila.append(formulaAux)
        elif c in conectivos:
        
            formulaAux = Tree(c, pila[-1], pila[-2])
            del pila[-1]
            del pila[-1]
            pila.append(formulaAux)
        else:
            print(u"Hay un problema: el símbolo " + str(c) + " no se reconoce")
    return pila[-1]

def Inorderp(f):
  

    if f.right == None:
        f,c,n = cods.Pinv(f.label)
        return f"P({f},{c},{n})"
    elif f.label == '-':
        return f.label + Inorderp(f.right)
    else:
        return "(" + Inorderp(f.left) + f.label + " " + Inorderp(f.right) + ")"

letrasProposicionales = [chr(x) for x in range(256,600)]
conectivos = ["Y", "O", ">", "="]
A = String2Tree(formula)

#----------------------------------------

inicial = True
rango = [n for n in range(cods.Nn) if n != 0]
for n in rango:
    if inicial:
        formula = cods.P(0,0,n)
        inicial = False
    else:
        formula = cods.P(0,0,n) + formula + "O"
        
formula = formula + "-" + cods.P(0,0,0) + '>'
A = String2Tree(formula)

def no_n(f,c,n):    
    inicial = True
    rango = [z for z in range(cods.Nn) if z != n]
    for z in rango:
        if inicial:
            formula = cods.P(f,c,z)
            inicial = False
        else:
            formula = cods.P(f,c,z) + formula + "O"

    return formula + "-" + cods.P(f,c,n) + '>'


formula = no_n(0,0,1)
A = String2Tree(formula)
print ("regla 1: ")
def regla1():
    inicial = True
    rango = [z for z in range(cods.Nn)]
    rangof = [f for f in range(cods.Nf)]
    rangoc = [c for c in range(cods.Nc)]
    
    for f in rangof:
        for c in rangoc:
            for z in rango: 
                if inicial:
                    formula = no_n(f,c,z)
                    inicial = False
                else:
                    formula = no_n(f,c,z) + formula + "Y" 
    return formula

formula = regla1()
A = String2Tree(formula)
print(Inorderp(A))
print("AQQUIIIIIIIII")

def casilla_negra():
    for c in range (Ncolumnas):
        for f in range (Nfilas):
            casilla=(c+f)%2
            if casilla == 1:
               casillasnegras=(c,f)
               (casillasnegras)
casilla_negra()