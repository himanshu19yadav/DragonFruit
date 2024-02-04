import numpy as np
import time
import sys

# Data Structures

class MicroorganismImage:
    def __init__(self, pixels):
        self.pixels = pixels

class DyeSensorImage:
    def __init__(self, dye_presence):
        self.dye_presence = dye_presence

class MicroorganismMetadata:
    def __init__(self, area, dye_amount, has_cancer):
        self.area = area
        self.dye_amount = dye_amount
        self.has_cancer = has_cancer

# Simulated Image Generation

def generate_microorganism_image(size=100, blob_size=25):
    pixels = np.zeros((size, size), dtype=int)

    # Create a random blob representing the microorganism
    blob_x, blob_y = np.random.randint(size - blob_size + 1, size, size=2)
    pixels[blob_x - blob_size//2:blob_x + blob_size//2, blob_y - blob_size//2:blob_y + blob_size//2] = 1

    return MicroorganismImage(pixels)

def generate_dye_sensor_image(microorganism_image, leakage_prob=0.1):
    dye_presence = microorganism_image.pixels.copy()

    # Introduce some dye leakage
    dye_leakage = np.random.rand(*dye_presence.shape) < leakage_prob
    dye_presence[dye_leakage] = 1

    return DyeSensorImage(dye_presence)

# Cancer Detection Algorithm

def compute_cancer_status(microorganism_image, dye_sensor_image):
    # Assuming pixels are binary (0 for black, 1 for white)
    area = np.sum(microorganism_image.pixels)
    dye_amount = np.sum(dye_sensor_image.dye_presence * microorganism_image.pixels)

    # Check if the calculated dye percentage exceeds the threshold for cancer
    dye_percentage = (dye_amount / area) * 100
    has_cancer = dye_percentage > 10

    return has_cancer

# Compression Techniques

def run_length_encode(image):
    encoded_image = []
    count = 1

    for i in range(1, len(image)):
        if image[i] == image[i - 1]:
            count += 1
        else:
            encoded_image.extend([count, image[i - 1]])
            count = 1

    encoded_image.extend([count, image[-1]])
    return encoded_image

def measure_storage_cost(image):
    return sys.getsizeof(image)

# Main Workflow

# Generate and visualize simulated images
microorganism_image = generate_microorganism_image()
dye_sensor_image = generate_dye_sensor_image(microorganism_image)

# Compute cancer status
has_cancer = compute_cancer_status(microorganism_image, dye_sensor_image)
print(f"The microorganism {'has cancer.' if has_cancer else 'does not have cancer.'}")

# Compression Example (Run-Length Encoding)
sample_image = np.random.randint(2, size=(100000, 100000), dtype=np.uint8)
encoded_image = run_length_encode(sample_image.flatten())

# Measure storage cost
original_storage_cost = measure_storage_cost(sample_image)
encoded_storage_cost = measure_storage_cost(encoded_image)

# Output results
print(f"\nOriginal Storage Cost: {original_storage_cost} bytes")
print(f"Encoded Storage Cost: {encoded_storage_cost} bytes")
print(f"Compression Ratio: {original_storage_cost / encoded_storage_cost:.2f}")
