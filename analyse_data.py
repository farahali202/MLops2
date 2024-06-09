# analyse_data.py
import pandas as pd

def analyze_data():
    # Read the data from the CSV file
    df = pd.read_csv('data/example_data.csv')
    
    # Perform some basic analysis
    mean_age = df['Age'].mean()
    city_counts = df['City'].value_counts()
    
    # Print the results
    print(f"Mean Age: {mean_age}")
    print("City Counts:")
    print(city_counts)

if __name__ == "__main__":
    analyze_data()
