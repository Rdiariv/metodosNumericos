#/usr/bin/python3
#-*- coding: utf-8 -*-
from sympy import *

def biseccion(fun, a, b, tol, N):
    print("Método de la bisección------------------")
    print("Funcion: ",fun)
    print("a0 =",a,"   b0 =",b,"   tolerancia=",tol)
    print("----------------------------------------")
    print("")
    
    x = symbols("x")
    #guardo fun (string) pasandola a expresion sin evaluar, con parse_expr, en funcion
    funcion=parse_expr(fun,evaluate=false)

    inter=1
    i=1
    while inter==1 and i<=N:
        p=(a+b)/2
        #sustituyo la x por el valor de a en funcion y lo evaluo con resultado float
        fa=funcion.subs(x,a).evalf()
        fb=funcion.subs(x,b).evalf()
        fp=funcion.subs(x,p).evalf()
        print("Iteración ",i,"--------------------------------------")
        print("a =",a,"     f(a) =",fa,"\n")
        print("b =",b,"     f(b) =",fb,"\n")
        print("p =",p,"     f(p) =",fp,"\n")
        print("")
        if fp==0 or (b-a)/2<tol:
            inter=0
            print("Éxito tras ",i," iteraciones.\nLa raíz es ",p)
        else:
            if fa*fp>0:
                a=p
            else:
                b=p
        i+=1
    
    #fin del while

    if(inter==1):
        print("El método no ha obtenido éxito tras ",N," iteraciones.") 
#FIN DE BISECCION()        

#def puntoFijo():
    


#fin de funcion punto fijo


#def metodoNewton():

#Fin de método de Newton

biseccion('x**3-10',1,4,0.001,20)