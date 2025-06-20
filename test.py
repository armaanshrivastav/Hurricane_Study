import re
import os

def extract_start_time_from_filename(filename):
    # Remove file extension if present
    filename_without_ext = os.path.splitext(filename)[0]
    
    # Find all numeric sequences in the filename
    numeric_sequences = re.findall(r"\d+", filename_without_ext)
    
    # The start time is typically the last 6-digit sequence (hhmmss format)
    for seq in reversed(numeric_sequences):
        if len(seq) == 6:  # Ensure it's a valid hhmmss format
            return seq
    
    return None  # Return None if no valid time found

# **Test Cases**
test_files = [
    "D20201007_010346_PQC",  # Expected: "010346"
    "D20211225_235959",       # Expected: "235959"
    "NoTimeHere.txt",         # Expected: None
    "AnotherFile_000123.dat", # Expected: "000123"
    "D20231215_120500_v2"     # Expected: "120500"
]

for file in test_files:
    print(f"Filename: {file} -> Extracted Start Time: {extract_start_time_from_filename(file)}")
