import sympy 


#Ecuaciones Diferenciales de Variables Separables puntos 1-5
def puntose1():
    x = sympy.symbols('x') 
    y = sympy.Function('y')(x)
    ej1 = sympy.Eq(sympy.diff(y, x), y * sympy.sin(x)) 
    rta1 = sympy.dsolve(ej1, y, simplify= False)
    print("Resultado: ")
    sympy.pprint(rta1)

def puntose2():
    x = sympy.symbols('x')
    y = sympy.Function('y')(x)
    ej2 = sympy.Eq(sympy.diff(y, x), y / x)
    rta2 = sympy.dsolve(ej2, y, simplify= False)
    print("Resultado: ")
    sympy.pprint(rta2)

def puntose3():
     x = sympy.symbols('x')
     y = sympy.Function('y')(x)
     ej3 = sympy.Eq(sympy.diff(y,x), y*sympy.exp(x))
     rta3 = sympy.dsolve(ej3, y, simplify=False)
     print("Resultado: ")
     sympy.pprint(rta3)

def puntose4():
    x = sympy.symbols('x')
    y = sympy.Function('y')(x)
    ej4 =sympy.Eq(sympy.diff(y,x), (3*x*y**2))
    rta4 = sympy.dsolve(ej4, y, simplify=False)
    print("Resultado: ")
    sympy.pprint(rta4)

def puntose5():
    x = sympy.symbols('x')
    y = sympy.Function('y')(x)
    ej5 = sympy.Eq(sympy.diff(y,x), (1+x**2)/y)
    rta5 = sympy.dsolve(ej5, y, simplify=False)
    print("Resultado: ")
    sympy.pprint(rta5)

#Ecuaciones Diferenciales Homogeneas 6-0

def puntohom6():
    x = sympy.symbols('x')
    y = sympy.Function('y')(x)
    ej6 = sympy.Eq(sympy.diff(y,x), (2*x+3*y)/(x-y))
    rta6 = sympy.dsolve(ej6, y, simplify=False)
    print("Resultado: ")
    sympy.pprint(rta6)

def puntohom7():
    x = sympy.symbols('x')
    y = sympy.Function('y')(x)
    ej7 = sympy.Eq(sympy.diff(y,x), ((x**2)+ y**2)/(x*y))
    rta7 = sympy.dsolve(ej7, y, simplify=False)
    print("Resultado: ")
    sympy.pprint(rta7)

def puntohom8():
    x = sympy.symbols('x')
    y = sympy.Function('y')(x)
    ej8 = sympy.Eq(sympy.diff(y,x), (y+x)/(x))
    rta8 = sympy.dsolve(ej8, y, simplify=False)
    print("Resultado: ")
    sympy.pprint(rta8)

def puntohom9():
    x = sympy.symbols('x')
    y = sympy.Function('y')(x)
    ej9 = sympy.Eq(sympy.diff(y,x), (x**2 - y**2)/(2*x*y))
    rta9 = sympy.dsolve(ej9, y, simplify=False)
    print("Resultado: ")
    sympy.pprint(rta9)

def puntohom0():
    x = sympy.symbols('x')
    y = sympy.Function('y')(x)
    ej0 = sympy.Eq(sympy.diff(y,x), ((x*y) - (y**2))/(x**2))
    rta0 = sympy.dsolve(ej0, y, simplify=False)
    print("Resultado: ")
    sympy.pprint(rta0)

numero = int(input("escoger un ejercicio a resolver:"))


if numero == 1:
    puntose1()
elif numero == 2:
     puntose2()
elif numero == 3:
    puntose3()
elif numero == 4:
    puntose4()
elif numero == 5:
    puntose5()
elif numero == 6:
    puntohom6()
elif numero == 7:
    puntohom7()
elif numero == 8:
    puntohom8()
elif numero == 9:
    puntohom9()
elif numero == 0:
    puntohom0()
else:
    print("Error")


