import qrcode

'''
Complex Version:
qr=qrcode.QRCode(
    version=10, #higher the version, complex the qr
    box_size=5,
    border=5 #white padding
)
'''
qr=qrcode.QRCode()

data="https://www.youtube.com/watch?v=dQw4w9WgXcQ"
qr.add_data(data)
img=qr.make_image()
# img.save("qr.png") #optional
img.show()