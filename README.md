# Physics-Informed Machine Learning: Projectile Motion

This project demonstrates a full-stack AI Engineering workflow: from simulating physical phenomena to training a predictive Machine Learning model.

## 🚀 Overview
I developed this project to bridge the gap between **Theoretical Physics** and **Data Science**. It uses a custom-built engine to simulate projectile motion and then employs a Linear Regression model to "discover" kinematic relationships.

## 🛠️ Tech Stack
- **Language:** Python
- **Libraries:** NumPy, SciPy (Physics), Pandas (Data Handling), Matplotlib (Visualization), Scikit-Learn (ML)
- **Tools:** PyCharm, Git

## 📈 Project Phases
1. **Mathematical Simulation:** A Python loop calculates displacement ($x, y$) and instantaneous velocity ($v_x, v_y$) using kinematic equations ($s = ut + \frac{1}{2}at^2$).
2. **Data Generation:** The script generates a dataset of 100+ unique flight paths with varying initial velocities and angles.
3. **Visualization:** Using Matplotlib to verify the parabolic trajectories.
4. **Machine Learning:** A Linear Regression model is trained to predict the landing distance based on initial state vectors.

## 📖 How to Run
1. Clone the repo: `git clone [YOUR_URL]`
2. Install dependencies: `pip install -r requirements.txt`
3. Generate data: `python data_generator.py`
4. Train AI: `python ai_model.py`

---
*Created by Angelo Kannangara | Undergraduate at UOM & USJ*