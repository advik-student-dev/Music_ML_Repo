"""
----------------
Machine Learning
----------------
"""

"""
-------
Imports
-------
"""

# Imports of libraries
import pandas as pd
import joblib
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import tree
import sys


# Creates Decision tree model
model = DecisionTreeClassifier()

fuck_you_count = 0


def modeller():
    global model
    global fuck_you_count

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

    # Places the return values of reader_and_divider (in tuple) in X and y
    X, y = reader_and_divider()

    # Unpacking the training and testing data randomly
    X_train, X_test, y_train, y_test = unpacker_of_test_and_train_data(X, y)

    # Takes in the training data as arguments
    # 2 in supervised learning and 1 in unsupervised learning
    model.fit(X_train, y_train)

    save_or_not_to_save = input("Would you like to save the model(yes/no): ").lower()
    if save_or_not_to_save == 'yes':
        # Saves the model
        joblib.dump(model, 'music-recommender.joblib')
    elif save_or_not_to_save == 'no':
        print("Not saving model \n")
    else:
        print("Fuck You!")
        fuck_you_count += 1

    predict_or_not_to_predict = input("Predict or not to predict(yes/no): ").lower()
    if predict_or_not_to_predict == 'yes':

        # Gives the X testing data (the people and their ages)
        # to the model with which the model will make the predictions
        predictions = model.predict(X_test)

        score_or_not_to_score = input(
"Would you like to score the accuracy of the model(yes/no): ")

        if score_or_not_to_score == 'yes':
            print(predictions)

            # Compares the predictions of the model (genres of the people)
            # and the testing data (actual genres of the people)
            score = accuracy_score(y_test, predictions)
            print(score)
        elif score_or_not_to_score == 'no':
            print(predictions)
        else:
            print("Fuck You")
            fuck_you_count += 1
    elif predict_or_not_to_predict == 'no':
        print("No predictions = No scoring = No drawing. Bye mothafucka")
        sys.exit(1)
    else:
        print("This the second input in this program loop and you did this. Imma head out...")
        sys.exit(1)

    if fuck_you_count >= 2:
        print(f"fuck_you_count is {fuck_you_count}. Goodbye you Dumbfuck")
        sys.exit(1)

    draw_or_not_to_draw = input("Would you like to make a graph of the model(yes/no): ").lower()
    if draw_or_not_to_draw == 'yes':
        # Makes a Decision Tree Graph(because the model is a 'DecisionTreeClassifier' object)
        tree.export_graphviz(model, out_file='music-recommender.dot',
                             feature_names=['age', 'gender'],  # To see the rules in the nodes
                             class_names=sorted(y.unique()),  # Displaying the class(here genre) of each node
                             label='all',  # Gives all nodes labels that we can read
                             rounded=True,  # To give rounded corners
                             filled=True  # To give each box a colour
                             )
        print("Exported the file")
    elif draw_or_not_to_draw == 'no':
        print("Ok")
    else:
        print(f"fuck_you_count = {fuck_you_count}. Fuck You!")


def model_loader(without_genres, genres):
    global model

    # Loads the model made by the modeler
    model = joblib.load('music-recommender.joblib')

    # Unpacking the training and testing data randomly
    X_train, X_test, y_train, y_test = train_test_split(without_genres, genres, test_size=0.2)
    predictions = model.predict(X_test)
    score = accuracy_score(y_test, predictions)
    print(predictions)
    print(score)


def reader_and_divider():
    # music_data is a data frame with the values of the given file
    music_data = pd.read_csv('/Users/adviksharma/Programming/Python /music.csv')

    # X is the data frame without the column genre
    X_return = music_data.drop(columns=['genre'])

    # y is the data frame with only genre as te
    y_return = music_data['genre']

    return X_return, y_return


def unpacker_of_test_and_train_data(without_genre, genre):
    # Unpacking the training and testing data randomly
    X_train_unpacked, X_test_unpacked, y_train_unpacked, y_test_unpacked = \
        train_test_split(without_genre, genre, test_size=0.2)

    return X_train_unpacked, X_test_unpacked, y_train_unpacked, y_test_unpacked


func_to_be_run = input("Make model(0) or load and run model(1): ")

if func_to_be_run == '0':
    modeller()
elif func_to_be_run == '1':
    print("""
If music-recommender.joblib does not exist in current directory, program will crash
""")
    X, y = reader_and_divider()
    model_loader(X, y)
else:
    print("Imma head out...")
    sys.exit(1)
