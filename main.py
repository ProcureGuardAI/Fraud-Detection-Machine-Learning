import pickle
import pandas as pd

# Load the model
with open("best_model_random_forest.pkl", "rb") as f:
    model = pickle.load(f)

# Example usage
def predict(data):
    return model.predict(data)

# Example data
data = pd.DataFrame({
    'feature1': [1, 2, 3],
    'feature2': [4, 5, 6]
})

# Make predictions
predictions = predict(data)
print(predictions)