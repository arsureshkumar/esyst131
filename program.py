import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
dataX, dataY = datasets.lead_diabetes(return_X_y = True)
dataX = dataX[:, np.newaxis, 2]
trainX = dataX[:-30]
testX = dataX[-30:]
trainY = dataY[:-30]
testY = dataY[-30:]
lr = linear_model.LinearRegression()
lr.fit(trainX, trainY)
predY = lr.predict(testX)
print("Coefficients: ", lr.coef_)
print("Mean squared error: %.2f" % mean_squared_error(testY, predY))
print("Coefficient of Determination: %.2f" % r2_score(testY, predY))
plt.scatter(testX, testY, color="black")
plt.plot(testX, predY, color="blue", linewidth=3)