import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# -------- Sample Training Data --------
# Features: country_code, visa_type_code
# Target: processing_days

data = {
    "country": [1, 1, 2, 2, 3, 3, 4, 4],
    "visa":    [1, 2, 1, 2, 1, 2, 1, 2],
    "days":    [45, 60, 30, 35, 50, 55, 40, 45]
}

df = pd.DataFrame(data)

X = df[["country", "visa"]]
y = df["days"]

# -------- Train Model --------
model = LinearRegression()
model.fit(X, y)

# -------- Save Model --------
with open("model.pkl", "wb") as file:
    pickle.dump(model, file)

print("Model trained and saved as model.pkl")
