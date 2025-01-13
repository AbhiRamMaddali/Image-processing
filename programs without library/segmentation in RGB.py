def color_segmentation(input_path, output_path):
    with open(input_path, 'rb') as f:
        header = f.read(54)  # BMP header is 54 bytes
        pixel_data = f.read()

    # Extract image dimensions from the header
    width = int.from_bytes(header[18:22], 'little')
    height = int.from_bytes(header[22:26], 'little')
    bits_per_pixel = int.from_bytes(header[28:30], 'little')

    if bits_per_pixel == 24:
        bytes_per_pixel = 3
    elif bits_per_pixel == 32:
        bytes_per_pixel = 4
    else:
        raise ValueError("Unsupported BMP format! Only 24-bit and 32-bit are supported.")

    # BMP rows are padded to be multiples of 4 bytes
    row_padding = (4 - (width * bytes_per_pixel) % 4) % 4

    # Initialize an array for the new pixel data
    new_pixel_data = bytearray()

    for y in range(height):
        for x in range(width):
            # Calculate the pixel index in the flat bytearray
            pixel_index = (y * (width * bytes_per_pixel + row_padding)) + (x * bytes_per_pixel)
            b = pixel_data[pixel_index]
            g = pixel_data[pixel_index + 1]
            r = pixel_data[pixel_index + 2]

            # If 32-bit, skip the alpha channel
            if bytes_per_pixel == 4:
                a = pixel_data[pixel_index + 3]  # Alpha channel

            # Apply color segmentation (example: threshold on RGB channels)
            if r > 128:  # Threshold for red
                r_seg = 255
            else:
                r_seg = 0

            if g > 128:  # Threshold for green
                g_seg = 255
            else:
                g_seg = 0

            if b > 128:  # Threshold for blue
                b_seg = 255
            else:
                b_seg = 0

            # Add the segmented pixel to the new pixel data
            new_pixel_data.extend([b_seg, g_seg, r_seg])

            # If 32-bit, preserve the alpha channel
            if bytes_per_pixel == 4:
                new_pixel_data.append(a)

        # Add row padding to the new pixel data
        new_pixel_data.extend([0] * row_padding)

    # Write the new BMP file
    with open(output_path, 'wb') as f:
        f.write(header)  # Write the header unchanged
        f.write(new_pixel_data)  # Write the modified pixel data

    print(f"Color-segmented BMP saved at {output_path}")


input_path = r"C:\Users\abhir\Desktop\park1.bmp"
output_path = r"C:\Users\abhir\Desktop\img_color.bmp"
color_segmentation(input_path, output_path)
