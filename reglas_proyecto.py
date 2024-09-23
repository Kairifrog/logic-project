
class objetoCodificacion2D :

    def __init__ (self,Nfilas,Ncolumnas,chrInit) :
        self.Nf = Nfilas
        self.Nc = Ncolumnas
        self.chrInit = chrInit

    def codifica(self,f,c) :
        return self.Nc * f + c

    def decodifica(self,n):
        f = int(n / self.Nc)
        c = n % self.Nc
        return f, c

    def P(self,f,c) :
        codigo = self.codifica(f,c)
        return chr(self.chrInit+codigo)

    def Pinv(self,codigo) :
        n = ord(codigo)-self.chrInit
        return self.decodifica(n)

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
        f,c = cods.Pinv(f.label)
        return f"P({f},{c})"
    elif f.label == '-':
        return f.label + Inorderp(f.right)
    else:
        return "(" + Inorderp(f.left) + f.label + " " + Inorderp(f.right) + ")"

def inorder(A) :
    if A.right == None:
        return A.label
    elif A.label == '-':
        return '-' + inorder(A.right)
    elif A.label in ['Y', 'O', '>', '=']:
        return "(" + inorder(A.left) + A.label + inorder(A.right) + ")"

letrasProposicionales = [chr(x) for x in range(256,600)]
conectivos = ["Y", "O", ">", "="]

# Crea las columnas del tablero a modo de formula
def cuadros(f):
    inicial=True
    for x in range(cods.Nc):
        if inicial:
            formula=cods.P(f, x)
            inicial=False
        else:
            formula=cods.P(f, x) + formula + "O"
    return formula

# Tablero
def regla1():
    inicial=True
    for f in range(cods.Nf):
        if inicial:
            formula=cuadros(f)
            inicial=False
        else:
            formula= cuadros(f) + formula + "Y"
    return formula


def no_f(f, c):
    inicial=True
    rango = [x for x in range(cods.Nf) if x != c]
    for x in rango:
        if inicial:
            formula = cods.P(f, x)
            inicial = False
        else:
            formula = cods.P(f, x) + formula + "O"

    return formula + "-" + cods.P(f, c) + ">"

#No puede haber mas de una torre por fila 

def regla2():
    inicial = True
    for f in range(cods.Nf):
        for c in range(cods.Nc):
            if inicial:
                formula=no_f(f, c)
                inicial=False
            else:
                formula=no_f(f, c) + formula + "Y"
    return  formula

def no_c(f, c):
    inicial = True
    rango = [x for x in range(cods.Nc) if x != f]
    for x in rango:
        if inicial:
            formula = cods.P(x, c)
            inicial = False
        else:
            formula = cods.P(x, c) + formula + "O"

    return formula + "-" + cods.P(f, c) + ">"

#No puede haber mas de una torre por columna

def regla3():
    inicial = True
    for f in range(cods.Nf):
        for c in range(cods.Nc):
            if inicial:
                formula = no_c(f, c)
                inicial = False
            else:
                formula = no_c(f, c) + formula + "Y"
    return  formula

def rules():
    global Ncolumnas, Nfilas
    global cods
    Ncolumnas = Nfilas = 5
    cods = objetoCodificacion2D(Nfilas,Ncolumnas,256)
    R1 = regla1()
    R2 = regla2()
    R3 = regla3()


    return R1 + R2 + "Y" + R3 + "Y"

def num():
    return Ncolumnas
