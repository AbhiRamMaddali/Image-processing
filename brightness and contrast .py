#The Version of Python compiler 3.13.0
def adjust_brightness_contrast_bmp(input_path, output_path, alpha=1.0, beta=0):
    """
    Adjusts the brightness and contrast of a 24-bit BMP image manually.

    :param input_path: Path to the input BMP file.
    :param output_path: Path to save the output BMP file.
    :param alpha: Contrast factor (e.g., 1.0 = no change, >1.0 increases contrast).
    :param beta: Brightness offset (e.g., 0 = no change, >0 increases brightness).
    """
    with open(input_path, "rb") as bmp_file:
        # Read the entire BMP file into memory
        bmp_data = bytearray(bmp_file.read())

    # Parse BMP header to get pixel data offset, width, height, and bits per pixel
    pixel_data_offset = int.from_bytes(bmp_data[10:14], "little")
    width = int.from_bytes(bmp_data[18:22], "little")
    height = int.from_bytes(bmp_data[22:26], "little")
    bits_per_pixel = int.from_bytes(bmp_data[28:30], "little")

    if bits_per_pixel != 24:
        raise ValueError("This program only supports 24-bit BMP files.")

    # BMP rows are padded to multiples of 4 bytes
    row_size = (width * 3 + 3) & ~3

    # Process each pixel
    for y in range(height):
        row_start = pixel_data_offset + y * row_size
        for x in range(width):
            # Calculate pixel position in the row
            pixel_pos = row_start + x * 3

            # Read B, G, R values
            b = bmp_data[pixel_pos]
            g = bmp_data[pixel_pos + 1]
            r = bmp_data[pixel_pos + 2]

            # Adjust brightness and contrast for each channel
            b_new = min(max(int(alpha * b + beta), 0), 255)
            g_new = min(max(int(alpha * g + beta), 0), 255)
            r_new = min(max(int(alpha * r + beta), 0), 255)

            # Write new values back
            bmp_data[pixel_pos] = b_new
            bmp_data[pixel_pos + 1] = g_new
            bmp_data[pixel_pos + 2] = r_new

    # Save the modified BMP file
    with open(output_path, "wb") as output_file:
        output_file.write(bmp_data)


# Example usage
input_bmp = r"C:\Users\abhir\Desktop\color_photo.bmp"
output_bmp = r"C:\Users\abhir\Desktop\c_photo.bmp"
adjust_brightness_contrast_bmp(input_bmp, output_bmp, alpha=2.0, beta=50)  # Increase contrast and brightness
print("Brightness and contrast adjusted. Saved to", output_bmp)
