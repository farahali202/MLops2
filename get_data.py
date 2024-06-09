# get_data.py
import pandas as pd

def fetch_data():
    # Create a simple DataFrame with example data
    data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
        'Age': [24, 27, 22, 32, 29],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
    }
    df = pd.DataFrame(data)
    
    # Save the data to a CSV file
    df.to_csv('data/example_data.csv', index=False)
    print("Data fetched and saved to 'data/example_data.csv'")

if __name__ == "__main__":
    fetch_data()
