from PIL import Image  # Import the PIL library for image handling
import numpy as np  # Import NumPy for array manipulation
import cv2  # Import OpenCV for image processing

# Load the image using PIL
file = "cat.jpg"  # Specify the path to the image file
img = Image.open(file)  # Open the image file using PIL, creating an Image object

# Convert the PIL image to a NumPy array
img_np = np.array(img)  # Convert the Image object to a NumPy array

# Resize the image using cv2.resize
# Set the percentage for horizontal and vertical resizing
fx = 0.1  # Scale factor for width (10% of the original width)
fy = 0.1  # Scale factor for height (10% of the original height)
resized_img_np = cv2.resize(img_np, None, fx=fx, fy=fy)  # Resize the image using OpenCV

# Convert the resized NumPy array back to a PIL image
resized_img = Image.fromarray(resized_img_np)  # Convert the NumPy array back to a PIL Image object

# Display the resized image
resized_img.show()  # Display the resized image using PIL
