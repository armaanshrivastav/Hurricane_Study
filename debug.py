import os
import shutil
import traceback
import pandas as pd
import altitude_radial_velocity
import altitude_theta_e
import altitude_vertical_velocity
from create_ui_root import create_root_html_with_title_and_footer
import radial_velocity
import tangential_velocity
import theta_e
import vertical_velocity
import trajectory
import wind_speed
import altitude_windspeed






def copy_main_template(source_file, target_folders):
    for folder_path in target_folders:
        destination_file = os.path.join(folder_path, "main.html")
        try:
            shutil.copy(source_file, destination_file)
            print(f"Copied {source_file} to {destination_file}")
        except Exception as e:
            print(f"Failed to copy to {destination_file}: {e}")

def clean_filename(i, filename):
    try:
        # Ensure the string starts with 'D' and ends with '.csv'
        if filename.endswith(".csv"):
            # Remove the leading 'D' and the '.csv' extension
            return f'{i} {filename[:-4]}'
        else:
            # If conditions don't match, return the original string
            return f'{i} {filename}'
    except Exception as e:
        # Return the original string in case of any error
        return f'{i} {filename}'
    
# Define the root folder containing the data
data_folder = 'C:/Users/abhin/OneDrive/Documents/SRP 2024-25/ProcessedData/Armaan/Fabian17'
colors=['blue','purple','darkred','green','black','yellow','red']

# Custom colorscale approximating 'tab20'
"""
custom_colorscale = [
    [0.0, '#377eb8'],  # Blue
    [0.1, '#ff7f00'],  # Orange
    [0.2, '#4daf4a'],  # Green
    [0.3, '#f781bf'],  # Pink
    [0.4, '#a65628'],  # Brown
    [0.5, '#984ea3'],  # Purple
    [0.6, '#999999'],  # Gray
    [0.7, '#e41a1c'],  # Red
    [0.8, '#dede00'],  # Yellow
    [1.0, '#377eb8']   # Repeat Blue for continuity
]
"""

custom_colorscale = [
    [0.0, '#1f77b4'],  # Blue
    [0.1, '#ff7f0e'],  # Orange
    [0.2, '#2ca02c'],  # Green
    [0.3, '#d62728'],  # Red
    [0.4, '#9467bd'],  # Purple
    [0.5, '#8c564b'],  # Brown
    [0.6, '#e377c2'],  # Pink
    [0.7, '#7f7f7f'],  # Gray
    [0.8, '#bcbd22'],  # Yellow-green
    [1.0, '#17becf']   # Cyan
]

# Traverse all subfolders and files in the data folder
for root, dirs, files in os.walk(data_folder):
    dirs.sort()  # Sort directories in alphabetical order
    files.sort()  # Sort files in alphabetical order
    # Initialize an array to store DataFrames for the current folder
    all_dataframes = []
    folder_name = os.path.basename(root)
    print(f"root={root}")
    print(dirs)
    print(files)