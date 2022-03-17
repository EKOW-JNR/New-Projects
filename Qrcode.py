import qrcode
#from qrcode.image.pil import PilImage

data = 'Instagram.com/_lil.shaker_'

img = qrcode.make(data)

img.save('C:/Users/EKOW JR/Desktop/New/Instagram.png')
#type(img)