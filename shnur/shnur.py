from pygame import *
win_size=[1000,500]
win=display.set_mode(win_size)
clock=time.Clock()
k=10
x0,y0=[50,250]
dx=100
high=[0,50,0]
velocitys=[0,20,0] 
m=[1000,50,1000]
dt=0.01
def change_kubiks(high,velocitys):
    acceleration=[0,0,0]
    acceleration[0]=k/m[0]*(high[1]-high[0])
    acceleration[-1]=k/m[-1]*(high[-2]-high[-1])
    for i in range(1,len(high)-1):
        acceleration[i]=(k/m[i])*(high[i-1]+high[i+1]-2*high[i])
    for i in range(len(high)):
        high[i]+=velocitys[i]*dt+acceleration[i]*dt**2/2
        velocitys[i]+=acceleration[i]*dt
    return high,velocitys
def get_energy(velocitys,high,m,k):
    energy=0
    for i in range(len(velocitys)):
        energy+=m[i]*velocitys[i]**2/2
    differences=[]
    for i in range(1,len(high)):
        differences.append(high[i]-high[i-1])
    for i in differences:
        energy+=k*i*i/2
    return energy
def map_high_to_points(high,x0,y0,dx):
    #повертає точки з висотами high
    points=[]
    for i in range(len(high)):
        points.append([x0+i*dx,y0-high[i]])
    return points
while 2>1:
    display.update()
    win.fill((0,0,0))
    for i in event.get():
        if i.type==QUIT:
            exit()
    clock.tick(60)
    points=map_high_to_points(high,x0,y0,dx)
    draw.lines(win,(255,0,0),False,points,3)
    high,velocitys=change_kubiks(high,velocitys)
    print(get_energy(high,velocitys,m,k))
