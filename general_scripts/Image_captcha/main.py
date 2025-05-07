from captcha.image import ImageCaptcha
from PIL import Image

# Specify the image size
image = ImageCaptcha(width=280, height=90)

# Specify the text to be displayed on the image
captcha_text = input("Enter the text for the captcha: ")

# Generate the captcha image
data = image.generate(captcha_text)

# Write the image to a file
image.write(captcha_text, 'captcha.png')

# Display the image
Image.open('captcha.png').show()

print(f"Captcha image with text '{captcha_text}' has been generated and saved as 'captcha.png'.")