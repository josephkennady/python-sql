# Summary
This script reads CSV and Excel files in a given directory and its subdirectories, removes rows with missing or null values in a specified column, and consolidates the data into a single Excel file.

# Inputs
* master_folder_path: A string containing the path to the master folder that contains the subfolders and files to be processed.

# Output
* An Excel file containing the consolidated data from all the CSV and Excel files in the given directory and its subdirectories. The file will be saved in the same location as the master folder.

# Prerequisites
The following Python modules are required:

* os: This module provides functions for interacting with the operating system.
* pandas: This module provides functions for data manipulation and analysis.

# Usage
To use the script, set the master_folder_path variable to the desired directory, and specify the column to be used for removing rows with missing or null values. Then, run the script.

# =====================================================================================================================================================================

import os
import pandas as pd

 # Set the path to the master folder containing the subfolders
master_folder_path = "path/for/the/main/folder"

# Check if the file exists
if os.path.exists(master_folder_path):
    print("File exists")
else:
    print("File does not exist")

# Create an empty list to store the dataframes
df_list = []

# Iterate through the subfolders in the master folder
for subfolder in os.listdir(master_folder_path):
    subfolder_path = os.path.join(master_folder_path, subfolder)

    # Iterate through the files in the subfolder
    for file in os.listdir(subfolder_path):
        # Check if the file is a CSV or Excel file
        if file.endswith(".csv") or file.endswith(".xlsx"):
            # Try to read the file into a dataframe
            try:
                if file.endswith(".csv"):
                    df = pd.read_csv(os.path.join(subfolder_path, file))
                else:
                    df = pd.read_excel(os.path.join(subfolder_path, file))
            except Exception as e:
                # Print an error message if there is an error
                print(f"Error processing {file}: {e}")
                continue

            # Remove rows with missing or null values in column "A"
            df = df.dropna(subset=["Unnamed: 0"])

            # Add the file and folder information to the dataframe
            df["folder"] = subfolder
            df["file"] = file

            # Add the dataframe to the list
            df_list.append(df)

# Iterate through the files in the main folder
for file in os.listdir(master_folder_path):
    # Check if the file is a CSV or Excel file
    if file.endswith(".csv") or file.endswith(".xlsx"):
        # Try to read the file into a dataframe
        try:
            if file.endswith(".csv"):
                df = pd.read_csv(os.path.join(master_folder_path, file))
            else:
                df = pd.read_excel(os.path.join(master_folder_path, file))
        except Exception as e:
            # Print an error message if there is an error
            print(f"Error processing {file}: {e}")
            continue

        # Remove rows with missing or null values in column "A"
        df = df.dropna(subset=["Unnamed: 0"])

        # Add the file and folder information to the dataframe
        df["folder"] = "main folder"
        df["file"] = file

        # Add the dataframe to the list
        df_list.append(df)

# Concatenate all the dataframes into a single dataframe
df_consolidated = pd.concat(df_list, ignore_index=True)

# Write the consolidated data to an Excel file
df_consolidated.to_excel("destination/file/path/and/file_name.xlsx", index=False)

# =====================================================================================================================================================================

# Customization
* To specify a different column for removing rows with missing or null values, change the value of the subset parameter in the dropna() function. For example, to use column "B" instead of column "A", use df.dropna(subset=["B"]).
* To save the consolidated data to a different location or with a different file name, change the value of the to_excel() function.
* To specify different file types to be processed, modify the if statement that checks the file extension.
* To skip subfolders or files with certain names, use an if statement to check the folder or file name before processing the data.
