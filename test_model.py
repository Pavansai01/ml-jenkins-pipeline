import joblib
import numpy as np

model = joblib.load('decision_tree_model.pkl')

X_new = np.array([[5.1, 3.5, 1.4, 0.2]])

y_new = model.predict(X_new)
print(f'Predicted class: {y_new}')
