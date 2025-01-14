from PIL import Image


def crop_image(image, coordinates, image_path=None):
    """
    Crop the image based on given coordinates
        image: image object
        coordinates: tuple of coordinates (left, upper, right, lower)
        image_path (optional): path to image. Defaults to None.
    """
    
    if(image_path!=None):
        image=Image.open(image_path)
        
    with Image.open(image) as img:
        cropped_img=img.crop(coordinates)
    return cropped_img