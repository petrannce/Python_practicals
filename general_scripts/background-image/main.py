from rembg import remove
from PIL import Image
import onnxruntime as ort

input_path = 'linda.jpg'
output_path = 'linda.png'

inp = Image.open(input_path)
output = remove(inp)
output.save(output_path)
Image.open(output_path)

# print('done')