import pandas as pd

def fetch_data():
    # Create a larger DataFrame with example data
    data = {
        'Name': [
            'Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Hannah', 'Ivy', 'Jack', 
            'Kathy', 'Liam', 'Mona', 'Nina', 'Oscar', 'Paul', 'Quincy', 'Rachel', 'Steve', 'Tina',
            'Uma', 'Victor', 'Wendy', 'Xander', 'Yara', 'Zack', 'Angela', 'Bruce', 'Clara', 'Dan',
            'Emma', 'Fiona', 'George', 'Helen', 'Ian', 'Julia', 'Kevin', 'Laura', 'Mike', 'Nora',
            'Oliver', 'Pam', 'Quinn', 'Rita', 'Sam', 'Tracy', 'Ursula', 'Vince', 'Will', 'Xena'
        ],
        'Age': [
            24, 27, 22, 32, 29, 35, 31, 28, 26, 30, 
            33, 21, 25, 34, 23, 36, 29, 31, 27, 32,
            24, 29, 28, 35, 26, 30, 24, 27, 22, 32, 
            29, 35, 31, 28, 26, 30, 33, 21, 25, 34, 
            23, 36, 29, 31, 27, 32, 24, 29, 28, 35
        ],
        'City': [
            'New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Jose',
            'Austin', 'Jacksonville', 'Fort Worth', 'Columbus', 'Charlotte', 'San Francisco', 'Indianapolis', 'Seattle', 'Denver', 'Washington',
            'Boston', 'El Paso', 'Nashville', 'Detroit', 'Oklahoma City', 'Portland', 'Las Vegas', 'Memphis', 'Louisville', 'Baltimore',
            'Milwaukee', 'Albuquerque', 'Tucson', 'Fresno', 'Sacramento', 'Mesa', 'Kansas City', 'Atlanta', 'Long Beach', 'Colorado Springs',
            'Raleigh', 'Miami', 'Virginia Beach', 'Omaha', 'Oakland', 'Minneapolis', 'Tulsa', 'Arlington', 'Tampa', 'New Orleans'
        ],
        'Salary': [
            50000, 55000, 45000, 60000, 52000, 58000, 62000, 48000, 51000, 53000,
            54000, 56000, 47000, 59000, 61000, 57500, 49000, 57000, 52000, 53000,
            55000, 56000, 47000, 58000, 60000, 61000, 49000, 57000, 52000, 53000,
            50000, 55000, 45000, 60000, 52000, 58000, 62000, 48000, 51000, 53000,
            54000, 56000, 47000, 59000, 61000, 57500, 49000, 57000, 52000, 53000
        ],
        'Department': [
            'HR', 'Engineering', 'Marketing', 'Sales', 'Finance', 'HR', 'Engineering', 'Marketing', 'Sales', 'Finance',
            'HR', 'Engineering', 'Marketing', 'Sales', 'Finance', 'HR', 'Engineering', 'Marketing', 'Sales', 'Finance',
            'HR', 'Engineering', 'Marketing', 'Sales', 'Finance', 'HR', 'Engineering', 'Marketing', 'Sales', 'Sales',
            'Finance', 'HR', 'Engineering', 'Marketing', 'Sales', 'Finance', 'HR', 'Engineering', 'Marketing', 'Sales',
            'Finance', 'HR', 'Engineering', 'Marketing', 'Sales', 'Finance', 'HR', 'Engineering', 'Marketing', 'Sales'
        ]
    }

    # Check if all arrays have the same length
    length = len(data['Name'])
    if not all(len(lst) == length for lst in data.values()):
        raise ValueError("All arrays must be of the same length")

    df = pd.DataFrame(data)
    
    # Save the data to a CSV file
    df.to_csv('large_example_data.csv', index=False)
    print("Data fetched and saved to 'data/large_example_data.csv'")

if __name__ == "__main__":
    fetch_data()
