import qrcode


qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

# The data that you want to store
user_data = {
    'name': 'von MUTINDA',
    'mobile': 729309658,
    'country': 'KE',
    'image': ''
}



# Add data
qr.add_data(user_data)
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image()

# Save it somewhere, change the extension as needed:
img.save("image.jpg")




