import pandas as pd
import numpy as np

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

column_minmax = {}

for column, min_val, max_val in zip(data.columns, min_values, max_values):
    if pd.api.types.is_numeric_dtype(data[column]):
        column_minmax[column] = (min_val, max_val)
        print(column_minmax[column])

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

print("====================================================")

random_rows = np.random.randint(0, 999, size=200)
random_cols = np.random.randint(0, 19, size=200)

data_nan = data.copy()
data_nan.iloc[random_rows, random_cols] = np.nan

print(data_nan)

column_stats = {}

for column in data.columns:
    if pd.api.types.is_numeric_dtype(data[column]):
        mean_value = data[column].mean()
    else:
        most_common_value = data[column].mode().iloc[0]
        mean_value = most_common_value
    column_stats[column] = mean_value

for column in data.columns:
    data_nan[column] = data_nan[column].fillna(column_stats[column])

print(data_nan)

data_normalized_1 = data.copy()
a = -1
b = 1
for index, row in data_normalized_1.iterrows():
    for column in data_normalized_1.columns:
        if pd.api.types.is_numeric_dtype(data[column]):
            data_normalized_1.at[index, column] = (row[column] - column_minmax[column][0]) * (b - a)) / (column_minmax[column][1] - column_minmax[col.name][0]) + a

print(data_normalized_1)