import numpy as np
from PIL import Image
from io import BytesIO

def has_cancer(microscope_image, feature_image_bytes):
    # Example criteria for cancer detection (replace with actual criteria)
    # For demonstration, we assume that cancer is detected if a certain pattern is present in both images.

    # Check microscope image for specific tissue pattern
    cancer_pattern_present = np.any(microscope_image < 100)

    # Check feature image for specific feature (e.g., color distribution)
    feature_image = Image.open(BytesIO(feature_image_bytes))
    feature_array = np.array(feature_image)
    feature_criteria_met = np.mean(feature_array[:, :, 0]) > 100  # Check if red channel intensity is above a threshold

    # Determine overall cancer status
    cancer_detected = cancer_pattern_present and feature_criteria_met

    return cancer_detected

# Example usage:
# Assuming you have generated simulated images using the code from the previous responses
cancer_status = has_cancer(simulated_microscope_image, simulated_feature_image_bytes)

# Print the result
if cancer_status:
    print("Parasite has cancer.")
else:
    print("Parasite does not have cancer.")
