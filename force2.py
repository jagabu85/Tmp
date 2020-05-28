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
num_steps = 50
angle = np.linspace(0,3.14*0.7,num_steps)
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


# Plot force by components X and Y at point e
"""plt.rc('text', usetex=True)
plt.rc('font', family='serif')
fig, ax1 = plt.subplots()
plt.plot(angle, force_e[:,0], label='x')
plt.plot(angle, force_e[:,1], label='y')
ax1.set_xlabel(r'Angle in rad')
plt.legend()
plt.show()
"""

# Start animation

fig, ax = plt.subplots()
ax.set_xlim(-400, 400)
ax.set_ylim(-7500, 7500)
angle_template = 'angle = %.3fº'
angle_text = ax.text(0, 0, '', transform=ax.transAxes)

xdata = np.zeros((1,2))
ydata = np.zeros((1,2))
line, = plt.plot([], [], '-r')

def init():
    line.set_data([],[])
    angle_text.set_text('')
    return line,

def update(i):
    #xdata.append(frame)
    #ydata.append(np.sin(frame))
    
    xdata[0,1] = force_e[i,0]
    ydata[0,1] = force_e[i,1]

    line.set_data(xdata, ydata)

    angle_text.set_text(angle_template % np.degrees(angle[i]))
    return line,

ani = FuncAnimation(fig, update, num_steps,
                    init_func=init, blit=False)
plt.show()

