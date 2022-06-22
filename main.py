"""
----------------
Machine Learning
----------------
"""

# Imports
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

"""
----------------------
Data Frame [IMPORTANT]
----------------------
"""


# DataFrame is a 2-dimensional labeled data structure with
# columns of potentially different types.
# You can think of it like a spreadsheet or SQL table, or a
# dictionary of Series objects.
# It is generally the most commonly used pandas object.


# music_data is a data frame with the values of the given file
music_data = pd.read_csv('/Users/adviksharma/Programming/Python /music.csv')

# X is the data frame without the column genre
X = music_data.drop(columns=['genre'])

# y is the data frame with only genre as te
y = music_data['genre']

# Unpacking the training and testing data randomly
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Creates Decision tree model
model = DecisionTreeClassifier()

# Takes in the training data as arguments
# 2 in supervised learning and 1 in unsupervised learning
model.fit(X_train, y_train)

# Gives the X testing data (the people and their ages)
# to the model with which the model will make the predictions
predictions = model.predict(X_test)

# Compares the predictions of the model (genres of the people)
# and the testing data (actual genres of the people)
score = accuracy_score(y_test, predictions)
print(predictions)
print(score)
