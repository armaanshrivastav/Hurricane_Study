import csv
import os
import re
import traceback

# Convert hhmmss to milliseconds
def hhmmss_to_milliseconds(hhmmss):
    hours = int(hhmmss) // 10000
    minutes = (int(hhmmss) % 10000) // 100
    seconds = int(hhmmss) % 100
    return (hours * 3600 + minutes * 60 + seconds) * 1000

# Convert milliseconds to hhmmss
def milliseconds_to_hhmmss(milliseconds):
    total_seconds = milliseconds / 1000.0
    hours = int(total_seconds // 3600)
    minutes = int((total_seconds % 3600) // 60)
    seconds = total_seconds % 60
    formatted_seconds = f"{seconds:.3f}".split(".")[1]  # Keep up to 3 decimal places for seconds
    return f"{hours:02}{minutes:02}{int(seconds):02}.{formatted_seconds}"

# Extract date (YYYYMMDD) and start time (hhmmss) from filename
def extract_date_and_start_time(filename):
    filename_without_ext = os.path.splitext(filename)[0]  # Remove extension
    numeric_sequences = re.findall(r"\d+", filename_without_ext)  # Extract all numeric sequences
    
    if len(numeric_sequences) < 2:
        return None, None  # Not enough data

    date_part = numeric_sequences[0]  # First numeric sequence is the date (YYYYMMDD)
    
    for seq in numeric_sequences[1:]:
        if len(seq) == 6:  # Look for a valid hhmmss time
            return date_part, seq
    
    return None, None  # No valid time found

# Read and process fixed-width data files
def read_fixed_width_file_to_csv(input_file, start_time_ms, date, start_time, original_root, output_root,
                                 ranges=[5,14,23,31,40,47,53,64,74,86,88,98,109,113,117,121,126,134,144,154,164,176,185]):
    
    # Compute relative path and create the corresponding subdirectory in the output folder
    relative_path = os.path.relpath(os.path.dirname(input_file), original_root)
    output_folder = os.path.join(output_root, relative_path)
    os.makedirs(output_folder, exist_ok=True)  # Ensure the correct subdirectory exists

    # Create output filename in the format YYYYMMDD_hhmmss.csv
    output_file = os.path.join(output_folder, f"{date}_{start_time}.csv")

    try:
        with open(input_file, 'r') as f_in, open(output_file, 'w', newline='') as f_out:
            writer = csv.writer(f_out)
            header = ["IX", "Time", "P (mb)", "Temperature", "Humidity", "Altitude", "WD", "Windspeed", 
                      "U (m/s)", "V (m/s)", "NS", "Vertical Velocity", "GPSz(m)", "FP", "FT", "FH", "FW", 
                      "Latitude", "Longitude", "RD (m/s)", "TA (m/s)", "theta-e (K)", "theta-v (K)", "Actual Time"]
            writer.writerow(header)
            
            for line in f_in:
                row = []
                start = 0
                for end in ranges:
                    row.append(line[start:end].strip())
                    start = end

                # Skip invalid rows containing missing data (-999 values)
                if any(str(value).strip() in ["-999", "-999.0", "-999.00", "-999.000",""] for value in [row[4], row[5], row[7], row[9], row[11], row[17], row[18], row[19], row[20], row[21]]):
                    continue  

                if row[0] == "IX":
                    continue

                try:
                    actual_time = start_time_ms + float(row[1]) * 1000
                    row.append(milliseconds_to_hhmmss(actual_time))
                    writer.writerow(row)
                except ValueError:
                    print(f"Warning: Invalid time data in file '{input_file}', skipping row. {ValueError}")
                    #traceback.print_exc()  # Prints the full traceback for debugging

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"An error occurred while processing '{input_file}': {e}")

# Folder containing data files
input_folder = "../HurricaneCompleteData"
output_folder = "../ProcessedData"

# Recursive file scanning
for root, dirs, files in os.walk(input_folder):
    for file_name in files:
        if not file_name.lower().endswith((".csv", ".xlsx", ".frd", ".bfr", ".png", ".txt", ".nc")):  # Case-insensitive filtering
            date_part, start_time = extract_date_and_start_time(file_name)
            
            if date_part and start_time:
                #print(f"Extracted date: {date_part}, start time: {start_time}")
                start_time_ms = hhmmss_to_milliseconds(start_time)
                #print(f"Processing file: {file_name}")
                input_file = os.path.join(root, file_name)
                read_fixed_width_file_to_csv(input_file, start_time_ms, date_part, start_time, input_folder, output_folder)
            else:
                print(f"Skipping file '{os.path.join(root, file_name)}' (No valid date or start time found).")
