"""
----------------
Machine Learning
----------------
"""

# Imports
# import pandas as pd
# from sklearn.tree import DecisionTreeClassifier
import joblib

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
# music_data = pd.read_csv('/Users/adviksharma/Programming/Python /music.csv')

# X is the data frame without the column genre
# X = music_data.drop(columns=['genre'])
#
# y is the data frame with only genre as te
# y = music_data['genre']
#
# Creates new model object
# model = DecisionTreeClassifier()
#
# Takes in the training data as arguments
# 2 in supervised learning and 1 in unsupervised learning
# model.fit(X, y)

# Loads the model music-recommender.joblib
model = joblib.load('music-recommender.joblib')
predictions = model.predict([[21, 1]])
print(predictions)
