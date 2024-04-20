from sklearn.model_selection import train_test_split

# Create sample data
X = range(10)
y = [i * 2 for i in X]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

print("Training data:", X_train, y_train)
print("Testing data:", X_test, y_test)
