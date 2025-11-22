# explore_datetime.py

# Import datetime module
from datetime import datetime, timedelta

# Function to display current date and time
def display_current_datetime():
    current_date = datetime.now()  # Get current date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")  # Format
    print(f"Current date and time: {formatted_date}")

# Function to calculate future date
def calculate_future_date():
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        future_date = datetime.now() + timedelta(days=days_to_add)  # Add days
        formatted_future_date = future_date.strftime("%Y-%m-%d")  # Format
        print(f"Future date: {formatted_future_date}")
    except ValueError:
        print("Please enter a valid number.")

# Run the functions
if __name__ == "__main__":
    display_current_datetime()
    calculate_future_date()