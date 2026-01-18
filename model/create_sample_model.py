import pickle
import numpy as np
from sklearn.dummy import DummyRegressor

# Deterministic randomness
np.random.seed(42)

# 🔑 MATCH FORM INPUT COUNT (5 FEATURES)
X_dummy = np.random.rand(50, 5)
y_dummy = np.random.randint(20, 100, size=50)

model = DummyRegressor(strategy="mean")
model.fit(X_dummy, y_dummy)

with open("sample_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("sample_model.pkl created (5 features, deterministic)")
