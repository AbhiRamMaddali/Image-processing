# two add any imgaes the size of the images should be same
def img_to_blend(input_path1, input_path2, output_path, weight1=0.9, weight2=0.1):
    def get_pixel_depth(header):
        # Extract bits per pixel from the BMP header (offset 28, 2 bytes)
        return int.from_bytes(header[28:30], byteorder='little')

    # Open and read the first BMP file
    with open(input_path1, 'rb') as f1:
        header1 = f1.read(54)
        pixel_data1 = f1.read()

    # Open and read the second BMP file
    with open(input_path2, 'rb') as f2:
        header2 = f2.read(54)
        pixel_data2 = f2.read()

    # Check if headers match
    if header1 != header2:
        raise ValueError(
            "The headers of the two BMP files do not match. Ensure both images have the same dimensions and format."
        )

    # Get bits per pixel
    bits_per_pixel = get_pixel_depth(header1)
    if bits_per_pixel not in (24, 32):
        raise ValueError(f"Unsupported bits per pixel: {bits_per_pixel}. Only 24-bit and 32-bit BMP images are supported.")

    # Ensure both images have the same size
    if len(pixel_data1) != len(pixel_data2):
        raise ValueError(
            "The pixel data sizes of the two BMP files do not match. Ensure both images have the same resolution."
        )

    # Determine bytes per pixel
    bytes_per_pixel = bits_per_pixel // 8

    # Blend the pixel data
    blend_data = bytearray()
    for i in range(0, len(pixel_data1), bytes_per_pixel):  # Process pixel by pixel
        B1, G1, R1 = pixel_data1[i:i + 3]
        B2, G2, R2 = pixel_data2[i:i + 3]

        B_new = int(weight1 * B1 + weight2 * B2)
        G_new = int(weight1 * G1 + weight2 * G2)
        R_new = int(weight1 * R1 + weight2 * R2)

        blend_data.extend([B_new, G_new, R_new])

        # For 32-bit images, preserve the alpha channel from the first image
        if bytes_per_pixel == 4:
            A1 = pixel_data1[i + 3]
            blend_data.append(A1)

    # Write the blended image to the output path
    with open(output_path, 'wb') as f_out:
        f_out.write(header1)
        f_out.write(blend_data)


# Example usage
input_path1 = r"C:\Users\abhir\Desktop\red.bmp"
input_path2 = r"C:\Users\abhir\Desktop\black.bmp"
output_path = r"C:\Users\abhir\Desktop\image0.bmp"

img_to_blend(input_path1, input_path2, output_path)
