from mpl_toolkits.mplot3d import Axes3D
from matplotlib.pyplot import title,figure,show,plot,legend
from numpy import linspace,sin,cos,pi

#declara la grafica en 3d
a=figure()
a.gca(projection="3d")

#calculo de teta
teta=linspace(-4*pi, 4*pi,100)

#calculo de r
r=linspace(0,pi,100)

#calculo del comportamiento de la curva
z=r
x= r*sin(teta)
y=r*cos(teta)


#muestra la grafica y sus propiedades
plot(x,y,z, label="Curva parametrica")
legend()
show()
