import cv2
import matplotlib.pyplot as plt

# Reading the image
image = cv2.imread('C:/Users/Sana/Desktop/image-processing-exam/sample.jpg')

# Checking if the image was loaded correctly
if image is None:
    print("Error loading the image. Please check the file path.")
else:
    # Image processing tasks
    # Converting to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Resizing the image to 100x100 pixels
    resized_image = cv2.resize(image, (100, 100))

    # Applying Gaussian Blur to the image
    blurred_image = cv2.GaussianBlur(image, (5, 5), 0)

    # Displaying the images
    plt.figure(figsize=(15, 5))

    # Original Image
    plt.subplot(1, 4, 1)
    plt.title("Original")
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))  # Convert BGR to RGB for correct color display
    plt.axis('off')  # Hide axes

    # Grayscale Image
    plt.subplot(1, 4, 2)
    plt.title("Grayscale")
    plt.imshow(gray_image, cmap='gray')  # Grayscale images don't need BGR to RGB conversion
    plt.axis('off')  # Hide axes

    # Resized Image
    plt.subplot(1, 4, 3)
    plt.title("Resized")
    plt.imshow(cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB))  # Convert BGR to RGB
    plt.axis('off')  # Hide axes

    # Blurred Image
    plt.subplot(1, 4, 4)
    plt.title("Blurred")
    plt.imshow(cv2.cvtColor(blurred_image, cv2.COLOR_BGR2RGB))  # Convert BGR to RGB
    plt.axis('off')  # Hide axes

    plt.tight_layout()  # Adjust layout to avoid overlap
    plt.show()

    print("All image processing tasks completed successfully")



