import qrcode
from PIL import Image


def generate_code(user_data):
    # Add data

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )

    qr.add_data(user_data)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image()

    # Save it somewhere, change the extension as needed:
    return img.save(user_data['name']+'.png')


if __name__ == '__main__':

    name = 'von MUKANYE'

    # The data that you want to store
    user_data = {
        'name': name,
        'mobile': 729309658,
        'country': 'KE',
        'image': ''
    }

    generate_code(user_data)
