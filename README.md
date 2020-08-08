# Binary Classifier

A simple script that performs binary classification.

We import the CSV files and upon analyzing the available datasets two problems are detected. The existance of 'NA' fields and string data. So, we drop any rows which contain nullfilable cells and then go about one-hot encoding using `pd.get_dummies`. 

Multiple ML Algorithms were applied yet the better performing ones were SVM and Logistic Regression based models while the worst ones were Neural Network and Gaussian Bayes. 

A simple Flask endpoint was implement to serve the result in a JSON format.


This project uses [Poetry](https://github.com/python-poetry/poetry)
```
poetry install
export FLASK_ENV=development FLASK_APP=main.py
poetry run flask run
```