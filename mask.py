from PIL import Image
import glob

img_to_paste = 'mask.png'

img2 = Image.open(img_to_paste)  # Image to paste into other images

count = 1  # Labels the new generated images

images = []  # List of opened images

# Opens all the images except the one to be pasted
for img in glob.glob('ben_afflek/*.png'):
    if img != img_to_paste:
        images.append(Image.open(img))

for imag in images:
    imag.paste(img2, (10, 150), mask=img2)
    imag.save(f'ben_afflek/pasted/{count}.png')
    count += 1
