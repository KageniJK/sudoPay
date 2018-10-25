import qrtools
from PIL import Image
from pyzbar.pyzbar import decode

def decode_id(data):
    data = decode(Image.open(data))
    print(data)



if __name__ == '__main__':
    decode_id('../von.jpg')
