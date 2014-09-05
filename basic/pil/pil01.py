# coding: utf-8
from PIL import Image

image = Image.open('Penguins.jpg')
print image.__class__
image.save('p.png')
# image.show()




