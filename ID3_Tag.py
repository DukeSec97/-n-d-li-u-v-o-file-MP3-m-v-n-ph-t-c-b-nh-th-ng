from mutagen.id3 import ID3, TXXX
import shutil

# Input MP3 file path
input_file = "input.mp3"
output_file = "metadata_hidden.mp3"

# Create a copy of the original file for editing
shutil.copy(input_file, output_file)

# Add hidden data to the metadata
tags = ID3(output_file)
tags.add(TXXX(encoding=3, desc="HiddenInfo", text="Secret hidden data"))
tags.save(output_file)

print(f"Hidden data has been embedded into the metadata of {output_file}")
