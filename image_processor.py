from PIL import Image

# Path to the original image
image_path = r'c:\Users\Sana\Desktop\image-processing-exam\sample.jpg'

# Open the image
image = Image.open(image_path)

# Convert the image to grayscale
grayscale_image = image.convert('L')

# Save the grayscale image as grayscale_sample.jpg
grayscale_image.save(r'c:\Users\Sana\Desktop\\image-processing-exam\grayscale_sample.jpg')

print("Grayscale image saved successfully.")


