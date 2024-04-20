from sklearn.linear_model import LinearRegression

# Create sample data
X = [[i] for i in range(10)]
y = [2*i for i in range(10)]

# Fit a linear regression model
model = LinearRegression()
model.fit(X, y)

# Predict using the model
prediction = model.predict([[11]])

print("Prediction using linear regression:", prediction[0])
