# Library Imports
import sys

# File Imports
import model
import csv_import

func_to_be_run = input("Make model(0) or load and run model(1): ")

if func_to_be_run == '0':
    model.modeller()
elif func_to_be_run == '1':
    print("""
If music-recommender.joblib does not exist in current directory, program will crash
""")
    X, y = csv_import.reader_and_divider()
    model.model_loader(X, y)
else:
    print("Imma head out...")
    sys.exit(1)
