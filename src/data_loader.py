import pandas as pd


# Load data and make it dataframe with pandas
def load_data_from_csv(path):
    try:
        data = pd.read_csv(path)
        return data
    except Exception as e:
        print(f"An error occurred while loading the CSV file: {e}")
        return None
