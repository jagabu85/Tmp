import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation


print("---------------------------------------------------- Start")
print("Point definitions")
a_0 = np.array([0,        0])
b_0 = np.array([62.5,     0])
c_0 = np.array([350,      0])
d_0 = np.array([350,     50])
e_0 = np.array([62.5, -62.5])
f_0 = np.array([56,    -374])

print("Define froces in points")
force_d = np.array([0, 85*1.6*9.81])

print("Define discretization")
num_steps = 20
angle = np.linspace(0,3.14*0.5,num_steps)
rotation = np.zeros((2,2))

force_e = np.zeros((num_steps, 2))

for i, alpha in enumerate(angle):
    rotation[0,0] = np.cos(alpha)
    rotation[0,1] = -np.sin(alpha)
    rotation[1,0] = np.sin(alpha)
    rotation[1,1] = np.cos(alpha)

    d = rotation.dot(d_0)
    e = rotation.dot(e_0)
    e_unit = e /  np.linalg.norm(e)
	
    fe = e - f_0
    fe_unit = fe /  np.linalg.norm(fe)
 
    sin_theta = np.cross(e_unit, fe_unit)

    force_e_norm = (np.cross(d,force_d))/ (np.linalg.norm(e)*sin_theta)
    force_e[i] =force_e_norm * fe_unit

print(force_e)
"""


# F means force
length_b = 62.5
length_c = 350
force_c = 850

point_b_init = np.array([length_b, 0])
point_e_init = np.array([length_b, -62.5])
point_d = np.array([length_b, -356.2])

num_steps = 20
angle = np.linspace(0,3.14*0.5,num_steps)

moment_b = np.zeros(num_steps)
force_b_y1 = np.zeros(num_steps)
force_e_xs = np.zeros((num_steps,2))
force_e_ys= np.zeros((num_steps,2))

force_e_x = np.zeros((num_steps,1))
force_e_y= np.zeros((num_steps,1))


rotation = np.zeros((2,2))
for i, alpha in enumerate(angle):
    moment_b[i] = force_c * np.cos (alpha) * length_c
    force_b_y1[i] = moment_b[i] / length_b

    rotation[0,0] = np.cos(alpha)
    rotation[0,1] = -np.sin(alpha)
    rotation[1,0] = np.sin(alpha)
    rotation[1,1] = np.cos(alpha)
    
    point_b = rotation.dot(point_b_init)
    point_e = rotation.dot(point_e_init)
                           
    eb = point_b-point_e # vecto_eb
    eb_unit = eb / np.linalg.norm(eb)
    force_e_y1 = force_b_y1[i]*eb_unit

    de = point_e - point_d
    de_unit = de / np.linalg.norm(de)
    perpendicular_de_unit = np.array([-de_unit[1] , de_unit[0] ])
    force_e_xs[i] = np.dot(force_e_y1, de_unit) * de_unit
    force_e_ys[i] = np.dot(force_e_y1, perpendicular_de_unit) * perpendicular_de_unit

    axis_x = np.array([1, 0])
    axis_y = np.array([0, 1])
    force_e_x[i] = np.dot(force_e_y1, axis_x)
    force_e_y[i] = np.dot(force_e_y1, axis_y)

    print(force_e_y1)

"""
"""
plt.rc('text', usetex=True)
plt.rc('font', family='serif')
fig, ax1 = plt.subplots()
plt.plot(angle, force_e_x, label='x')
plt.plot(angle, force_e_y, label='y')
ax1.set_xlabel(r'Angle in rad')
plt.legend()
plt.show()




# Start animation

fig, ax = plt.subplots()
ax.set_xlim(-10,10)
ax.set_ylim(-10, 10)
xdata, ydata = [], []
line, = plt.plot([], [], '-r')



coordinates_x = np.array([0, 1])
coordinates_y = np.array([0, 1])


def init():
    line.set_data([],[])
    return line,

def update(frame):
    #xdata.append(frame)
    #ydata.append(np.sin(frame))
    #line.set_data(xdata, ydata)
    #arrow.seta_data(1,1,2,2)
    line.set_data(coordinates_x, coordinates_y*frame)
    return line,

ani = FuncAnimation(fig, update, frames=np.linspace(0, 2*np.pi, 128),
                    init_func=init, blit=True)
#plt.show()i
"""
