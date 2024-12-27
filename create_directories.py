import os
from datetime import datetime

# Define the base path for the content folders
base_path = "dynamic-content-2025"

# Create the base path directory if it doesn't exist
if not os.path.exists(base_path):
    os.makedirs(base_path)

# Create a folder for each day of the year in 2025
year = 2025
for day_of_year in range(1, 366 + 1):  # Account for 2025 being a leap year
    date = datetime.strptime(f"{year}-{day_of_year}", "%Y-%j").date()
    folder_name = date.strftime("%Y-%m-%d")
    folder_path = os.path.join(base_path, folder_name)
    
    # Create the folder
    os.makedirs(folder_path, exist_ok=True)
    
    # Add a sample index.html file in each folder
    with open(os.path.join(folder_path, "index.html"), "w") as f:
        f.write(f"<html><body><h1>Content for {folder_name}</h1></body></html>")

print(f"Dynamic content folders for {year} have been created under '{base_path}'.")