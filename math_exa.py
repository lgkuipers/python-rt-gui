from math import *

def xy2alphabeta(x, y):

    l=80.0
    m=80.0
    z=sqrt(pow(x,2) + pow(y,2))

    abc = degrees(acos((-pow(l,2) + pow(m,2) + pow(z,2))/(2*m*z)))
    bac = degrees(acos((-pow(m,2) + pow(l,2) + pow(z,2))/(2*l*z)))
    bad = degrees(atan(y/x))
    acb = 180.0 - abc - bac

    beta = 180.0 - bac - bad
    alpha = 180.0 - bac - bad - acb

    return alpha, beta

def alphabeta2JK(alpha, beta):
    k_float = - 4.64 * alpha + 438
    j_float = 4.05 * beta - 321.2
    j = int(j_float)
    k = int(k_float)
    return j, k

x_str = input("X>")

while x_str != "":

    y_str = input("Y>")

    #x = 64.0
    #y = 16.0

    x = float(x_str)
    y = float(y_str)

    alpha, beta = xy2alphabeta(x, y)

    print("---")
    print(alpha)
    print(beta)

    j, k = alphabeta2JK(alpha, beta )

    print("---")
    print(j)
    print(k)

    x_str = input("X>")
