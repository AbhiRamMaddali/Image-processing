def img_crop(input_path, output_path, x, y, x1, y1):
    # Open the input BMP file
    with open(input_path, 'rb') as f:
        # Read the BMP header (first 54 bytes)
        header = f.read(54)

        # Extract metadata from the BMP header
        width = int.from_bytes(header[18:22], byteorder='little')
        height = int.from_bytes(header[22:26], byteorder='little')
        bits_per_pixel = int.from_bytes(header[28:30], byteorder='little')

        # Ensure the BMP file is either 24-bit or 32-bit
        if bits_per_pixel not in [24, 32]:
            raise ValueError("This function supports only 24-bit and 32-bit BMP files.")

        # Calculate bytes per pixel and row size
        bytes_per_pixel = bits_per_pixel // 8
        row_size = (width * bytes_per_pixel + 3) & ~3  # Row size padded to a multiple of 4 bytes

        # Calculate cropping dimensions
        crop_width = x1 - x
        crop_height = y1 - y
        if crop_width <= 0 or crop_height <= 0 or x1 > width or y1 > height:
            raise ValueError("Invalid cropping coordinates.")

        # Read the pixel data
        pixel_data = f.read()

        # Prepare the cropped pixel data
        cropped_data = bytearray()
        for row in range(y, y1):  # Loop through the rows in the cropping region
            row_start = row * row_size  # Start of the current row in the pixel data
            cropped_row = pixel_data[row_start + x * bytes_per_pixel:row_start + x1 * bytes_per_pixel]

            # Add the cropped row to the cropped data
            cropped_data.extend(cropped_row)

            # Add padding to make the cropped row size a multiple of 4 bytes
            crop_row_size = (crop_width * bytes_per_pixel + 3) & ~3
            padding = crop_row_size - (crop_width * bytes_per_pixel)
            cropped_data.extend(b'\x00' * padding)

    # Update the BMP header for the cropped image
    new_header = bytearray(header)
    new_header[18:22] = crop_width.to_bytes(4, 'little')  # Update width
    new_header[22:26] = crop_height.to_bytes(4, 'little')  # Update height
    new_header[2:6] = (54 + len(cropped_data)).to_bytes(4, 'little')  # Update file size

    # Write the cropped BMP file
    with open(output_path, 'wb') as f:
        f.write(new_header)
        f.write(cropped_data)

    print(f"Cropped image saved to {output_path}")


# Example usage
input_path = r"C:\Users\abhir\Desktop\hl.bmp"
output_path = r"C:\Users\abhir\Desktop\cropped.bmp"

# Define the cropping region (x, y, x1, y1)
x = 50 # Starting x-coordinate
y = 50  # Starting y-coordinate
x1 = 200  # Ending x-coordinate
y1 = 200  # Ending y-coordinate

# Crop the BMP image
img_crop(input_path, output_path, x, y, x1, y1)
