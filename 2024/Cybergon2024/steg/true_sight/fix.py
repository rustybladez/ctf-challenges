import binascii

def fix_png_structure(input_file, output_file):
    # Correct PNG signature
    png_signature = b'\x89PNG\r\n\x1a\n'
    ihdr_chunk_name = b'IHDR'
    ihdr_chunk_length = b'\x00\x00\x00\x0d'  # IHDR length (13 bytes)

    with open(input_file, 'rb') as f:
        data = f.read()

    # Ensure the file starts with the PNG signature
    if not data.startswith(png_signature):
        print("Fixing PNG signature...")
        data = png_signature + data[8:]

    # Check for IHDR presence
    if ihdr_chunk_name not in data[:32]:
        print("IHDR chunk missing. Fixing...")
        # Add the IHDR chunk identifier and length
        data = data[:8] + ihdr_chunk_length + ihdr_chunk_name + data[8:]

    # Save the fixed file
    with open(output_file, 'wb') as f:
        f.write(data)

    print(f"File saved as {output_file}.")
    print("Run a PNG validator or open it to verify.")

# Paths for the input and output files
input_file = 'CYBERGON.png'  # Replace with your corrupted PNG file path
output_file = 'fixed.png'    # Output file with the corrected structure

# Run the function
fix_png_structure(input_file, output_file)
