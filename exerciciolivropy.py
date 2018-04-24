def questao1():
    return(5**2,9*5,15/12,12/15,15//12,12//15,5%2,9%5,15%12,12%15,6%6,0%7)

def questao2(h):
    hora = 51/24
    resto = hora+2
    return resto

def questao3():
    hatual = float(input('Hora atual: '))
    esperar = float(input('Horas que deve esperar: '))
    v = (hatual+ esperar)%24
    print('O alarme irá tocar as {} horas.'.format(v))
     
    
def questao5():
    a = str('Só')
    b = str('trabalho')
    c = str('sem')
    d = str('diversão')
    e = str('faz')
    f = str('de')
    g = str('João')
    h = str('um')
    i = str('chato.')
    print('{} {} {} {} {} {} {} {} {}'.format(a,b,c,d,e,f,g,h,i))
    
def questao6():
    a = 6* (1-2)
    return a

def questao7(t):
    a = 10000*(1+(0.08/12))**(12*t)
    return (a)

def questao8(a):
    return(a**2)* 3.14159
     
def questao9(a,b):
     return (a*b)
        
def questao10(km,l):
    return (km/l)
    
def questao11(c):
    return (c*1.8) + 32
     
def questao12(f):
    return ( f - 32) / 1.8
    




