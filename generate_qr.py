import qrcode

name = 'von MUTINDA'
mobile = 729309658
country = 'KE'


img = qrcode.make( name+str(mobile)+country )

img.save('von.jpg')



''' 
now to embed image to a qr code 
'''
# from pyqrcode import QRCode
# from PIL import Image
# url = pyqrcode.QRCode('http://www.eqxiu.com',error = 'H')
# url.png('test.png',scale=10)
# im = Image.open('test.png')
# im = im.convert("RGBA")
# logo = Image.open('logo.png')
# box = (135,135,235,235)
# im.crop(box)
# region = logo
# region = region.resize((box[2] - box[0], box[3] - box[1]))
# im.paste(region,box)
# im.show()