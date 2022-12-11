import pandas as pd
import numpy as np

df = pd.read_csv('data_cleaned.csv')
df = df.dropna()

# choose variables
df.columns

df_model = df[['Gold','Year', 'Sport', 'Discipline', 'Country', 'Gender', 'Population','GDP_per_Capita',
             'Prev_Gold_Medals_Won', 'Prev_Silver_Medals_Won', 'Prev_Bronze_Medals_Won']]
# get dummy variables
df_dum = pd.get_dummies(df_model)

# Train test split
from sklearn.model_selection import train_test_split

X = df_dum.drop('Gold', axis=1)
y = df_dum['Gold'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

X_train = X_train.reset_index()
X_test = X_test.reset_index()
X_train = X_train.drop('index', axis=1)
X_test = X_test.drop('index', axis=1)

# knn Classification
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score

knn = KNeighborsClassifier()
knn.fit(X_train, y_train)
np.mean(cross_val_score(knn, X_train, y_train, cv=4))

# Random Forest Classification
from sklearn.ensemble import RandomForestClassifier

rf = RandomForestClassifier()
np.mean(cross_val_score(rf, X_train, y_train, cv=4))

# Use gridsearch to optimise knn model
from sklearn.model_selection import GridSearchCV

knn_parameters = {'n_neighbors':range(3,7), 'weights':('uniform', 'distance'), 'p':(1, 2)}
knn_gs = GridSearchCV(knn, knn_parameters, cv=4)
knn_gs.fit(X_train, y_train)

knn_gs.best_score_
knn_gs.best_estimator_

# Use gridsearch to optimise knn model
rf_parameters = {'n_estimators':range(10,300,10), 'criterion':('gini', 'entropy', 'log_loss'), 'max_features':('auto', 'sqrt', 'log2'), 'class_weight':('none', 'balanced', 'balanced_subsample')}
rf_gs = GridSearchCV(rf, rf_parameters, cv=4)
rf_gs.fit(X_train, y_train)

rf_gs.best_score_
rf_gs.best_estimator_

# Test models with test data
t_pred_knn = knn_gs.best_estimator_.predict(X_test)
t_pred_rf = rf_gs.best_estimator_.predict(X_test)

from sklearn.metrics import accuracy_score
accuracy_score(y_test, t_pred_knn)
accuracy_score(y_test, t_pred_rf)

# Pickle Model for Productionization
import pickle

filename = 'Gold_Medal_Predictor_Model'
pickle.dump(knn_gs.best_estimator_, open(filename, 'wb'))