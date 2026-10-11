#Task8
O=None
a=497
p=9739
def add(P,Q):
    if P==O:
        return Q
    if Q==O:
        return P
    xp, yp=P
    xq, yq=Q
    if xp==xq and yp%p==-yq%p:
        return O
    else:
        if P!=Q:
            lamda=(yq-yp)*pow(xq-xp, -1, p)
        else:
            lamda=(3*xp**2+a)*pow(2*yp,-1,p)
    x3=(lamda**2-xp-xq)%p
    y3=(lamda*(xp-x3)-yp)%p
    punct=(x3,y3)
    return punct

def elliptic_curve(x,y):
    return (y**2)%9739==(x**3+497*x+1768)%9739
px=8045
py=6936

print(add((5274,2841), (8669,740)))
print(add((5274,2841), (5274,2841)))

P=(493,5564)
Q=(1539,4742)
R=(4403,5202)
suma1=add(P,P)
suma2=add(suma1, Q)
suma3=add(suma2, R)
print(suma3)