from PIL import Image

def flip_image(image, mode='horizontal'):
    with Image.open(image) as img:
        if mode == 'horizontal':
            flipped_img = img.transpose(Image.FLIP_LEFT_RIGHT)
        elif mode == 'vertical':
            flipped_img = img.transpose(Image.FLIP_TOP_BOTTOM)
        return flipped_img