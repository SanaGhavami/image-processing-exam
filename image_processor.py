import cv2

# Reading the image
image = cv2.imread('C:/Users/Sana/Desktop/image-processing-exam/sample.jpg')

# Checking if the image is loaded correctly
if image is None:
    print("Error loading the image. Please check the file path.")
else:
    # Converting to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("grayscale_sample.jpg", gray_image)

    # Resizing the image
    resized_image = cv2.resize(image, (100, 100))
    cv2.imwrite("resized_sample.jpg", resized_image)

    # Applying Gaussian Blur
    blurred_image = cv2.GaussianBlur(image, (5, 5), 0)
    cv2.imwrite("blurred_sample.jpg", blurred_image)

    print("All image processing tasks completed successfully")


