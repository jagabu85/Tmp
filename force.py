import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation


print("---------------------------------------------------- Start")

# F means force
length_b = 0.5
length_c = 3
force_c = 1

num_steps = 20
angle = np.linspace(0,3.14*0.5,num_steps)

moment_b = np.zeros(num_steps)
force_b_y1 = np.zeros(num_steps)
force_b_out_xs = np.zeros((num_steps,2))
force_b_out_ys= np.zeros((num_steps,2))

point_b_init = np.array([0.5,0])
point_b_out_init = np.array([0.5,-0.25])
point_d = np.array([0.5, -2])

rotation = np.zeros((2,2))
for i, alpha in enumerate(angle):
    moment_b[i] = force_c * np.cos (alpha) * length_c
    force_b_y1[i] = moment_b[i] / length_b

    rotation[0,0] = np.cos(alpha)
    rotation[0,1] = -np.sin(alpha)
    rotation[1,0] = np.sin(alpha)
    rotation[1,1] = np.cos(alpha)
    
    point_b = rotation.dot(point_b_init)
    point_b_out = rotation.dot(point_b_out_init)
                           
    vector_db = point_d - point_b_out
    
    dv_unit = vector_db / np.linalg.norm(vector_db)
    perpendicular_dv_unit = np.array([-dv_unit[1], dv_unit[0]])
    force_b = force_b_y1[i] * ((point_b-point_b_out) / np.linalg.norm(point_b-point_b_out))
    force_b_out_xs[i] = np.dot(force_b, dv_unit) * dv_unit
    force_b_out_ys[i] = np.dot(force_b, perpendicular_dv_unit) * perpendicular_dv_unit


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
plt.show()
