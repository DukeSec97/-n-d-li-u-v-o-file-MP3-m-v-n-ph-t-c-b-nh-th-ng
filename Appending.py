# Define file paths
appended_file = "appended_hidden.mp3"

# Create a copy before appending data
shutil.copy(output_file, appended_file)

# Hidden data with markers for easy extraction
hidden_data_marker = b"\n--HIDDEN-DATA--\nSECRET_PAYLOAD_1234567890\n--END--\n"

# Append hidden data to the end of the file
with open(appended_file, "ab") as f:
    f.write(hidden_data_marker)

print(f"Hidden data has been appended to the end of {appended_file}")
