import qrcode
from PIL import Image

data = input("Enter the data to generate QR code: ")
qr = qrcode.QRCode(
    version=3,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=8,
    border=4,
)

qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="aqua")

# Save the image to a file
img.save("qr_code.png")
Image.open("qr_code.png")

# Display the image
img.show()
