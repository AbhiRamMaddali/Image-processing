#The Version of Python compiler 3.13.0
def rgb_to_grayscale_bmp(input_bmp_path, output_bmp_path):
    with open(input_bmp_path,'rb') as f:
        # Read BMP header (first 54 bytes)
        header = f.read(54)
        pixel_data = f.read()

    # Grayscale pixel data
    grayscale_pixel_data = bytearray()

    for i in range(0, len(pixel_data), 3):
                                                     # Extract RGB values
        B = pixel_data[i]
        G = pixel_data[i + 1]
        R = pixel_data[i + 2]

        # Compute grayscale value
        grayscale_value = int(0.2126*R+0.7152*G+0.0722*B)

        # Replace RGB with grayscale
        grayscale_pixel_data.extend([grayscale_value,grayscale_value,grayscale_value])

    # Save the new BMP file
    with open(output_bmp_path, 'wb') as f:
        f.write(header)  # Write the header
        f.write(grayscale_pixel_data)  # Write the grayscale pixels


# Example usage
input_bmp_path = r"C:\Users\abhir\Desktop\cat.bmp"

output_bmp_path = r"C:\Users\abhir\Desktop\d_image.bmp"  # Output BMP path

rgb_to_grayscale_bmp(input_bmp_path, output_bmp_path)
print(f"Grayscale image saved as {output_bmp_path}")
