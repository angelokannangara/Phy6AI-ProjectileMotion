import math
from scipy.constants import g
import csv

def projectileSimulator(u, thetaDeg, writer):
    t=0
    y=0
    thetaRad = math.radians(thetaDeg)
    dt = 0.05

    while y >= 0:
        x = u * math.cos(thetaRad) * t
        y = (u * math.sin(thetaRad) * t) - (0.5 * g * t ** 2)
        v_x = u * math.cos(thetaRad)
        v_y = u * math.sin(thetaRad) - g * t

        alpha = math.atan(v_y / v_x)
        writer.writerow([round(t, 2), round(v_x, 2), round(v_y, 2), round(alpha, 2), round(x, 2), round(y, 2)])

        t += dt





with open('projectile_data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['time','velocity-x','velocity-y','angle','x','y'])

    for u in range(10,51,10):
        for thetaDeg in range(15,75,15):
            projectileSimulator(u, thetaDeg, writer)

