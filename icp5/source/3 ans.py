from sklearn.cluster import KMeans
import pandas as pd
from sklearn.metrics import silhouette_score
dataset = pd.read_csv('College.csv')

dataset = dataset.drop(['Unnamed: 0'], axis=1)
dataset = dataset.drop(['Private'], axis=1)
#train,test=train_test_split(data,test_size=0.4)
for i in range(2,7) :
    kmean = KMeans(n_clusters=i, max_iter=300)
    x=kmean.fit_predict(dataset)
   
    sil=silhouette_score(dataset,x)
    print("for cluster ",i,"silhouette score is",sil)