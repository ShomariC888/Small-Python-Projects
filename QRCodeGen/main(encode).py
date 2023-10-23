import qrcode

data = 'Don\'t forget to subscribe'

# img = qrcode.make(data)

# img.save('C:/Users/shoma/OneDrive/Desktop/Beginner_Files/QRCodeGen/new/myqrcode.png')

qr = qrcode.QRCode(version = 1, box_size=10, border=5)

qr.add_data(data)

qr.make(fit=True)
img = qr.make_image(fill_color = 'red', back_color = 'white')

img.save('C:/Users/shoma/OneDrive/Desktop/Beginner_Files/QRCodeGen/new/myqrcode1.png')