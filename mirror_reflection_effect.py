from skimage import data
import numpy as np
import matplotlib.pyplot as plt
import cv2


def load_image():
    """Image loading function"""
    img = data.astronaut()  #Loading astronaut image
    if img is None or not isinstance(img, np.ndarray):
        raise ValueError("Failed to load image")
    return img  #Returns loaded image


def mirror_image(image):
    """Function for mirroring image"""
    if image is None or not isinstance(image, np.ndarray):
        raise ValueError("Failed to mirror image")
    return image[:, ::-1]  #Returns mirrored image


def concatenate_with_line(original, mirrored, line_width=5, line_color=(255, 255, 255)):
    """Function for concatenating and drawing line"""
    if original is None or mirrored is None:
        raise ValueError("Image Error")
    if original.shape != mirrored.shape:
        raise ValueError("Incorrect shapes of images")
    result = cv2.hconcat([original, mirrored])  #Concating images
    h, w = result.shape[:2]  #Getting height and wight of concated image
    result = cv2.line(result, (int(w/2), 0), (int(w/2), h), line_color, line_width)  #Drawing line
    return result


def save_image(image, output_path="result.png"):
    """Function for saving image"""
    if image is None or not isinstance(image, np.ndarray):
        raise ValueError("Failed to save image")
    image_bgr = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)  # Convertation from RGB to BGR for OpenCV correct work
    cv2.imwrite(output_path, image_bgr)  # Saving image
    print(f"Result saved to {output_path}")


def display_image(image):
    """Function for displaying image"""
    if image is None or not isinstance(image, np.ndarray):
        raise ValueError("Failed to display image")
    plt.figure(figsize=(10, 5))
    plt.imshow(image)
    plt.axis('off')
    plt.show()


if __name__ == "__main__":
    try:
        image = load_image()
        mirrored = mirror_image(image)
        result = concatenate_with_line(image, mirrored)
        save_image(result, "result.png")
        display_image(result)
    except Exception as e:
        print(f"Error: {e}")
