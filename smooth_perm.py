from math import *
from itertools import *


def list_index_increasing(L):
    """
    L : List(Integers)
    return [i_1, ... , i_k] such that [L[i_1], ... , L[i_k]] is sorted
    """
    Ls = sorted(L)
    return [L.index(Ls[i])+1 for i in range(len(Ls))]


def avoidance(w,v):
    """
    w in Sl and v in Sk with k<=l given w = [w(1), ..., w(l)], v = [v(1), ..., v(k)]
    Return True if w avoids v, False otherwise
    """
    l = len(v)
    K = [i+1 for i in range(len(w))]
    for C in combinations(K, l):
        wC = [w[i-1] for i in list(C)]
        if list_index_increasing(wC) == v: # same relative order
            return False     
    return True

def number_smooth_permutation(n):
    """
    return the number of smooth Schubert varieties for the Bruhat decomposistion of SLn
    (Weyl group of type A) with 3412 and 4231 avoidance
    """
    K = [i+1 for i in range(n)]
    Sn = list(permutations(K))
    return sum([1 for s in Sn if avoidance(s,[3,4,1,2]) and avoidance(s,[4,2,3,1])])