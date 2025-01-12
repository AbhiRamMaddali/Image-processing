#The Version of Python compiler 3.13.0
import cv2
import numpy as np

# Load the image
image = cv2.imread(r"C:\Users\abhir\Desktop\PXL_20210509_052249401.jpg")  # Replace 'image.jpg' with your image file

# Create a binary mask
# Example: A circular mask in the center
height, width = image.shape[:2]
mask = np.zeros((height, width), dtype=np.uint8)  # Create a blank black mask
center = (width // 2, height // 2)  # Center of the image
radius = min(width, height) // 4  # Radius of the circle
cv2.circle(mask, center, radius, (255), -1)  # Draw a white circle on the mask

# Apply the mask to the image
masked_image = cv2.bitwise_and(image, image, mask=mask)

# Save and display the images
cv2.imwrite(r"C:\Users\abhir\Desktop\jh.jpg", masked_image)
