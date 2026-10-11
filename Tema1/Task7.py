#Task7
def elliptic_curve(x,y):
    return (y**2)%9739==(x**3+497*x+1768)%9739
px=8045
py=6936
print(elliptic_curve(px,py))
qx=px
qy=-py
print(elliptic_curve(qx,qy))
#-6936 nu este un numar de la 0 la 9739, folosim modulo ca sa il aducem aici
qy_nou=qy%9739

print(elliptic_curve(qx,qy_nou))
print(qx, qy_nou)

