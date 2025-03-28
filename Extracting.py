# Read the file contents
with open(appended_file, "rb") as f:
    content = f.read()

# Locate the hidden data using markers
start_marker = b"--HIDDEN-DATA--"
end_marker = b"--END--"

start = content.find(start_marker)
end = content.find(end_marker)

if start != -1 and end != -1:
    hidden_data = content[start + len(start_marker): end].strip()
    print(f"Extracted hidden data: {hidden_data.decode()}")
else:
    print("No hidden data found")
