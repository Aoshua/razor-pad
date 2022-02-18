from PIL import Image

image = Image.open('img/icons8-knife-32.png')

imRotate = image.rotate(-45)
filename = "img/icons8-knife-32-r.png"
imRotate.save(filename)
print('File rotation complete.')
