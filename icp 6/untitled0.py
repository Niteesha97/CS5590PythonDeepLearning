from sklearn.cross_validation import train_test_split
from sklearn import datasets
from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt



dataset = pd.read_csv('weatherHistory.csv')


y = dataset['Temperature (C)']

X = dataset.drop(['Summary','Daily Summary','Temperature (C)','Loud Cover'],axis=1)

X = pd.get_dummies(X, columns=["Precip Type"])



X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=101)

lm = LinearRegression()
model = lm.fit(X_train,y_train)

predictions = lm.predict(X_test)
print(predictions)



print ('RMSE is: \n', mean_squared_error(y_test, predictions))
print ("R^2 is: \n", model.score(X_test, y_test))




