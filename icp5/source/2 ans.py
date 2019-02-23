from sklearn.cluster import KMeans
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="white", color_codes=True)
import warnings
warnings.filterwarnings("ignore")

dataset = pd.read_csv('College.csv')

dataset = dataset.drop(['Unnamed: 0'], axis=1)
dataset = dataset.drop(['Private'], axis=1)

x = dataset.iloc[:,[1,2,3,4]]
y = dataset.iloc[:-1]
print(x,y)



print(dataset.info())
# see how many samples we have of each species
print(dataset["PhD"].value_counts())

sns.FacetGrid(dataset, hue="PhD", size=10).map(plt.scatter, "Accept", "Enroll")
# do same for petals
sns.FacetGrid(dataset, hue="PhD", size=10).map(plt.scatter, "Accept", "Enroll")
plt.show()
# note that the species are nearly linearly separable with petal size,but sepal sizes are more mixed.
from sklearn import preprocessing
1
scaler = preprocessing.StandardScaler()

scaler.fit(x)
X_scaled_array = scaler.transform(x)
X_scaled = pd.DataFrame(X_scaled_array, columns = x.columns)


nclusters = 3# this is the k in kmeans
seed = 0

km = KMeans(n_clusters=nclusters, random_state=seed)
km.fit(X_scaled)

# predict the cluster for each data point
y_cluster_kmeans = km.predict(X_scaled)
print(y_cluster_kmeans)


