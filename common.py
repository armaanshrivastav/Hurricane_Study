import os
import shutil
import traceback
import pandas as pd
import altitude_radial_velocity
import altitude_theta_e
import altitude_vertical_velocity
from create_ui_root import create_root_html_with_larger_subcategory_buttons
import radial_velocity
import tangential_velocity
import theta_e
import vertical_velocity
import trajectory
import wind_speed
import altitude_windspeed






def copy_main_template(source_file, target_folders, humidity_mean=None, placeholder="{MeanRH}"):
    for folder_path in target_folders:
        destination_file = os.path.join(folder_path, "main.html")
          # Format humidity_mean to 4 decimal places if provided
        replacement_var = f"{float(humidity_mean):.4f}" if humidity_mean is not None else None
        try:
            if replacement_var is not None:
                # Read the source file and replace the placeholder
                with open(source_file, 'r') as file:
                    content = file.read()
                modified_content = content.replace(placeholder, replacement_var)
                
                # Write the modified content to the destination
                with open(destination_file, 'w') as file:
                    file.write(modified_content)
                print(f"Copied and modified {source_file} to {destination_file} (replaced {placeholder})")
            else:
                # If no replacement_var, just copy the file as-is
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
data_folder = 'C:/Users/abhin/OneDrive/Documents/SRP 2024-25/ProcessedData'
colors=['blue','purple','darkred','green','black','yellow','red','orange','pink','teal','lavender','maroon','turquoise','magenta','olive','cyan','indigo']

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
    # If the folder name ends with a number, format it to two digits
    if folder_name[-1].isdigit():
        base_name = folder_name.rstrip('0123456789')
        number_part = folder_name[len(base_name):]
        folder_name = f"{base_name}{int(number_part):02}"

    # Print the current folder being processed
    print(f"Processing folder path: {root}")
    print(f"Processing folder: {folder_name}")
    names = []
    i=0
    first_file_name=''
    clean_file_name_val=''
    is_first_file_processed = False
    for file in files:
        if file.endswith('.csv'):
            file_path = os.path.join(root, file)
            
            try:
                # Read the CSV file into a DataFrame
                df = pd.read_csv(file_path)

                # Skip files with only headers or empty files
                if df.empty or len(df.columns) == 1:
                    print(f"Skipping file (empty or header-only): {file}")
                    continue
                # Sort the DataFrame by 'Actual Time' if the column exists
                if 'Actual Time' in df.columns:
                    df = df.sort_values(by='Actual Time')
                i=i+1
                # Store the DataFrame in the array
                all_dataframes.append(df)
                clean_file_name_val = clean_filename(i, file)
                if is_first_file_processed==False:
                    first_file_name = file[:-4]
                    is_first_file_processed = True
                names.append(clean_file_name_val)
                # Placeholder for additional operations for each CSV
                # Example: print(f"Processing file: {file}")
                print(f"Processing file: {file}")
            except Exception as e:
                print(f"Error processing file {file_path}: {e}")
                traceback.print_exc()
    print(f"first file name = {first_file_name}")
    # Collect Actual Time values only from DataFrames that contain the column
    actual_time_series = [df['Actual Time'] for df in all_dataframes if 'Actual Time' in df.columns]
    Humidity = [
    pd.to_numeric(df['Humidity'], errors='coerce').dropna().astype(float)
    for df in all_dataframes
    if 'Humidity' in df.columns and not pd.to_numeric(df['Humidity'], errors='coerce').dropna().empty
    ]
    
    if (Humidity):
        all_humidity = pd.concat(Humidity)
        humidity_mean=all_humidity.mean()
    else: 
        humidity_mean = None
  
    # Check if the list is not empty before concatenating
    if actual_time_series:
        all_actual_times = pd.concat(actual_time_series)
        # Convert to integers, then strings, and apply zfill
        min_time = str(int(all_actual_times.min())).zfill(6)
        max_time = str(int(all_actual_times.max())).zfill(6)
        print(f"Minimum Actual Time: {min_time.zfill(6)}")
        print(f"Maximum Actual Time: {max_time}")
        print(f"Folder name = {folder_name}")
        # Check if the folder exists, if not, create it
        folder_path = f'graphs/{folder_name}_{first_file_name}'
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        radial_velocity.plot_trajectories(all_dataframes, names,folder_name, colors,custom_colorscale, f'{folder_path}/radial_velocity.html')
        tangential_velocity.plot_trajectories(all_dataframes, names,folder_name, colors,custom_colorscale, f'{folder_path}/tangential_velocity.html')
        theta_e.plot_trajectories(all_dataframes, names,folder_name, colors,custom_colorscale, f'{folder_path}/theta_e.html')
        vertical_velocity.plot_trajectories(all_dataframes, names,folder_name, colors,custom_colorscale, f'{folder_path}/vertical_velocity.html')
        trajectory.plot_trajectories(all_dataframes, names,folder_name, colors,custom_colorscale,min_time, max_time, f'{folder_path}/trajectory.html')
        wind_speed.plot_trajectories(all_dataframes, names,folder_name, colors,custom_colorscale, f'{folder_path}/wind_speed.html')
        altitude_windspeed.plot_2d_altitude_vs_windspeed(all_dataframes, names,folder_name,colors,  f'{folder_path}/altitude_wind_speed.html')
        altitude_theta_e.plot_2d_altitude_vs_theta_e(all_dataframes, names,folder_name,colors,  f'{folder_path}/altitude_theta_e.html')
        altitude_radial_velocity.plot_2d_altitude_vs_radial_velocity(all_dataframes, names,folder_name,colors,  f'{folder_path}/altitude_radial_velocity.html')
        altitude_vertical_velocity.plot_2d_altitude_vs_vertical_velocity(all_dataframes, names,folder_name,colors,  f'{folder_path}/altitude_vertical_velocity.html')
        copy_main_template('Main_Template.html', [folder_path],str(humidity_mean))
    else:
        print("No DataFrames contain the 'Actual Time' column.")      
    

    pass

    # Placeholder for additional operations for each folder
    # Example: print(f"Finished processing folder: {root}")
    # Clear all_dataframes after processing the folder
    all_dataframes = []
    pass


base_directory = "./graphs"  # Replace with your base directory
output_file = os.path.join(base_directory, "root.html")  # Output file path
project_title = "Visualizing Dropwindsonde Data Of Small Scale Features in Three Dimensions to Document the Role of These Features on Tropical Cyclone Intensity Change"  # Replace with the project title
placeholder_name = "Armaan Shrivastav"  # Replace with the placeholder name for the footer
create_root_html_with_larger_subcategory_buttons(base_directory, output_file, project_title, placeholder_name)

# Example output: print total number of DataFrames loaded
print("Processing completed.")
