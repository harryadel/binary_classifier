import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from flask import Flask

train = pd.read_csv('training.csv', sep=';')
test = pd.read_csv('validation.csv', sep=';')

train = train.dropna(how='any')
test = test.dropna(how='any')

cols = train.iloc[:, train.columns != 'classLabel']
num_cols = train._get_numeric_data().columns
categorical_cols = list(set(cols) - set(num_cols))

X_train = train[categorical_cols]
X_train = pd.get_dummies(data=X_train, columns=categorical_cols)
X_test = test[categorical_cols]
X_test = pd.get_dummies(data=X_test, columns=categorical_cols)
X_test = X_test.reindex(columns = X_train.columns, fill_value=0)


y_train = train['classLabel']

y_test = test['classLabel']


lr_clf = LogisticRegression(random_state=0, solver='lbfgs', multi_class='ovr')
lr_clf.fit(X_train, y_train)

app = Flask(__name__)
@app.route('/', methods=["GET"])
def main():
  return {
    "train": 'Accuracy of LogisticRegression classifier on training set: {:.2f}'.format(lr_clf.score(X_train,y_train)),
    "test": 'Accuracy of LogisticRegression classifier on test set: {:.2f}'.format(lr_clf.score(X_test,y_test))
  }
     
    