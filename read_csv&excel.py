
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
