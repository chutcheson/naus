import io
import base64
import os

from PIL import Image

class CivImage:
    def __init__(self, image, description):
        self.description = description
        self.image = image
        self.downsampled_image = self.downsample_image(image)
        self.downsampled_image_base64 = self.image_to_base64(self.downsampled_image)
    
    def downsample_image(self, image, size=(128, 128)):
        return image.resize(size, Image.ANTIALIAS)

    def image_to_base64(self, image):
        buffered = io.BytesIO() 
        image.save(buffered, format="PNG")
        return base64.b64encode(buffered.getvalue()).decode()

    def save(self, file_name, folder="../data"):
        if not os.path.exists(folder):
            os.mkdir(folder)
        file_path = os.path.join(folder, file_name)
        self.downsampled_image.save(file_path)
