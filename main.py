"""
App entry point

# Note: This script assumes that all columns in data.csv are numeric.
# If there are non-numeric columns, you'd need to handle or exclude them when computing these statistics.
"""

import polars as pl
import matplotlib.pyplot as plt


def load_data(filename):
    return pl.read_csv(filename)


def display_dataset_head(data):
    print("Dataset Head:")
    print(data.head())
    print("\n")


def display_basic_statistics(data):
    print("Basic Descriptive Statistics:")
    print(data.describe())
    print("\n")


def generate_summary_statistics(data):
    print("\nMedian:\n", data.median())
    print("\n")


def visualize_data(data):
    # Extracting data from the Polars DataFrame and converting to numpy arrays
    age = data.select("Age").to_numpy().flatten()
    scores = data.select("Score").to_numpy().flatten()

    plt.bar(age, scores)
    plt.xlabel('Age')
    plt.ylabel('Score')
    plt.title('Average Score by Age')
    plt.show()


def main():
    data = load_data('data.csv')
    display_dataset_head(data)
    display_basic_statistics(data)
    generate_summary_statistics(data)
    visualize_data(data)


if __name__ == "__main__":
    main()

