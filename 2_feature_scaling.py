import numpy as np
from sklearn.preprocessing import MinMaxScaler

# Create sample data
data = np.array([[1], [2], [3], [4]])

# Perform Min-Max scaling
scaler = MinMaxScaler()
scaled_data = scaler.fit_transform(data)

print("Scaled data:")
print(scaled_data)
