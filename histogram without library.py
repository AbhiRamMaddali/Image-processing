#The Version of Python compiler 3.13.0
def calculate_histogram(image_path):
    # Open the image in binary mode
    with open(image_path, 'rb') as file:
        data = file.read()

    # Convert image data into pixel intensities
    pixel_values = [byte for byte in data]

    # Initialize histogram bins (0-255 for grayscale)
    histogram = [0] * 256

    # Count pixel intensity occurrences
    for pixel in pixel_values:
        if 0 <= pixel < 256:  # Ensure it's a valid intensity
            histogram[pixel] += 1

    return histogram


def plot_histogram(histogram):
    max_frequency = max(histogram)
    scale = 50 / max_frequency  # Scale frequencies for terminal display

    print("Pixel Intensity Histogram")
    for intensity, frequency in enumerate(histogram):
        bar = '█' * int(frequency * scale)  # ASCII bar chart
        print(f"{intensity:3}: {bar}")


# Example usage
image_path = r"C:\Users\abhir\Desktop\color_photo.bmp" # Must be raw grayscale image data
histogram = calculate_histogram(image_path)
plot_histogram(histogram)

