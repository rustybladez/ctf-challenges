import os

# Directory containing the files (update with the actual path if needed)
directory = "."

# Initialize an empty string to store the combined binary data
combined_binary = ""

# Loop through file names from 0.txt to 55.txt
for i in range(55, -1, -1):
    file_name = f"{i}"
    file_path = os.path.join(directory, file_name)
    
    try:
        # Read the contents of the file
        with open(file_path, "r") as file:
            content = file.read().strip()
            # Add the file's content to the combined binary string
            combined_binary += content
    except FileNotFoundError:
        print(f"Error: {file_name} not found. Skipping.")
    except Exception as e:
        print(f"Error reading {file_name}: {e}")

# Print the combined binary string
print(combined_binary)
