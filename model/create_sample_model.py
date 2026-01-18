import pickle
import numpy as np
from sklearn.dummy import DummyRegressor


np.random.seed(42)

# Create dummy training data
X_dummy = np.random.rand(50, 10)   # 10 features (including RERA)
y_dummy = np.random.randint(20, 100, size=50)

# Train dummy regressor (predicts mean)
model = DummyRegressor(strategy="mean")
model.fit(X_dummy, y_dummy)

# Save model
with open("sample_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("sample_model.pkl created successfully with deterministic behavior")
