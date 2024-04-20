import matplotlib.pyplot as plt

# Create sample data
x = range(10)
y = [i ** 2 for i in x]

# Plot the data
plt.plot(x, y)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Sample Data Visualization')
plt.show()
