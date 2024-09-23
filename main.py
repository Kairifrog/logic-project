import reglas_proyecto as pr
import DPLL
import FNC
import visualizacion as vs


def modificaciones():

    letrasproposicionalesA = [chr(x) for x in range(256, 1000)]
    letrasproposicionalesB = [chr(x) for x in range(1001, 20000)]
    formula = pr.rules()
    A = pr.String2Tree(formula)
    inor = pr.inorder(A)
    T = FNC.Tseitin(inor, letrasproposicionalesA, letrasproposicionalesB)
    formaClausal = FNC.formaClausal(T)
    S,I = DPLL.dpll(formaClausal,{})
    
    tableroSolucion = vs.crearTablero()

    for k in I.keys():
        if (k in letrasproposicionalesA) and (I[k] == 1):
            f, c = pr.cods.decodifica(ord(k) - pr.cods.chrInit)
            tableroSolucion.changeValue(f, c)
    tableroSolucion.ShowTab()

def main():
    
    modificaciones()

if __name__ == '__main__':
    main() 