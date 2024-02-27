import pandas as pd

file_path = "german-credit.txt"

data = pd.read_csv(file_path, delimiter=' ', header=None)

decision_column = data.iloc[:, -1]
decision_classes = decision_column.unique()

print("Symbole klas decyzyjych: ")
print(decision_classes)

classes_counts = decision_column.value_counts()
print(classes_counts)

min_values = data.min()
max_values = data.max()

for column, min_val, max_val in zip(data.columns, min_values, max_values):
    if pd.api.types.is_numeric_dtype(data[column]):
        print(f"Column: {column}")
        print(f"  Minimum value: {min_val}")
        print(f"  Maximum value: {max_val}")

for column in data.columns:
    unique_values = data[column].unique()
    print(f"Column: {column}")
    print(f"  Unique values: {unique_values}")
    print(f"  Unique values count: {len(unique_values)}")

for column in data.columns:
    if pd.api.types.is_numeric_dtype(data[column]):
        std_dev = data[column].std()
        print(f"Column: {column}")
        print(f"  Standard deviation: {std_dev}")