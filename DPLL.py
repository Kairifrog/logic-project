from random import choice
from copy import deepcopy

def complemento(l):
    if '-' in l:
        return l[1:]
    else:
        return '-' + l

def simplificar(S, l):

    complement = complemento(l)
    Sp = deepcopy(S)
    Sp = [c for c in Sp if l not in c]
    for c in Sp:
        if complement in c:
            c.remove(complement)
    return Sp

def aumentar_dict(I, l):

    Ip = deepcopy(I)
    complement = complemento(l)
    if '-' not in l:
        Ip[l] = 1
    else:
        Ip[complement] = 0
    return Ip

def unit_propagate(S, I):

    while [] not in S:
        unit = ""
        for x in S:
            if len(x) == 1:
                unit = x[0]
                break
        if len(unit) == 0:
            break
        S = simplificar(S, unit)
        I = aumentar_dict(I, unit)
    return S, I

def dpll(S, I):

    S, I = unit_propagate(S, I)

    if len(S) == 0:
        return "Satisfacible", I
    if [] in S:
        return "Insatisfacible", {}

    literal = choice(choice(S))
    complement = complemento(literal)
    newS = simplificar(S, literal)
    newI = aumentar_dict(I, literal)
    sat, newI = dpll(newS, newI)
    if sat == "Satisfacible":
        return sat, newI
    else:
        newS = simplificar(S, complement)
        newI = aumentar_dict(I, complement)
        return dpll(newS, newI)
