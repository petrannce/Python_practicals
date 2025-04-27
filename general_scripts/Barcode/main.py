import barcode
from barcode.writer import ImageWriter
from IPython.display import display, Image as IPImage

barcode_format = barcode.get_barcode_class('code128')

barcode_number = '1234567890123'

barcode_image = barcode_format(barcode_number, writer=ImageWriter())

barcode_filename = 'barcode_image'
barcode_image.save(barcode_filename)

display(IPImage(filename = f'{barcode_filename}.png'))