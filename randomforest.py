# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 10:24:44 2018

@author: ASHWIN JOSEPH
"""

# 2. Import libraries and modules
import numpy as np
import pandas as pd
 
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.ensemble import RandomForestRegressor
# for cross validation
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import GridSearchCV
#importing performance metrics
from sklearn.metrics import mean_squared_error, r2_score
#for re-using our model in the future
from sklearn.externals import joblib 
 
# 3. Load red wine data.
dataset_url = 'http://mlr.cs.umass.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv'
data = pd.read_csv(dataset_url, sep=';')
print(data)
#gives the dimesnsion of the dataset
print(data.shape)
# 4. Split data into training and test sets
y = data.quality
print(y)
X = data.drop('quality', axis=1)
print(X)

 
# 5. Declare data preprocessing steps
pipeline = make_pipeline(preprocessing.StandardScaler(), 
                         RandomForestRegressor(n_estimators=100))
 
# 6. Declare hyperparameters to tune
hyperparameters = { 'randomforestregressor__max_features' : ['auto', 'sqrt', 'log2'],
                  'randomforestregressor__max_depth': [None, 5, 3, 1]}
 
# 7. Tune model using cross-validation pipeline
clf = GridSearchCV(pipeline, hyperparameters, cv=10)
 
clf.fit(X_train, y_train)
 
# 8. Refit on the entire training set
# No additional code needed if clf.refit == True (default is True)
 
# 9. Evaluate model pipeline on test data
pred = clf.predict(X_test)
print(r2_score(y_test, pred))
print(mean_squared_error(y_test, pred))
 
# 10. Save model for future use
joblib.dump(clf, 'rf_regressor.pkl')
# To load: clf2 = joblib.load('rf_regressor.pkl')
#clf2 = joblib.load('rf_regressor.pkl')
 
# Predict data set using loaded model
#clf2.predict(X_test)