# Binary Classifier

## WIP

As of right now I'm currently stuck on matching the number of features between training and validation set. None of my models can run without solving this issue first.

I used LabelEncoder and OneHotEncoder to tackle the problem of categorical data but apparently OneHotEncoder increases the number of features drastically!

I tried using `pd.get_dummies` but to no avail. Also, I came across a stackoverflow answer which recommended combining both datasets into one but I couldn't get it to work. :( 


This script is written using *Jupyter Notebook* to easily visualise the data while working on it.

Just simply fire up *Jupyter Notebook* and import `notebook.ipynb` and you're set to go.