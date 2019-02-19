# import scikit learn datasets libraries
from sklearn import datasets
#  import the metrics for the calculation of accuracy 
from sklearn import metrics
# import the split function using cross validation
from sklearn.cross_validation import train_test_split
#impoting the gaussian naive bayes model
from sklearn.naive_bayes import GaussianNB

#loads the iris dataset
IRIS = datasets.load_iris()

# create the x and z
X = IRIS.data
z = IRIS.target

#splitting the dataset into training and test data
X_train, X_test, z_train, z_test = train_test_split(X, z, test_size=0.3, random_state=5)

# Gaussian classifier created
model = GaussianNB()

#training the model using the training sets
model.fit(X_train, z_train)

#prediction for the test dataset 
z_pred = model.predict(X_test)

# calculating accuracy for the actual and predicted values of test datasets
print("Accuracy of naivebayes method is:",metrics.accuracy_score(z_test, z_pred))
