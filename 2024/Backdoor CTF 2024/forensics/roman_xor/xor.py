from PIL import Image, ImageChops

im1 = Image.open("chall.png").convert('1')
im2 = Image.open("candidate.png").convert('1')

result = ImageChops.logical_xor(im1,im2)
result.save('result.png')