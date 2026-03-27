import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import alpha

df = pd.read_csv('projectile_data.csv')

plt.figure(figsize=(10,6))

for name, group in df.groupby('velocity-x'):
    plt.plot(group['x'],group['y'], label=f'v_x={name}m/s')


plt.title('Projectile Motion Simulator')
plt.xlabel('Distance(Meters)')
plt.ylabel('Height(Meters)')
plt.axhline(0, color='black', linewidth=1)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()

plt.show()


