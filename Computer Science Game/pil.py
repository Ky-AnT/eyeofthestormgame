from PIL import Image

img = Image.open('brick_layers/1.gif')

img_resize = img.resize((10, 10))
img_resize.save('brick_layers/out.gif')

img_resize_lanczos = img.resize((10, 10), Image.LANCZOS)
img_resize_lanczos.save('brick_layers/out1.gif')
