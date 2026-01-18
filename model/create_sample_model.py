import pickle
import numpy as np
from sklearn.dummy import DummyRegressor

# Dummy regressor predicts mean value
X_dummy = np.random.rand(50, 10)   # 10 features (incl RERA)
y_dummy = np.random.randint(20, 100, size=50)

model = DummyRegressor(strategy="mean")
model.fit(X_dummy, y_dummy)

with open("sample_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("sample_model.pkl created successfully")
