from sklearn.linear_model import LinearRegression

# Sample data
X = [[1], [2], [3], [4], [5]]
y = [2, 4, 6, 8, 10]

# Create the model and fit the data
model = LinearRegression()
model.fit(X, y)

# Make a prediction
x_new = [[6]]
print(model.predict(x_new))
