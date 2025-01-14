from PIL import Image

def rotate_image(image, angle):
    with Image.open(image) as img:
        rotated_img = img.rotate(angle, expand=True)
        return rotated_img
