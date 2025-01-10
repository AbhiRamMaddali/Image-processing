def rgb_to_grayscale_bmp(input_bmp_path, output_bmp_path):
    with open(input_bmp_path,'rb') as f:
        # Read BMP header (first 54 bytes)
        header = f.read(54)

        # Read the pixel data
        pixel_data = f.read()

    # Grayscaleflter pixel data
    grayscale_pixel_data = bytearray()

    for i in range(0, len(pixel_data), 3):
        # Extract RGB values
        B = pixel_data[i]
        G = pixel_data[i + 1]
        R = pixel_data[i + 2]
        r=min(2*R,255)
        g=int((1-0.5)*G)
        b =int((1 - 0.5)*B)
        t=int((1-0.5)*R+0.5*255)



        # Compute grayscale value
        grayscale_value = int(R+0*G+0*B)

        # Replace RGB with grayscale
        grayscale_pixel_data.extend([t,b,g])

    # Save the new BMP file
    with open(output_bmp_path, 'wb') as f:
        f.write(header)  # Write the header
        f.write(grayscale_pixel_data)  # Write the grayscale pixels


# Example usage
input_bmp_path = r"C:\Users\abhir\Desktop\color_photo.bmp"

output_bmp_path = r"C:\Users\abhir\Desktop\l_image.bmp"  # Output BMP path

rgb_to_grayscale_bmp(input_bmp_path, output_bmp_path)
print(f"Grayscale image saved as {output_bmp_path}")
