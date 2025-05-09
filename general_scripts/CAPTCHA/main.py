from captcha.image import ImageCaptcha
from PIL import Image
import random

def generate_captcha(length=10):
    return ''.join(random.choices('string.ascii_letters + string.digits', k=length))

def generate_captcha_image(captcha_text, image_width=280, image_height=90):
    image = ImageCaptcha(image_width, image_height)
    image_file = f'captcha_{captcha_text}.png'
    image.write(captcha_text, image_file)
    return image_file

captcha_text = generate_captcha()
image_file = generate_captcha_image(captcha_text)

print(f"Captcha image with text '{captcha_text}' has been generated and saved as '{image_file}'.")
Image.open(image_file).show()
# pip install captcha