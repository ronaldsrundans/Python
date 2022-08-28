from sklearn.linear_model import LogisticRegression
from sklearn.datasets.samples_generator import make_blobs
import pandas as pd
import numpy as np
from sklearn import linear_model
#separating into labels and features
df = pd.read_csv('train.csv', delimiter=",")
label = df['class']
features = df.drop('class', axis=1)
#defining our logistic regression estimator and training
regr = linear_model.LogisticRegression()
regr.fit(features, label)
# new instances where we do not know the answer
df2 = pd.read_csv('test.csv', delimiter=",")
df2=df2.values
# make a prediction
ynew = regr.predict_proba(df2)
# show the inputs and predicted outputs
thislist = []
for i in range(len(ynew)):
	#print("Predicted=%s" % ( ynew[i][1]))
	#print(ynew[i][1])
	thislist.append(ynew[i][1])
#print(thislist)
#probabilities for class=1
df = pd.DataFrame(thislist)
df.to_csv('ronaldsrundans.csv', index=False,header=False)


