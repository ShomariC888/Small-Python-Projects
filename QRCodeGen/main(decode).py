from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open('C:/Users/shoma/OneDrive/Desktop/Beginner_Files/QRCodeGen/new/myqrcode.png')

result = decode(img)

print(result)