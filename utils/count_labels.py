import pandas as pd

# Load the dataset
file_path = 'test_predictions_cnn1d_best1.csv'  # Replace with your file path if different
data = pd.read_csv(file_path)

# Ensure you know the column where the classes are stored
# Replace 'ClassColumn' with the actual column name containing the class values
class_column = 'Predicted Label'  # Replace with the name of your column

# Count the occurrences of each class
class_counts = data[class_column].value_counts()

# Display the count for classes 0, 12, and 3
for class_label in [0, 1,2, 3]:
    print(f"Class {class_label}: {class_counts.get(class_label, 0)}")
