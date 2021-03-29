"""BOIN Erwan - SERRE Antonn- 1PV2
Analyse numerique - TP2"""

import math

#Equation 1
def g1plus(x):
    return (9-3*x)**0.25
def g1moins(x):
    return -(9-3*x)**0.25

#Equation 2
def g2alpha(x):
    return math.acos((x+2)/3)
def g2beta(x):
    return -(math.acos((x+2)/3))

#Equation 3
def g3(x):
    return math.log(7/x)

#Equation 4
def g4alpha(x):
    return math.log(10+x)
def g4beta(x):
    return math.exp(x)-10

#Equation 5
def g5(x):
    return math.atan((x+5)/2)

#Equation 6
def g6(x):
    return math.log(x**2+3)

#Equation 7
def g7(x):
    return (7-4*math.log(x))/3

#Equation 8
def g8alpha(x):
    a=2*x**2-4*x+17
    return a**0.25
def g8beta(x):    
    return -((2*x**2)-4*x+17)**0.25

#Equation 9
def g9(x):
    return math.log(2*math.sin(x)+7)

#Equation 10
def g10(x):
    return math.log((10)/math.log(x**2+4))


#Code Question 1
def PointFixe (g, x0, epsilon, Nitermax):
    xold = x0
    xnew = g(xold)
    erreur = xnew - xold
    xold = xnew
    n = 1
    while abs(erreur) > epsilon and n < Nitermax : 
        xnew = g(xold)
        erreur = xnew - xold 
        xold = xnew
        n = n+1
    return xnew, n 

#Resultats methode point fixe
print("Equation 1: f(x)=0 avec environ x=",PointFixe(g1plus, 1.5, 1e-3, 5e4),"iterations.")
print("Equation 1: f(x)=0 avec environ x=",PointFixe(g1moins, -1.5, 1e-3, 5e4),"iterations.\n")
print("Equation 2: f(x)=0 avec environ x=",PointFixe(g2alpha, 0.3, 1e-3, 5e4),"iterations.")
print("Equation 2: f(x)=0 avec environ x=",PointFixe(g2beta, -1.9, 1e-3, 5e4),"iterations.\n")
print("Equation 3: f(x)=0 avec environ x=",PointFixe(g3, 1.5, 1e-3, 5e4),"iterations.\n")
print("Equation 4: f(x)=0 avec environ x=",PointFixe(g4alpha, 2.5, 1e-3, 5e4),"iterations.")
print("Equation 4: f(x)=0 avec environ x=",PointFixe(g4beta, -9.8, 1e-3, 5e4),"iterations.\n")
print("Equation 5: f(x)=0 avec environ x=",PointFixe(g5, 1.5, 1e-3, 5e4),"iterations.\n")
print("Equation 6: f(x)=0 avec environ x=",PointFixe(g6, 1.9, 1e-3, 5e4),"iterations.\n")
print("Equation 7: f(x)=0 avec environ x=",PointFixe(g7, 1.8, 1e-3, 5e4),"iterations.\n")
print("Equation 8: f(x)=0 avec environ x=",PointFixe(g8alpha, 2.5, 1e-3, 5e4),"iterations.")
print("Equation 8: f(x)=0 avec environ x=",PointFixe(g8beta, -2.5, 1e-3, 5e4),"iterations.\n")
print("Equation 9: f(x)=0 avec environ x=",PointFixe(g9, 1.2, 1e-3, 5e4),"iterations.\n")
print("Equation 10: f(x)=0 avec environ x=",PointFixe(g10, 1.3, 1e-3, 5e4),"iterations.\n")

