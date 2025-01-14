from PIL import Image, ImageEnhance

def adjust_brightness(image, factor):
    """
    Adjust the brightness of an image.
    :param factor: 1.0 means no change, less than 1.0 darkens, greater than 1.0 brightens.
    """
    with Image.open(image) as img:
        enhancer = ImageEnhance.Brightness(img)
        brightened_img = enhancer.enhance(factor)
        return brightened_img

def adjust_contrast(image, factor):
    """
    Adjust the contrast of an image.
    :param image: PIL.Image object
    :param factor: 1.0 means no change, less than 1.0 reduces contrast, greater than 1.0 increases contrast.
    :return: PIL.Image object with adjusted contrast.
    """
    with Image.open(image) as img:
        enhancer = ImageEnhance.Contrast(img)
        contrasted_img = enhancer.enhance(factor)
        return contrasted_img

def adjust_saturation(image, factor):
    """
    Adjust the saturation of an image.
    :param image: Input PIL.Image object or image file path
    :param factor: 1.0 means no change, less than 1.0 desaturates, greater than 1.0 increases saturation.
    :return: PIL.Image object with adjusted saturation
    """
    with Image.open(image) as img:
        enhancer = ImageEnhance.Color(img)
        saturated_img = enhancer.enhance(factor)
        return saturated_img
