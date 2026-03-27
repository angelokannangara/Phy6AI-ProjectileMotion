import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

df = pd.read_csv('projectile_data.csv')

X = df[['velocity-x', 'velocity-y', 'time']]
y = df['x']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model= LinearRegression()
model.fit(X_train, y_train)

test_velocity_x = 20.0
test_velocity_y = 15.0
test_time = 2.5

test_data = pd.DataFrame([[20.0, 15.0, 2.5]], columns=['velocity-x', 'velocity-y', 'time'])
prediction = model.predict(test_data)

print(f"Prediction for x distance:{prediction[0]:.24f}meters")
print(f"Manual Math(v_x*t):{test_velocity_x * test_time:.4f}meters")
