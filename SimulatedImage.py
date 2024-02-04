 # we created simulated images for both microscope and feature-extracted images using the data structures we chose earlier. We'll use NumPy for the microscope image and simulate JPEG compression for the feature-extracted image.


import numpy as np
from PIL import Image, ImageDraw
from io import BytesIO

# Function to create simulated microscope image
def create_simulated_microscope_image(height, width):
    # Simulate tissue patterns using random values
    tissue_pattern = np.random.randint(0, 256, size=(height, width), dtype=np.uint8)

    # Create a blank image
    microscope_image = Image.new("L", (width, height), color=255)
    draw = ImageDraw.Draw(microscope_image)

    # Simulate tissue patterns on the blank image
    draw.point(np.column_stack(np.where(tissue_pattern < 200)), fill=0)

    # Convert image to NumPy array
    microscope_image_array = np.array(microscope_image)

    return microscope_image_array

# Function to create simulated feature-extracted image
def create_simulated_feature_image():
    # Simulate a colorful feature-extracted image
    feature_image = np.random.rand(256, 256, 3) * 255  # Random RGB image
    feature_image = feature_image.astype(np.uint8)

    # Save the feature image as a JPEG in memory (simulating compression)
    img_bytesio = BytesIO()
    Image.fromarray(feature_image).save(img_bytesio, format='JPEG', quality=90)
    feature_image_bytes = img_bytesio.getvalue()

    return feature_image_bytes

# Simulation parameters
microscope_image_height = 500
microscope_image_width = 500

# Create simulated microscope image
simulated_microscope_image = create_simulated_microscope_image(microscope_image_height, microscope_image_width)

# Display or process simulated microscope image as needed

# Create simulated feature-extracted image
simulated_feature_image_bytes = create_simulated_feature_image()

# Display or process simulated feature-extracted image as needed




