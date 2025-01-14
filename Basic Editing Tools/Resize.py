import Image from PIL

def resize(image, width, height, maintain_aspect_ratio=True):
    with Image.open(image) as img:
        if maintain_aspect_ratio:
            image=img.thumbnail(width,height)
        else:
            image=img.resize(width,height)
    return image