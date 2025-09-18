from skimage import data
import numpy as np
import matplotlib.pyplot as plt
import cv2


def mirror_and_line(image, output_path="result.png"):
    """
    Takes an input image, creates its mirrored version,
    concatenates both images, draws a vertical white line
    and saves the result to a file.
    """
    try:
        if image is None or not isinstance(image, np.ndarray):
            raise ValueError("Image Error")
        h, w = image.shape[:2]  # Getting image height and width
        image_mirror = image[:, ::-1]  # Mirroring image
        result = cv2.hconcat([image, image_mirror])  # Concatenating original and mirrored images
        result = cv2.line(result, (w, 0), (w, h), (255, 255, 255), 5)  # Drawing line
        cv2.imwrite(output_path, cv2.cvtColor(result, cv2.COLOR_RGB2BGR))  # Convert RGB to BGR for correct work
        print(f"Result saved to {output_path}")
    except Exception as e:
        print(f"Error: {e}")  # Handling any possible errors


if __name__ == "__main__":
    img = data.astronaut()  # Loading image
    if img is None or not isinstance(img, np.ndarray):
        print("Image Error")
    else:
        mirror_and_line(img, "result.png")  # Processing and saving result image
