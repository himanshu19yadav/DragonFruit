# DragonFruit


Let’s BreakDown the Problem: 


Microscope Images: Black and white images, 100,000x100,000 pixels each, showing the whole microorganism.
In the captured image, the microorganism appears as a single blob.
The shape of this blob is arbitrary, meaning it can have any form or structure.
Each pixel in the images can have one of two colors: black or white.
If a pixel is part of the microorganism (the blob), it is black.
If a pixel is in the space surrounding the microorganism, it is white.
The images are quite large, with dimensions of 100,000x100,000 pixels. This means each image is a grid of 100,000 rows and 100,000 columns of pixels. Many thousands of such images will be captured.There will be one image for each microorganism in a colony. where each image is essentially a grid of black and white pixels, representing the microorganism and its surroundings.

Dye Sensor:
The images captured by the dye sensor are also 100,000x100,000 pixels, matching the resolution of the microscope images.
The dye sensor images highlight areas that are illuminated by the dye, giving a visual representation of where the dye is located within the microorganism.
the dye sensor may sometimes indicate the presence of dye outside of the microorganism.
while the dye sensor provides valuable information about where the luminescent dye is present in the microorganism, the researchers need to be aware of potential leakage, which might cause the sensor to detect dye outside of the intended areas. 


The images from the microscope depict the entire microorganism (parasite) in detail. However, these images only show the overall structure of the microorganism, represented as a blob, with no specific information about the presence of the luminescent dye.
The images from the dye sensor, captured simultaneously with the microscope, focus solely on indicating where the luminescent dye is present. These images provide information about the illuminated areas within the microorganism, but there might be some detection of dye outside the microorganism due to leakage.
A microorganism (parasite) is considered to have cancer if the total amount of luminescent dye detected within its body surpasses 10% of the area occupied by the microorganism in the image.
The researchers want to store images of all the microorganisms they have studied. Additionally, they want to store images specifically showing where the dye is present in the microorganisms. However, they only want to store these dye images for microorganisms that meet the cancer criteria (dye amount exceeds 10% of the microorganism area).



