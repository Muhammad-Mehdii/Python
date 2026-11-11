# import libraries
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
#generate small dataset
np.random.seed(42)
X = 2 * np.random.rand(100, 1)
Y = 4 + 3 * X + np.random.randn(100, 1)
# create linear regression model
model = LinearRegression()
model.fit(X, Y)
# make predictions
X_new = np.array([[0], [1.5] , [2]])
Y_predict = model.predict(X_new)
#original data and liner regression line
plt.scatter(X, Y, label="Orignal Data")
plt.plot(X_new, Y_predict, color='red', label="Regression Line")
plt.scatter(X_new, Y_predict, color='red', label="Predicted data")
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Linear Regression Example")
plt.legend()
plt.show()
