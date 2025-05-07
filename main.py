import numpy as np
import matplotlib.pyplot as plt
alt = 0
v0 = 0
acc0 = 0
m = 2300
M = m * .60
g = 9.81
F = m*g
T = 1.5 * F
u = 3000
v = 0
t = 0
ts = 0.01
orbit = 80
mdot = T / u
times = []
altitudes = []
velocities = []
masses = []
accelerations = []
while t < 10:
    m -= mdot * ts
    if m < M:
        m = M
        T = 0
        print("No more fuel")
    acc = (T - m * g) / m
    v += acc*ts
    new_state = alt + v * ts
    alt = new_state
    if alt >= orbit:
        print("Rocket has escaped!")
        break
    elif alt <= 0:
        print("Rocket has crashed!")
        break
    t += ts
    times.append(t)
    altitudes.append(alt)
    velocities.append(v)
    masses.append(m)
    accelerations.append(acc)

plt.plot(times, altitudes)
plt.title("Altitude vs Time")
plt.xlabel("Time (s)")
plt.ylabel("Altitude (m)")
plt.grid(True)
plt.show()